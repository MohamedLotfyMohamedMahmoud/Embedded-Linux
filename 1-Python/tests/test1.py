""" 
x=5
print(type(x))
x="Mohamed"
print(type(x))
x=3.5
print(type(x)) 
"""


"""
x,y,z=1,2,3
print(x)
print(y)
print(z) 
"""

# Data Type
""" x="Mohammed"
print(x)
print(type(x))
y=5
print(y)
print(type(y))

z=3.55
print(z)
print(type(z))

w=3+4j
print(w)
print(type(w))
"""

""" 
x=[1,2,3,4,5]
print(x)
print(type(x))

y=(1,2,3,4,5)
print(y)
print(type(y))


z=range(1,5)
print(z)
print(list(z))
print(type(z)) 
"""



#x=[1,2,3,4,5]
#print(x[0:5:2])
#print(x[1:4])
#print(x[1:])
#print(x[-4])

""" 
x=True
print(x)
print(type(x))
 """
#print(bool("Hello"))
#print(bool("False"))
#print(bool(False))
#print(bool("None"))
#print(bool(None))
#print(bool(12))
#print(bool(0))
""" 
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({})) 
"""
""" 
x=["mohamed",2,4,5.4,12]
print(x)
print(x[0])
x[0]=99
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x) 
"""
""" 
x=("mohamed",2,4,5.4,12)
print(x)
print(x[0])
#x[0]=99    ---->immutable
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
"""
""" 
thisdict={
    "brand":"Ford",
    "electric":False,
    "year":1946,
    "color":["red", "white", "blue"]
}
 """
 #print(type(thisdict))
#print(thisdict)
#print(thisdict["brand"])
""" 
print(thisdict["color"])
print(thisdict["color"][0])
print(thisdict["color"][1])
print(thisdict["color"][2]) 
"""
""" 
print(thisdict.keys())
print(thisdict.values())
print(len(thisdict)) 
"""

""" 
thisset={"apple","banana","cherry"}
print(type(thisset))
print(thisset)
 """

""" 
for i in range(5):
    print(i,end=",")
print("")
 """
""" 
for i in range(0,5):
    print(i,end=",")
print("")     
"""
""" 
for i in range(1,10:2):
    print(i,end=",")
print("")     
"""
""" 
x=list(range(0,10))
print(x) 
"""

""" 
x="mohamed"
print(list(x)) 
"""
""" 
input_name=input("plz enter your name :")
print("Hello ," +input_name)
age=input("plz enter your age :")
print(" your age :"+str(age)+" yours old") 
"""
""" 
x,y=27,2
print(x**y)
print(x/y)
print(x//y) 
"""
""" 
x,y=12,14
if x>10 and y>10:
    print("Hello") 
"""
""" 
x,y=12,14
print(x&y)
print(x|y)
print(x^y)
print(~y)
"""
""" 
print(1 in [1,2,3,4,5])
print(8 in [1,2,3,4,5])
print(8 not in [1,2,3,4,5])
print(1 not in [1,2,3,4,5]) 
"""
""" 
x=5
y=5
print(id(x))
print(id(y))
if x is y:    
    print("x is y")
if x==y: 
    print("x equal to y") 
"""
""" 
x=[10]
y=[10]
if x is not y:
    print("x is y")
if x==y:
    print("x is equal to y")    
"""
""" 
x,y=50,15
if y>x:
    print("y is greater than y")
elif x==y:
    print("x is equa to y")
else:
    print("x is greater than y") 
"""
""" 
x,y=50,15
if y>x:print("y is greater than x")
elif x>y:print("x is greater than y")
else:print("x is equal to y") 
"""
""" 
a=15
b=30
print("A") if a<b  else print("B")  
"""
""" 
a=30
b=30
print("A") if a>b else print("B") if a<b else print("A equal to B")   
"""
""" 
x,y=33,100
if y>x:
    pass
"""
""" 
i=0
while i<6:
    print(i)
    i=i+1
 """
""" 
for i in range(6):
    print(i)
 """""" 
for i in range(6):
    print(i ,end=" ") 
"""
""" 
for i in range(1,10):
    if i%2==0:
        break
    print(i ,"odd")
 """
""" 
for i in range(1,10):
    if i%2==0:
        continue
    print(i,"odd")
 """
""" 
for i in range(1,6):
    print(i)
else:
    print("Finally value")
 """
""" 
for i in range(0):
    print("hello, world!")
else:print("goodbye, world!") 
"""
#[print(i) for i in range(10) if i%2==0]
#[print(i) for i in "mohamed"]
""" 
adj=["red","big","testy"]
fruits=["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
 """
""" 
name=input("plz enter your name :")
for i in range(len(name)):
    print(name[-1-i],end=" ")

print()    

"""
""" 
name=input("plz enter your name :")
text=name[::-1]
print(text) 
"""
import datetime
now=datetime.datetime.now()
print(now)