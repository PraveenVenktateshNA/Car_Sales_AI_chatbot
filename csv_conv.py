csv_text = """Company,Model,Model Year,Type,Fuel,Color,Price (INR),Transmission,Avg Mileage (kmpl),Size,Luxury,Safety
Toyota,Fortuner 4.0L,2023,SUV,Petrol,Pearl White,2900000,Automatic,10.5,High,Mid,5
Honda,City ZX,2023,Sedan,Petrol,Metallic Grey,1100000,CVT (Auto),12,Mid,Low-Mid,4
Hyundai,Tucson Hybrid,2024,SUV,Hybrid,Phantom Black,2450000,Automatic,18.5,Mid-High,Mid,5
Mahindra,Scorpio N,2022,SUV,Diesel,Red,1600000,Manual,14,High,Mid,4
Tata,Nexon EV,2023,SUV,Electric,Blue,1750000,Automatic,30 (eQM range),Mid,Low,4
Kia,Seltos GTX,2023,SUV,Petrol,White,1650000,Automatic,16,Mid,Mid,5
Ford,EcoSport,2021,SUV,Petrol,Black,950000,Manual,15,Mid,Low,4
Renault,Kwid,2023,Hatchback,Petrol,Yellow,450000,Manual,18,Low,Low,3
BMW,X3 xDrive30i,2023,SUV,Petrol,Black,6200000,Automatic,12,High,High,5
Mercedes,GLC 300,2023,SUV,Petrol,Silver,6500000,Automatic,11,High,High,5
Honda,Amaze,2023,Sedan,Petrol,Red,700000,Manual,18,Low-Mid,Low,4
Hyundai,i20,2023,Hatchback,Petrol,Grey,800000,Manual,19,Low-Mid,Low,4
Tata,Harrier,2022,SUV,Diesel,White,1500000,Manual,15,Mid-High,Mid,5
Kia,Carnival,2023,MPV,Petrol,Blue,2800000,Automatic,13,High,High,5
Toyota,Camry Hybrid,2023,Sedan,Hybrid,White,3700000,Automatic,23,Mid-High,High,5
Ford,Endeavour,2022,SUV,Diesel,Blue,3100000,Manual,13,High,Mid,5
Renault,Duster,2023,SUV,Diesel,Grey,1000000,Manual,17,Mid,Low,4
BMW,3 Series,2023,Sedan,Petrol,White,4500000,Automatic,14,Mid,High,5
Mercedes,C-Class,2023,Sedan,Petrol,Black,4800000,Automatic,13,Mid,High,5
Hyundai,Venue,2023,SUV,Petrol,Red,850000,Manual,18,Low-Mid,Low,4
Tata,Punch,2023,SUV,Petrol,Blue,650000,Manual,18,Low,Low,4
Kia,Sonet,2023,SUV,Petrol,White,800000,Manual,17,Low-Mid,Low,4
Mahindra,Thar,2023,SUV,Petrol,Green,1300000,Manual,14,Mid,Mid,4
Honda,Jazz,2023,Hatchback,Petrol,Silver,950000,CVT (Auto),17,Low-Mid,Low,4
Toyota,Glanza,2023,Hatchback,Petrol,Red,700000,Manual,19,Low-Mid,Low,4
Hyundai,Creta,2023,SUV,Petrol,Black,1400000,Automatic,16,Mid,Mid,5
Renault,Kiger,2023,SUV,Petrol,White,700000,Manual,18,Low-Mid,Low,4
Ford,Figo,2023,Hatchback,Petrol,Blue,650000,Manual,18,Low,Low,4
BMW,X1 sDrive20i,2023,SUV,Petrol,White,4700000,Automatic,13,Mid,High,5
Mercedes,GLA 200,2023,SUV,Petrol,Silver,5000000,Automatic,12,Mid,High,5
Honda,WR-V,2023,SUV,Petrol,Red,950000,Manual,17,Low-Mid,Low,4
Tata,Altroz,2023,Hatchback,Petrol,Blue,700000,Manual,19,Low-Mid,Low,4
Kia,Carens,2023,MPV,Petrol,White,1500000,Automatic,14,Mid-High,Mid,5
Mahindra,Marazzo,2023,MPV,Diesel,Black,1300000,Manual,16,Mid,Mid,5
Hyundai,Verna,2023,Sedan,Petrol,Red,1300000,Automatic,17,Mid,Mid,5
Toyota,Innova Crysta,2023,MPV,Diesel,White,1800000,Manual,14,Mid-High,Mid,5
Ford,Aspire,2023,Sedan,Petrol,Blue,900000,Manual,18,Low-Mid,Low,4
Renault,Triber,2023,MPV,Petrol,Yellow,600000,Manual,20,Low-Mid,Low,4
BMW,5 Series,2023,Sedan,Petrol,Black,7500000,Automatic,12,High,High,5
Mercedes,E-Class,2023,Sedan,Petrol,White,8000000,Automatic,11,High,High,5
Hyundai,i10,2023,Hatchback,Petrol,Red,600000,Manual,20,Low,Low,4
Tata,Tiago,2023,Hatchback,Petrol,Blue,600000,Manual,19,Low,Low,4
Kia,Stonic,2023,SUV,Petrol,Green,1200000,Automatic,16,Mid,Mid,5
Mahindra,XUV700,2023,SUV,Diesel,Black,2200000,Automatic,14,High,Mid,5
Honda,CR-V,2023,SUV,Petrol,Silver,3200000,Automatic,15,Mid,Mid,5
Toyota,Yaris,2023,Sedan,Petrol,White,1200000,Automatic,18,Low-Mid,Low,4
"""

with open("realistic_car_dataset_50.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)

print("CSV file 'realistic_car_dataset_50.csv' created successfully!")
