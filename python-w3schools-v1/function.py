# # deinfe function
# def myfunction():
#     print("this is myfunction")
# # calling function
# def myfunction():
#     print("this is myfunction")
# myfunction()
# # parameter

# def myfunction(a):
#     print("this is myfunction",a)
# myfunction("ok here")
# # default parameter
# def myfunction(a = "make is easy"):
#     print("this is myfunction",a)
# myfunction()
# # passing a list as parameter
# def myfunction(foods):
#     for x in foods:
#         print(x)
# myfunction(["apple","make","easy","life"])
# # return values
# def sum(a,b):
#     return a + b
# print(sum(1,2))
# # keyword argument
# def sum(a,b):
#     return a + b
# print(sum(a=1,b=2))
# arbitrary arguments
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")
# # pass statement
# def myfunction():
#     pass
# # recursion
def sumof(num):
    if (num == 0):
        return 0
    return num+sumof(num-1)
print(sumof(5))