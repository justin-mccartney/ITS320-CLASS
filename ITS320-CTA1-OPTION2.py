# ------------------------------
# Program Name: CTA1-OPTION2
# Author: Justin McCartney
# Date: 4-20-2024
# ------------------------------
# Pseudocode: [Below]
"""
print(enter an integer)
    a = INPUT
print(enter another integer)
    b = INPUT

print(OUTPUTS)
    print(a // b) - integer division
    print(a / b) - float division
    print(a % b) - modulo division
"""
# ------------------------------
# Inputs: two individual integers
# Outputs: output the outcome of... integer division, float division, and modulo division
# (as well as the prompts for user input and the heading for the output)
# ------------------------------
# Reading integers in from the user ...
print("Enter an integer: ")
a = int(input())
print("Enter a second integer: ")
b = int(input())

# Printing results for all operations ...
print("Outputs:")
print(a // b)   #Integer division
print(a / b)    #Float division
print(a % b)    #Modulo division