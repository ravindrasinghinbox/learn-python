# # import module
import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#     print("contain")
# else:
#     print("not contain")
# # reg function
# print(re.findall("ai",txt))
# print(re.findall("adi",txt))
# # metacharacters
# # special sequences
# # sets
# # the findall
# # search
# str = "The rain in Spain"
# x = re.search("\s", str)
# print("The first white-space character is located in position: ",x.start())
# # split
# str = "The rain in Spain"
# x = re.split("\s", str)
# print(x)
# str = "The rain in Spain"
# x = re.split("\s", str,1)
# print(x)
# # sub
# str = "The rain in Spain"
# x = re.sub("\s","_",str)
# print(x)
# str = "The rain in Spain"
# x = re.sub("\s","_",str,2)
# print(x)
# # match object
str = "The rain in Spain"
x = re.search("ai", str)
print(x)
print(x.span())
print(x.string)
print(x.group())
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())