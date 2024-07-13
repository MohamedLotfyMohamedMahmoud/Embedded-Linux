""" 
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(car)
car.clear()
print(car)

 """
""" 
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(car)
car2=car.copy()
print(car2)
 """
""" 
key=['brand','model','year']
defualt_value='unknown'   
car=dict.fromkeys(key,defualt_value)
print(car) 
"""
""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(car)
value=car.get('model')
print(value) """

""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

VALUE=car.items()
print(VALUE) """

""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

VALUE=car.keys()
print(VALUE)  """

""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(car)
VALUE=car.pop('model')
print(VALUE)
print(car) """

""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(car) 
VALUE=car.popitem()
print(VALUE)
print(car)  """

""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
VALUE=car.setdefault('model')
print(VALUE) """
""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
car.update({"model":"mmm","brand":"pp","year":1215})
print(car) """

""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
value=car.values()
print(value) """

""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(car) 
 """

""" car=dict([('brand','ford'),('model','mustang'),('year',1964)])
print(car) 

 """
""" car=dict(brand='ford',
         model='mustang',
         year=1964)
print(car) 
 """


""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
for x,y in car.items():
    print(x,y) """

""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

print("======================================")
for x in car:
    print(x)
print("======================================")
for x in car.keys():
    print(x)
print("======================================")
for x in car:
    print(car[x])
print("======================================")
for x in car.values():
    print(x)
print("======================================")
 """

""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

if "model" in car:
    print("yes, model is one of keys in dictionary")
print("======================================")
print(len(car))
print("======================================")
car["color"]="red"
print(car)
print("======================================")
car["color"]="yellow"
print(car)
print("======================================")

 """
""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print("======================================")
car['color']=[1,2]
print(car)
print("======================================")
car['color']={1,2}
print(car)
print("======================================")
car[1]="vbdf"
car[-1]="wef"
print(car)
print("======================================") """
""" car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

del car["model"]
print(car)
del car
print(car) """

""" my_family={
    "child1":{
        "name":"ali",
        "year":1253
    },
    "child2":{
        "name":"mohmed",
        "year":1536
    }
} 
print(my_family)
"""
""" 
print("========================================")
print(my_family["child1"]["name"])
print(my_family["child1"])
print(dict.keys(my_family))
print("========================================")
print("========================================")
print(my_family["child1"]["name"])
print(my_family["child1"])
print(my_family.keys())
print("========================================") """

""" def function(x):
    x=5
    print("x inside function ",x)
    print("address x inside function ",id(x))

x=10
print("x before function ",x)
print("address x before function ",id(x))

function(5)

print("x after function ",x)
print("address x after function ",id(x))
 """

""" def function(x):
    x[0]=5
    print("x before function",x)
    print("id x before function",id(x))
x=[10]    
print("x inside function",x)
print("id x inside function",id(x))
function(x)
print("x after function",x)
print("id x after function",id(x))
 """
""" import datetime

x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%Y")) """
""" class person:
    def __init__(self,name):
        print("constructor is called")
        print(self)
        print(name)
        self.name=name
        print(name)
    def __del__(self):
        print("Destructor is called")

person("ali") """

""" class person:
    def __init__(self,name):
        print("constructor is called")
        self.name=name
    def greeting(self):
        print("hello")
    def __del__(self):
        print("Destructor is called")
        
Ali = person("ali")
Ali.greeting()
 """


class person:
    """flgmifojgfdlfgpokfg"""
    def __init__(self,name):
        print("constructor is called")
        self.name=name
    def greeting(self):
        """bfhdf"""
        print("hello")
    def __str__(self):
        return("Discription of class person")    
    def __del__(self):
        print("Destructor is called")

print("==========================")
Ali = person("ali")
print("==========================")
Ali.greeting()
print("==========================")
print(Ali)
print("==========================")


