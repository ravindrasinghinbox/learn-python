import matplotlib.pyplot as plt
from scipy import stats

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,81,86,82,87,94,78,77,85,86]
'''
Linear regression uses the relationship between the data-points to draw a straight line through all them.
This line can be used to predict future values.

In the example below, the x-axis represents age, and the y-axis represents speed. We have registered the age and speed of 13 cars as they were passing a tollbooth. Let us see if the data we collected could be used in a linear regression:

R-Squared
It is important to know how well the relationship between the values of the x-axis and the values of the y-axis is, if there are no relationship the linear regression can not be used to predict anything.

The relationship is measured with a value called the r-squared.

The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

Python and the Scipy module will computed this value for you, all you have to do is feed it with the x and y values:
'''
x = [1,2,3,4,5]
y = [10,20,30,40,50]

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [2,4,8,16,32,64,128,256,512,1024]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(slope, intercept, r, p, std_err)
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)

speed = myfunc(6)
print(speed)

plt.show()