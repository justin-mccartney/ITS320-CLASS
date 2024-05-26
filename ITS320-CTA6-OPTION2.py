# ------------------------------
# Program Name: CTA6-OPTION2
# Author: Justin M.
# Date: 05-26-2024
# ------------------------------
# Pseudocode: [Below]
"""
    Function 1: cartesian product function(first list, second list) - lists are parameters
        create product of both lists
        return said product

    Function 2: main function()
        # create list A -
            users input numbers to fill the list
            ensure that list is no longer than ten values long
            separate the list values using commas upon input
        # create list B -
            users input numbers to fill the list
            ensure that list is no longer than ten values long
            separate the list values using commas upon input

        # failsafe - ensure that lists are no longer than ten elements
            if list A or list B are longer than ten elements
                OUTPUT: Lists are longer than ten elements
                return

        # prepare result ...
            result = cartesian product(list A, list B)

        print result
            OUTPUT: result ...
"""
# ------------------------------
# Inputs: values to fill list A and list B
# Outputs: Prompts for input, and input warning, as well as the final result (cartesian product)
# ------------------------------
# Import, allows for use of "product" in order to create cartesian product
from itertools import product

# Function which will return the product of two lists
# NO PRINTING FROM THE FUNCTION
def cartesian_product(A, B):
    return list(product(A, B))

# Main function
def main():
    # Print warning which will ensure that user enters no more than ten values
    print("\nWARNING: Before submitting lists, please make sure they have no more than TEN items.")

    # Input the numbers for list A - separate using commas
    A = list(map(int, input("\nEnter the elements of the first list, separate each item using a comma: ").split(',')))

    # Input the numbers for list B - separate using commas
    B = list(map(int, input("\nEnter the elements for the second list, separate using commas once again: ").split(',')))

    # Ensuring that each list only has ten values stored - fail protection
    if len(A) > 10 or len(B) > 10:
        print("Error! Each list should have no more than ten items.")
        return

    # Creating the result of the program - cartesian product
    result = cartesian_product(A, B)

    # Output ...
    print("AxB: ", result)

if __name__ == "__main__":
    main()