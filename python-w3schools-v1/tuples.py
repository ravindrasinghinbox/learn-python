tuple_ = ("apple","banana","mango")
# print(tuple_)
# print(tuple_[0])
# print(tuple_[-1])
# # get by range
# print(tuple_[0:1])
# print(tuple_[-3:-1])
# change value
# list_ = list(tuple_)
# list_[0] = "not apple"
# tuple_ = list_
# print(tuple_)
# make loop tuple
# for x in tuple_:
#         print(x)
# # check in in tuple
# if "apple" in tuple_:
#     print("this tuple have fruits tuple")
# # tuple len
# print(len(tuple_))
# # create tuple with one item
# tuple_ = ("ok",)
# tuple_2 = ("not tuple")
# print(type(tuple_))
# print(type(tuple_2))
# # tuple del
# del tuple_
# print(tuple_)
# tuple1 = ("a", "b", "c")
# tuple2 = ("d", "e", "f")
# tuple3 = tuple1 + tuple2
# print(tuple3)
# # check type now
# print(type(tuple3))
tuple_ = tuple(("a", "b", "c"))
print(tuple_)
print(tuple_.index("a"))
print(tuple_.count("a"))