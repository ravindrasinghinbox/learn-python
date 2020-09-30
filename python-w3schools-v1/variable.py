# print x and y
# x = 5
# y = "this is my fav num"
# print(x)
# print(y)

# change variable after declare
# x = 5
# x = "My name is this and i changed value"
# print(x)

# it's same sas
# x = 'Hello'
# x = "Hello"
# print(x)

# it's same sas
# x = 'x'
# X = "X"
# print(x, X)

#assing value to multiple variable
# x, y, z = "orrange", "banana", "cherry"
# print(x, y, z)

#you can assign same value to multiple variable
# x = y = z = "alphabet"
# print(x,y,z)

# text with variable
# x = "awesome"
# print("This is output", x)

#concate variable and print
# x = "hello"
# y = "world"
# print(x + y)

# use + for number
# x = 5
# y = 6
# print(x + y)

# get error with number and string
# x = "hello"
# y = 5
# print(x+y)

# global variable example
# x = "awesome"
# def myFun():
#     print('Global variable print: ',x)
# myFun()

# global and local variable example
# x = "make it easy"
# def makeIt():
#     x = "value changed in function"
#     print('print value from function: ', x)
# makeIt()
# print('Print global as well: ',x)

# declare global varialble inside function
# def myFun():
#     global x
#     x = "this is global"
#     print(x)
# myFun()
# print('Print global variable',x)

# change global variabble inside function
x = "global value"
def fun():
    global x
    x= "i changed value"
    print(x)
fun()
print("let's print global vaue",x)