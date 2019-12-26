import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score


#  time of day
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
# speed of car
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# x = [1,5,10,15]
# y = [1,5,10,15]

# # here last parameter in polyfit will be used to how many dot will be use 
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# # print('mymodel',numpy.polyfit(x, y, 2))
# # number of sample will be used between 1,22 of 50
# myline = numpy.linspace(1, 22, 100)
# plt.scatter(x, y)
# plt.plot(myline,mymodel(myline))
# plt.grid()
# plt.show()

# R-squared
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# print(r2_score(y,mymodel(x)))

# x = [1, 2, 3, 4,  5,  6,  7,  8,    9,  10]
# y = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# # Predict future values
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# time = 12
# speed = mymodel(time)
# print("Car speed at ",time,":00 ",speed,'with value',r2_score(y,mymodel(x)))


# bad input

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
time = 12
plt.scatter(x, y)
myline = numpy.linspace(1, 22, 100)
plt.plot(myline,mymodel(myline))
plt.grid()
plt.show()
speed = mymodel(time)
print("bad r value",r2_score(y,mymodel(x)))