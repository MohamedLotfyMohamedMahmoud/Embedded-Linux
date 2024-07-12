""" 
Write a Python program to count the number 4 in a given list.
"""

numbers_input = input("Enter integers separated by spaces: ")

my_list = [int(num) for num in numbers_input.split()]

print("List of numbers entered:", my_list)

i,k=0,0
for i in my_list:
    if 4==i:
        k=k+1
print("count the number Four :",k)    

