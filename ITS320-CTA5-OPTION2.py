# ------------------------------
# Program Name: CTA5-OPTION2
# Author: Justin McCartney
# Date: 05-19-2024
# ------------------------------
# Pseudocode: [Below]
"""
FIRST FUNCTION:
    process_strings(string 1, string 2, and string 3)
        concatenated string = string 1 + string 2

        reversed string = reverse ... string 3
        print(reverse string)

        return concatenated string

SECOND FUNCTION:
    main()
        Prompt the user to enter three strings
        string 1 = INPUT
        string 2 = INPUT
        string 3 = INPUT

        result = process_strings(string 1, string 2, string 3)

        print(result)
"""
# ------------------------------
# Inputs: three individual strings
# Outputs: result, which will be the concatenated string, and the reversed string
# ------------------------------
# Define the first function
def process_strings(string_one, string_two, string_three):
    # Creating the concatenated string
    concatenated_string = string_one + " " + string_two

    # Returning the concatenated string
    return concatenated_string

def main():
    # Prompting user for the three string inputs
    string_one = input("Enter your first string: ")
    string_two = input("Enter your second string: ")
    string_three = input("Enter your third string: ")

    # Creating and printing string three, in reverse
    reversed_string_three = string_three[::-1]
    print("Reversed String 3: ", reversed_string_three)

    # Calling the strings function, and input the three user inputs
    result = process_strings(string_one, string_two, string_three)

    # Print the concatenated string
    print("Concatenated String: ", result)

# Ensures that when main is called only when the script is run directly
if __name__ == "__main__":
    main()
