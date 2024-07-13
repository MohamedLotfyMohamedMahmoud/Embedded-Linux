 

""" 
name2:str="mohamed"
print(type(name2))
 """
""" 
name="mohaemd"
print(type(name))

name=name.capitalize()
print(name)

name=name.casefold()
print(name)

name=name.center(20)
print(name)

name=name.count('m')
print(name) 
"""

""" 
name="mohamed lotfy"
name=nmae.end

 """


""" 
name="mohamed lotfy"
print(name.startswith("mohamed"))
print(name.endswith("lotfy"))
print(name.endswith("mohamed"))

 """
"""
name="mohamed lotfy"
print(name.find("lotfy"))
print(name.find('m',2)) 
"""
"""
name="  mohamed  lotfy  "
print(name.strip())
name="MOHAMED LOTFY"
print(name.lower())
name="  mohamed lotfy  "
print(name.upper().strip())
print(name.lower())

name=" mohamed ,lotfy "
print(name.replace(" ","_"))

name="mohamed lotfy"
print(name.split(" "))
print(type(name.split(" ")))

name="mohamed , lotfy"
print(name.split(","))
print(type(name.split(",")))

txt="there is rain in spain stays mainly in plain"
x= "wmn" in txt 
print(x)
print(type(x))
 """
""" 
age=25
txt="my name mohamed , i am {}"
print(txt.format(age))
 """
""" 
age=25
print("my name mohamed , i am {}".format(age))
 """""" 
quantity=3
itemno=567
price=49.95
my_order="i want to {} piece of item {} for dollars"
print(my_order.format(quantity,itemno,price))
 """
""" 
quantity=3
itemno=567
price=49.95
my_order="i pay {2} doller for {0}piece of item{1}"
print(my_order.format(quantity,itemno,price))
 """
"""
name=["how", "are","you","today?"]
print(" ".join(name))

name=["how", "are","you","today?"]
print("_".join(name))

num="1234" # or num="mojsd4"
print(num.isalnum())

num="1234"
print(num.isdecimal())

num="mojsd4"
print(num.isdecimal())

num="1234"
print(num.isdigit())

num="mojsd4"
print(num.isdigit())
 """
 #four method to print string with string substitution
""" 
x=10
print("wlcome number: "+str(x)+" hello")
print("wlcome number: {} hello".format(x))
print(f"wlcome number: {x} hello")
print("wlcome number: %d hello"%x)
 """
#help()
""" 
def my_function():
    print("my name is mohamed")

my_function()
 """
""" 
def my_function(f_name):
    print("my name is {}".format(f_name))

my_function("mohamed") 
"""
""" 
def my_function(num):
    return num*5
print(my_function(5))
print(my_function(4))
print(my_function(3))
 """
""" 
def my_funtion():
    pass  #becuse function can not be empty so we put pass
my_funtion() 
"""

""" 
def my_function(child3,child2,child1):
    print("the youngest child is "+child3)

my_function("mohamed","ali","ahmed")
my_function("mohamed",child2="ali",child1="ahmed")
my_function(child2="mohamed",child1="ali",child3="ahmed") 
"""
""" 
def my_function(country="egypt"):
    print("i am from "+country)

my_function("india")
my_function("sweden")
my_function() 
"""

""" 
def my_function(*kids):
    print(type(kids))
    print("the youngest kids "+kids[2])
my_function("mohmaed","ali","ahmed") 
""" 

""" 
def my_function(**name):
    print(type(name))
    print("his las name is "+name["last_name"])

my_function(first_name="moahmed",last_name="lotfy")
 """
""" 
def my_function(d):
    for key in d:
        print("key :",key,"value :",d[key])

D={'a':1,'b':2,'c':3}
my_function(D)
"""

""" 
x=555
def my_functoin():
    x=111
    print(id(x))
    print("x=",x)
my_functoin()    
print(id(x))
print("x=",x)
 """
""" 
x=555
def my_functoin():
    global x
    x=111
    print(id(x))
    print("x=",x)
my_functoin()    
print(id(x))
print("x=",x) """

""" 
x=lambda a :a+50
print(x(4))
 """
""" 
x=lambda a,b:a*b
print(x(8,9)) 
"""

""" 
list=[10,51,81,11,63]
list.sort()
print("the largest element :",list[-1]) 
"""
""" 
list=[10,51,81,11,63]
print("the largest element :",max(list)) 
"""

