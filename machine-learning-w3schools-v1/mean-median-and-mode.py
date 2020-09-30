import numpy
from scipy import stats
# mean
# median
# mode
speed = [87, 86, 87, 88, 99, 86, 103, 111, 94, 78, 77, 85, 86]
# mean value or average value
x = numpy.mean(speed)
print(x)
# median middle of value
x = numpy.median(speed)
print(x)
# mode most common
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)