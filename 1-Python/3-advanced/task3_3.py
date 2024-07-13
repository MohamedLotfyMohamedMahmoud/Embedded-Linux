"""
Write a Python program to get the command-line arguments
"""

import sys

def main():
    # Get the command-line arguments
    args = sys.argv

    # Print the script name
    print(f"Script name: {args[0]}")

    # Print the number of arguments
    print(f"Number of arguments: {len(args) - 1}")

    # Print the arguments
    for i, arg in enumerate(args[1:], start=1):
        print(f"Argument {i}: {arg}")

if __name__ == "__main__":
    main()

