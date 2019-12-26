import matplotlib.pyplot as plt
import numpy
from scipy import stats

# # car
# x = [1, 2, 3, 4, 5,6]
# # speed
# y = [5,4,3,2,1,0]

# slope, intercept, r, p, std_err = stats.linregress(x, y)
# print(stats.linregress(x, y))
# # slope = -1
# # intercept = 7
# def myfunc(x):
#     print("x=",x,"cal=",slope * x + intercept,"arg slope,intercept",slope,intercept)
#     return slope * x + intercept

# mymodel = list(map(myfunc, x))
# plt.scatter(x, y)
# plt.plot(x,mymodel)
# plt.show()

# R-squared
# The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
# print(r)

# predict future
# x = [1,2,3,4]
# y = [5,4,3,2]
# slope, intercept, r, p, std_err = stats.linregress(x, y)
# print('slope',slope, 'intercept',intercept, 'r',r, 'p',p, 'std_err',std_err)
# def myfunc(x):
#   return slope * x + intercept

# speed = myfunc(5)

# print('Car speed: ',speed)

# data with less relationship
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept
print(slope, intercept, r, p, std_err)
mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
# ---------------------------------home work-----------------------------------------
# from tuple
# def g():
#     return (1, 2, 3)
# a, b, c = g()

# # from dictionary
# def g():
#     return {'a':1, 'b':2, 'c':3}
# c = g()
# print(c['a'])

# class ReturnValue:
#     __slots__ = ["y0","y1","y2"]
#     def __init__(self, y0, y1, y2):
#         self.y0 = y0
#         self.y1 = y1
#         self.y2 = y2
# def g():
#     return ReturnValue(1,2,3)
# print(g())

# # named tuple
# import collections
# Point = collections.namedtuple('m', ['x', 'y'])
# p = Point(11, y=22)
# a, b = p
# print(a,b,p)