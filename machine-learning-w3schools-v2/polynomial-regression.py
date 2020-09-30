# import matplotlib.pyplot as plt

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# plt.scatter(x, y)
# plt.show()

# import numpy
# import matplotlib.pyplot as plt

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# # mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# # print(type(mymodel))
# # myline = numpy.linspace(1, 22, 100)

# # plt.scatter(x, y)
# # plt.plot(myline, mymodel(myline))
# # plt.show()
# '''
# The polynomial’s coefficients, in decreasing powers, or if the value of the second parameter is True, the polynomial’s roots (values where the polynomial evaluates to 0). For example, poly1d([1, 2, 3]) returns an object that represents x^2 + 2x + 3, whereas poly1d([1, 2, 3], True) returns one that represents (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x -6.
# '''
# p = numpy.poly1d([1,2,3],True)
# # https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html
# x = numpy.polyfit(x, y, 3)
# print(x)

# import numpy
# from sklearn.metrics import r2_score

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# speed = mymodel(17)
# print(speed)