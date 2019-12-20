# # create set
# _set = {"a", "b", "c"}
# print(_set)
# # add
# _set.add("d")
# print(_set)
# # update
# _set.update("e")
# print(_set)
# # multiple update
# _set.update(["f", "g"])
# print(_set)
# # loop
# for x in _set:
#     print(x)

# # len
# print(len(_set))
# # item remove
# _set.remove("a")
# print(_set)
# # discard
# _set.discard("a")
# # clear
# _set.clear()
# print(_set)
# del
# _set = {"a", "b", "c"}
# # join
# _set1 = {1, 2, 3}
# _set2 = {4, 5, 6}
# _set = _set1.union(_set2)
# print(_set)
# # pop
# print(_set.pop(),_set)
# # set consturctor
# _set = set(("a", "c", "d"))
# print(_set)
# copy
_set = {1, 2, 3}
print(_set.copy())
# difference
_set1 = {1, 2, 3}
_set2 = {3, 4, 5}
print(_set1.difference(_set2))


# union
_set1 = {1, 2, 3}
_set2 = {3, 4, 5}
print(_set.union(_set2))

# difference update
_set1 = {1,3,2}
_set2 = {3, 4}
_set1.difference_update(_set2)
print(_set1)

# isdisjoint update
_set1 = {3,4}
_set2 = {3, 4}
x =_set1.isdisjoint(_set2)
print(x)
x = {"apple", "banana", "cherry"}
y = {"apple"}

z = x.isdisjoint(y) 

print(z)