# ------------------------------
# Program Name: CTA4-OPTION2
# Author: Justin McCartney
# Date: 05-12-2024
# ------------------------------
# Pseudocode Below:
"""
Initialize values -
    total = 0
    maximum ...
    minimum ...

Read user input - grades
    for loop
        grade = enter grade: INPUT
        total = total + grade
        if grade > maximum
            maximum = grade
        if grade < minimum
            minimum = grade

Calculate average
    average = total / 5

Print statistics
    print average
    print maximum
    print minimum
"""
# Initialize values
total = 0
maximum = float('-inf')
minimum = float('-inf')

# Reading grades from user input
for i in range(5):
    grade = float(input("Enter grade: "))
    total += grade
    if grade > maximum:
        maximum = grade
    if grade < minimum:
        minimum = grade

# Calculate average
average = total / 5

# Print statistics
print("Average: ", average)
print("Maximum: ", maximum)
print("Minimum: ", minimum)