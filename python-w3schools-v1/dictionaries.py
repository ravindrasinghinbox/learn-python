# # create and print dicrtionay
# dic = {
#     "name": "Ravindra singh",
#     "age": 30,
#     "birth":1989
# }
# print(dic)
# # access item
# print(dic["name"])
# # access item with get method
# print(dic.get("name"))
# # change value
# dic["name"] = "make it easy"
# print(dic)
# # loop dictionaris and print key
# for x in dic:
#     print(x)
# # loop dictionary and print value
# for x in dic:
#     print(dic[x])
# # print values in loop
# for x in dic.values():
#     print(x)
# # loop through key value with items
# for x, y in dic.items():
#     print(x,y)
# # check if key exist
# if "name" in dic:
#     print("yes it have keyword")
# # len
# print(len(dic))
# # add item
# dic["country"] = "India"
# print(dic)
# # remove item
# del dic["country"]
# print(dic)
# # pop key
# print(dic.pop("name"))
# print(dic)
# # pop item
# print(dic.popitem())
# print(dic)
# # del key
# del dic
# print(dic)
# del dictionaries
# del dic
# print(dic)
# clear
dic = {"a": "first letter", "b": "second letter"}
dic.clear()
print(dic)
# copy

dic = {"a": "first letter", "b": "second letter"}
xdic = dic.copy()
print(xdic)
# dict
dic = dict({"a": "first", "b": "second"})
print(dic)
# group dictionaries
dic1 = {"a":"1"}
dic2 = {"b": "2"}
dic = {
    "first": dic1,
    "second":dic2
}
print(dic)
print(dic["first"]["a"])
# dict constructor
dic = dict(name="ok", model="ok", year="1989")
print(dic)
# setdefault
dic = dict(name="ok", model="ok", year="1989")
x = dic.setdefault("x","fine")
print(x)


