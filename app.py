import os
import json
import re
import chainlit as cl
from openai import AsyncOpenAI
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

car_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "dataset1.csv"))

print(car_df.head())

#setting up the open_ai api
client = AsyncOpenAI(
                        api_key = os.getenv("OPENROUTER_API_KEY") ,
                        base_url= "https://openrouter.ai/api/v1"
)

#filling fixed prompt (wont be consider if user gave none)
def df_filt(car_df, prefs):
    size_map = {
    "Sedan": "Mid",
    "SUV": "High",
    "Hatchback": "Low"
    }
    if prefs.get("Size") in size_map:
        prefs["Size"] = size_map[prefs["Size"]]
    filt_df = car_df.copy()
    for field in ["Fuel", "Color", "Transmission", "Size"]:
        if prefs.get(field):
            temp_df = filt_df[filt_df[field] == prefs[field]]
            if not temp_df.empty:
                filt_df = temp_df
            else:
                print(f"[df_filt] Skipping filter for {field} - no match")
    print("[df_filt] Before:", len(car_df), "→ After:", len(filt_df))
    return filt_df


#rank based filtering for the remaining fields
def ranked_filter(car_df,prefs):
    filtered_df = car_df.copy()
    
    # #price filter
    # if(prefs.get("Price (INR)")):
    #     filtered_df = filtered_df[filtered_df["Price (INR)"] == prefs["Price (INR)"]]
    
    #luxury filter
    user_lux = prefs.get("Luxury" , "High")
    lux_order = ["High" , "Mid" , "Low"]
    lux_df = filtered_df[filtered_df["Luxury"] == user_lux]
    if lux_df.empty:
        for lux in lux_order:
            if lux == user_lux:
                continue
            alt_df = filtered_df[filtered_df["Luxury"] == lux]
            if not alt_df.empty:
                lux_df = alt_df
                break
    filtered_df = lux_df

    #safety filter
    user_saf = prefs.get("Safety" , 5)
    saf_order = [5,4,3,2,1]
    saf_df = filtered_df[filtered_df["Safety"] == user_saf]
    if saf_df.empty:
        for saf_lvl in saf_order:
            if saf_lvl == user_saf:
                continue
            safalt_df = filtered_df[filtered_df["Safety"] == saf_lvl]
            if not safalt_df.empty:
                saf_df = safalt_df
                break
    filtered_df = saf_df


    #mileage filter
    user_mil = prefs.get("Avg Mileage (kmpl)")
    if user_mil:
        mil_df = filtered_df[filtered_df["Avg Mileage (kmpl)"] == user_mil]
        if mil_df.empty:
            mil_val = sorted(filtered_df["Avg Mileage (kmpl)"].unique() , reverse=True)
            for val in mil_val:
                if val >= user_mil:
                    continue
                mil_df = filtered_df[filtered_df["Avg Mileage (kmpl)"] == val]
                if not mil_df.empty:
                    break
    else:
        mil_val = sorted(filtered_df["Avg Mileage (kmpl)"].unique() , reverse=True)
        for val in mil_val:
            mil_df = filtered_df[filtered_df["Avg Mileage (kmpl)"] == val]
            if not mil_df.empty:
                break
    filtered_df = mil_df


    #price filter
    user_price = prefs.get("Price (INR)")
    if user_price:
        price_df = filtered_df[filtered_df["Price (INR)"] <= user_price]
        if price_df.empty:
            price_val = sorted(filtered_df["Price (INR)"].unique())
            for val in price_val:
                if val > user_price:
                    continue
                price_df = filtered_df[filtered_df["Price (INR)"] <= val]
                if not price_df.empty:
                    break
    else:
        price_val = sorted(filtered_df["Price (INR)"].unique())
        for val in price_val:
            price_df = filtered_df[filtered_df["Price (INR)"] <= val]        
            if not price_df.empty:
                break
    filtered_df = price_df
    print("[ranked_filter] Final count:", len(filtered_df)) #here for checking shud be removed after
    return filtered_df


    

async def extract_info(user_input: str):
    prompt = f"""
You are a helpful car sales assistant. Extract the user's car preference from the message below.

Return the result as a JSON with these **exact keys and formats** (match the values from the dataset):

- Fuel: Petrol, Diesel, Electric, Hybrid
- Color: Must be a valid color from a real car (like Red, Blue, Black, White, etc.)
- Price (INR): Integer only. Give approximate expected price in INR (example: 1500000)
- Transmission: Manual or Automatic
- Avg Mileage (kmpl): Integer only (e.g. 15, 18, 20)
- Size: Choose from: Hatchback, Sedan, SUV, MPV
- Luxury: Choose from: Low, Mid, High
- Safety: Choose only from: 3, 4, 5 (numeric)

Do not add any extra text or explanation. Only return clean, parseable JSON.

User message: \"{user_input}\"
"""

    response = await client.chat.completions.create(
        model = "google/gemma-3n-e4b-it:free" ,
        messages = [{"role": "user" , "content": prompt}]
    )
    content = response.choices[0].message.content.strip()
    content_cleaned = re.sub(r"^```json\s*|\s*```$", "", content.strip(), flags=re.MULTILINE)
    try:
        prefs = json.loads(content_cleaned)
        return prefs
    except:
        print("Could not parse JSON", content)
        return None



@cl.on_message
async def handle_user_message(message: cl.Message):
    # Get what the user typed
    user_input = message.content
    prefs = await extract_info(user_input)
    
    if prefs is None:
        await cl.Message(content="Sorry, I couldn't understand your preferences").send()
        return 
    
    await cl.Message(content = f"Extracted preferences: \n{prefs}").send()
    
    filtered = df_filt(car_df , prefs)

    ranked = ranked_filter(filtered , prefs)
    print("\n[prefs]", prefs)
    print("[DF] Unique Fuel:", car_df["Fuel"].unique())
    print("[DF] Unique Color:", car_df["Color"].unique())
    print("[DF] Unique Transmission:", car_df["Transmission"].unique())
    print("[DF] Unique Size:", car_df["Size"].unique())

    if ranked.empty:
        await cl.Message(content="Sorry, no cars match your preferences.").send()

    else:
        top_cars = ranked.head(5).to_string(index=False)
        await cl.Message(content=f"Top car matches:\n{top_cars}").send()


@cl.on_chat_start
async def start():
    await cl.Message(content = "Welcome to our Car Dealership Assistant").send()
    await cl.Message(content = "Explain your Car Preferences for purchase").send()
