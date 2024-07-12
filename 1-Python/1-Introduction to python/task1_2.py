"""
Write a Python program to test whether a passed letter is a vowel or not. 
"""
vowel_character=['A','E','I','O','U','a','e','i','o','u']
char=input("plz enter your character :")
if char in vowel_character:
    print(char,"is vowel character")
else:print(char,"is not vowel character")    