# # array
# cars = ["Ford", "volvo", "BMW"]
# print(cars)
# # access element of array
# print(cars[0])
# # length
# print(len(cars))
# # looping array
# for x in cars:
#     print(x)
# # adding array element
# cars.append("BMW")
# print(cars)
# # removing array element
# cars.pop(0)
# print(cars)
# # delete element
# cars.remove("BMW")
# print(cars)
# # clear
# cars.clear()
# # copy
# cars = ["Ford", "volvo", "BMW"]
# x = cars.copy()
# count
cars = ["Ford", "volvo", "BMW"]
x = cars.count("BMW")
print(x)
# extends
cars.extend(["ok", "two", "make"])
print(cars)
# insert
cars.insert(0, ["a","b","c"])
print(cars)
# pop
cars.pop(0)
print(cars)
# remove
cars.remove("two")
print(cars)
# reverse
cars = [1, 2, 3, 4, 5]
cars.reverse()
print(cars)
# sort
cars = [1, 3, 5, 6]
cars.sort()
print(cars)