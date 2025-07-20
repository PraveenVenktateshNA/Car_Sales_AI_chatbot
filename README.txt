Car Recommendation AI Assistant

This is an AI based project built with Chainlit that uses Natural Language as prompt and converts into JSON Format for the program to work with.

I can guess your thoughts about this, you may think "I can just put the same prompt to chatgpt or anyother AI and it can give a better answer than my project", yes its not as good as you think but the main point of this project is its reusability of the part where it can convert your Natural Language into a JSON format which u can play with in any way and create your own logic.

Overview

The assistant helps users find cars based on their spoken or written preferences like:
- "I want a red automatic SUV under 12 lakhs with good mileage."
- "Looking for a safe petrol hatchback for city driving."

It then:
1. **Extracts the preferences** from the prompt using an LLM.
2. **Converts them to JSON.**
3. **Filters and ranks** cars from the dataset based on these preferences.

Tech Stack

-  **Chainlit** (LLM-based interface)
-  **Python (Pandas)**
-  **OpenRouter / OpenAI API**
-  **CSV dataset**
-  Runs locally with terminal or browser interface


Project Structure

Car_AI/
├── .env # API key and secret settings (should NOT be pushed)
├── app.py # Main Chainlit app logic
├── dataset1.csv # Car dataset
├── requirements.txt # Dependencies
└── README.md # Project info (this file)


Inorder for the program to run: 
  pip install -r requirements.txt 
  Add ur .env file:
              AI_KEY = your_ai_model_key
  Run the app:
          chainlit run app.py

Thanks for visiting Project :)












