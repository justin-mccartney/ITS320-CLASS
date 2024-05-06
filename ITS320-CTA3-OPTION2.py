# ------------------------------
# Program Name: CTA3-OPTION2
# Author: Justin McCartney
# Date: 05-06-2024
# ------------------------------
# Pseudocode: [Below]
"""
- Store the different tax rates and income amounts
income tax rates {
    500 - 10%
    1500 - 15%
    ...
}

- Prompt user for income
    "Enter weekly income: "
    USER INPUT (float)

- Calculate tax rates
    tax rate = 0
    loop through bracket with for loop
        if income is found on / within bracket amounts ...
            tax rate is set to that rate
            break

- Calculate tax amount
    tax withheld = income * tax rate

- Print results
    print income
    print tax rate
    print tax withheld
"""
# ------------------------------
# Inputs: only income
# Outputs: income, tax rate, tax withheld
# ------------------------------
# Income brackets and tax rates
income_tax_rates = {
    500: 0.10,
    1500: 0.15,
    2500: 0.20,
    float('inf'): 0.30
}

# Input user income
income = float(input("Enter weekly income: "))

# Calculate tax rate
tax_rate = 0
for bracket, rate in income_tax_rates.items():
    if income < bracket:
        tax_rate = rate
        break

# Calculate tax amount
tax_withheld = income * tax_rate

# Print outputs
print(f"Income: ${income:.2f}")
print(f"Tax rate: {tax_rate*100:.0f}%")
print(f"Tax Withheld: ${tax_withheld:.2f}")