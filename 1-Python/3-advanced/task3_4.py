""" 
Python program to get the ASCII value of a character 
"""

def get_ascii_value(character):
    return ord(character)

def main():
    # Prompt the user to enter a character
    char = input("Enter a character: ")
    
    # Ensure that the user inputs exactly one character
    if len(char) != 1:
        print("Please enter exactly one character.")
        return
    
    # Get and print the ASCII value
    ascii_value = get_ascii_value(char)
    print(f"The ASCII value of '{char}' is {ascii_value}.")

if __name__ == "__main__":
    main()
