import numpy
import matplotlib.pyplot as plt

# # generate big data
# x = numpy.random.uniform(0.0, 5.0, 25)
# print(x)

# # histogram
# x = numpy.random.uniform(0.0, 50.0, 250)

# plt.hist(x, 5)
# plt.grid()
# plt.show()

# big data distributions
# x = numpy.random.uniform(0, 5, 10)
x = [1,1,1,1,1,2,3,3,3,3,4,4,4]

plt.subplot(121)
plt.hist(x, 10)
plt.subplot(122)
plt.hist(x, 3)
plt.grid(True,c='c',animated=True)
plt.show()