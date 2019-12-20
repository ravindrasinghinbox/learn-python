# create class
class MyClass:
    x = 5
# create object
obj = MyClass()
print(obj.x)
# __init__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFun(this):
        print("make is easy " + this.name)
p1 = Person("jhon", 36)
p1.name = "Maker"
print(p1.myFun())
# object method
# self parameter
# delete object properties
# delete object
del p1.name
# pass statement
class Person:
    pass