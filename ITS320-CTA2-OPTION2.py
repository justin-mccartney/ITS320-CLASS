# ------------------------------
# Program Name: CTA2-OPTION2
# Author: Justin McCartney
# Date: 04-28-2024
# ------------------------------
# Pseudocode: [Below]
"""
- Prompting the user for the car info ...
INPUT: Brand (string)
INPUT: Model (string)
INPUT: Year (string)
INPUT: Odometer Start (float)
INPUT: Odometer End (float)
INPUT: MPG (float)

- Calculate miles driven ...
total_miles (float) = end odo - start odo

- Calculate gallons used ...
total_gallons (float) = miles / mpg

- Create dictionary to store car info ...
car_info = {brand, model, ..., total_gallons}

- Output car info ... loop through dictionary
for loop
    car info ...
"""
# ------------------------------
# Inputs: All car info, i.e. Brand, model, year, odo start, odo end, MPG ...
# Outputs: Dictionary with all car info - including total miles and total gallons ...
# ------------------------------
# Collecting user inputs for all the vehicle information
brand = input("Enter the brand of vehicle: ")
model = input("Enter the model of vehicle: ")
year = input("Enter the year of vehicle: ")
odometer_start_reading = float(input("Enter the starting odometer reading: "))
odometer_end_reading = float(input("Enter the ending odometer reading: "))
mpg = float(input("Enter the MPG of the vehicle: "))

# Calculating total miles travelled
total_miles = odometer_end_reading - odometer_start_reading

# Calculating total gallons used
total_gallons = total_miles / mpg
round(total_gallons, 2)

# Dictionary that stores the vehicles information
car_info = {
    "brand": brand,
    "model": model,
    "year": year,
    "odometer_start_reading": odometer_start_reading,
    "odometer_end_reading": odometer_end_reading,
    "mpg": mpg,
    "total_miles": total_miles,
    "total_gallons": total_gallons
}

# Print the vehicle information dictionary - for loop that is printing information
print("\nCar information:")
for key, value in car_info.items():
    print(f"{key}: {value}")