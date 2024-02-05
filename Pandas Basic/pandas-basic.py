import pandas as pd

# Create a DataFrame with car data
car_data = {
    'Car Model': ['Toyota Camry', 'Honda Accord', 'Ford Mustang', 'Chevrolet Malibu', 'Tesla Model 3'],
    'Year': [2022, 2021, 2022, 2021, 2022],
    'Color': ['Silver', 'Blue', 'Red', 'Black', 'White'],
    'Price': [25000, 28000, 35000, 30000, 45000],
    'Mileage': [15000, 12000, 8000, 20000, 5000]
}

car_df = pd.DataFrame(car_data)

# Display the DataFrame
print(car_df)

# Export the DataFrame to an Excel file
car_df.to_excel('car_data.xlsx', index=False)

car_df_from_excel = pd.read_excel('car_data.xlsx')
print(car_df_from_excel)

print(car_df_from_excel[['Car Model', 'Year']])

print(car_df_from_excel[0:4])