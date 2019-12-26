# standard diviation https://en.wikipedia.org/wiki/Standard_deviation
import numpy
# standard deviation
# std
# variance
# var
# speed = [1,1,1,1,1]
# x = numpy.std(speed)
# x2 = numpy.mean(speed)
# print("deviation",x)
# print("mean", x2)

# speed = [2,4,4,4,5,5,7,9]
# x = numpy.std(speed)
# x2 = numpy.mean(speed)
# print("deviation",x)
# print("mean",x2)

'''
Let's undersatand standerd diviation
    2,4,4,4,5,5,7,9
    u = (2 + 4 + 4 + 4 + 5 + 5 + 7 + 9)/8 = 5

    First, calcualte the deviation of each data point from the mean, and square then result of each

    (2 - 5)^2 = (-3)^2 = 9
    (4 - 5)^2 = (-1)^2 = 1
    (4 - 5)^2 = (-1)^2 = 1
    (4 - 5)^2 = (-1)^2 = 1
    (5 - 5)^2 = (0)^2 = 0
    (5 - 5)^2 = (0)^2 = 0
    (7 - 5)^2 = (2)^2 = 4
    (9 - 5)^2 = (4)^2 = 16

    the variance is the mean of thesee values
    a^2 = (9 + 1 + 1 + 1 + 0 + 0 + 4 + 16)/8 = 4

    and the population standard deviation is equal to the square root of th varianc
    a = v/2x2 = 2
'''
# speed = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
# std = numpy.std(speed)
# mean = numpy.mean(speed)
# print("deviation",std,"mean",mean)

#variance
speed = [2,4,4,4,5,5,7,9]

x = numpy.var(speed)

print(x)