# check int type varialble type
# x = 5
# print(type(x))

# python data type
# strVar = "hello str"
# intVar = 5
# floatVar = 5.5
# complexVar = 1 j
# listVar = ["apple", "banana", "cherray"]
# tupleVar = ("a", "b", "c")
# rangeVar = range(6)
# dictVar = {"name": "john", "age": 36}
# setVar = {"apple", "worked", "many"}
# frozensetVar = frozenset({"apple", "banan", "cherray"})
# boolVar = True
# bytesVar = b"hello"
# byteArrayVar = bytearray(5)
# memoryviewVar = memoryview(bytes(5))

# print(strVar,intVar,floatVar,complexVar,listVar,tupleVar,rangeVar,dictVar,setVar,frozensetVar,boolVar,bytesVar,byteArrayVar,memoryviewVar)

# create specific data type with function
x = str("hello world")
print('str', x)
x = int(20)
print('int', x)
x = float(1.23)
print('float', x)
x = list(("apple", "banana", "cherry"))
print(x)
x = tuple(("apple", "banana", "cherry"))
print('tuple', x)
x=range(6)
print('range', x)
x=dict(name="john", age=36)
print('dict', x)
x=set(("apple", "banana", "cherry"))
print('set', x)
x=frozenset(("apple", "banana", "cherry"))
print('frozenset', x)
x=bool(5)
print('bool', x)
x=bytes(5)
print('bytes', x)
x=bytearray(5)
print('bytearay', x)
x=memoryview(bytes(5))
print('memoryview',x)