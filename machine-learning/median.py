import numpy

# speed = [99,86,87,88,111,86,12,103,87,94,78,77,85,86]

# # median will take mid value of ordered set if there is odd number in set will average of two mid value
# # 77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103 
# # (86 + 87) / 2 = 86.5

# x = numpy.median(speed,keepdims = True,overwrite_input=True)

# print(x)

a = numpy.array([[10,  7,  4],
           [ 3,  2,  1]])
b = a.copy()
# keepdims - return value in dimension wise
# overwrite_input - replace input array in sorted form
x = numpy.median(b, axis=1, keepdims=True)
print(x)