""" 
import requests
url=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(url.json())

 """

""" 
import requests
from pprint import pprint
url=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
pprint(url.json()) 
"""
""" 
import util1
print(util1.sum(9,6))

import util_file.util2
print(util_file.util2.mul(5,4))

import util_file.util2 as op
print(op.mul(5,4))

from util_file.util2 import mul
print(mul(4,5)) 
"""
#BUILT IN module
""" 
import platform
print(platform.system())
print(platform.release())
print(platform.version())
print(platform.machine())
print(platform.processor())
print(platform.architecture())
print(platform.node()) 
"""
""" 
list=[1,2,3,4,"mohamed","lotfy"]
list.append("python")
print(list)
list2=list.copy()
print(list2)
list2.clear()
print(list2)
print(list.index("mohamed"))
list.insert(6,"mohamed")
print(list)
list.remove("python")
print(list)
pop_value=list.pop(3)
print("pop_value =",pop_value)
print(list)
list.reverse()
print(list)
del list[0]
print(list)
 """
""" 
list=[1,1.3,"hi",1]
for i in list:
    print(i)
    print(type(i))
 """
""" 
list=[1,1.3,"hi",1]
print(list)
print(len(list))
 """
""" 
list=[10,20,30,40,50,60,70]
print(list[:])
print(list[::])
print(list[::2])
print(list[1:1])
print(list[-1])
print(list[-1:])
print(list[-1::-1])
print(list[-1:-1])
 """
""" 
list=[15,10,152,100,2]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
 """
""" 
list=['a','b',["cc","dd",["eee","fff"]],'g','h']
print(list[2])
print(list[2][2])
print(list[2][2][0])
list[2].insert(0,"xx")
print(list) 
"""

""" mytuple=(1,2,3,4,5,6)
print(mytuple[-4:-1])
 """
 # program sleep for two sec to put cursor in position that wante to write hello world 
""" 
import pyautogui
from time import sleep
sleep(2)
pyautogui.write("Hello world")
 """
""" myset = {"apple", "banana", "cherry"}

# List with new elements
new_fruits = ["orange", "mango", "grape"]

# Updating the set with elements from the list
myset.update(new_fruits)

# Printing the updated set
print("Updated set:", myset)
 """
#program print position of mouse
""" 
import pyautogui
from time import sleep
while True:
    print(pyautogui.position()) 
"""
#program to move mouse to position you wante
""" 
import pyautogui
from time import sleep
pyautogui.moveTo(100,100)
sleep(1) 
"""
#program run visual studio automatic 
""" 
import pyautogui
from time import sleep
try:
    location=None
    while location is None:
        location=pyautogui.locateOnScreen("play.png")
        sleep(1)
        pyautogui.moveTo(location.left+25,location.top+7)
        pyautogui.click(location.left+25,location.top+7)
except pyautogui.ImageNotFoundException:
    print("Image not Found") 
"""
#program open terminatin using pyautoGui
""" 
import pyautogui
from time import sleep
pyautogui.hotkey('win','r')
pyautogui.typewrite('cmd')
sleep(2)
try:
    location=None
    while location is None:
        location=pyautogui.locateOnScreen('terminal.png')
        pyautogui.moveTo(location.left+location.width-40,location.top+location.height-45,duration=1)
        pyautogui.click(location.left+location.width-40,location.top+location.height-45)
except pyautogui.ImageNotFoundException:
    print("Image not Found") 
"""
"""
# not work with me
import pyautogui
from time import sleep
import webbrowser

# URL of the Google Sheets document
url = "https://docs.google.com/spreadsheets/d/15DWVmMf326eZN5qj-y34EUPj4J2EJ3sX/edit?usp=drive_link&ouid=116328957113911525564&rtpof=true&sd=true"
webbrowser.open(url,new=2)  
sleep(3)
try:
    location = None
    while location is None:
        # Try to locate the image on the screen
        location = pyautogui.locateOnScreen('name2.png',confidence=0.9)
        sleep(1)
        
except pyautogui.ImageNotFoundException:
    print("Image not found")
    exit()
pyautogui.click(location.left+250,location.top+30) 
pyautogui.keyDown('shift')
pyautogui.press('right')
for i in range(0,5):  
    pyautogui.press('down')
    sleep(0.1) 
pyautogui.keyUp('shift')     
pyautogui.hotkey('delete')

"""

