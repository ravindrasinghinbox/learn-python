import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5, 1, 100)
plt.subplot(121)
plt.hist(x, 10)
plt.subplot(122)
plt.hist(numpy.random.normal(5, 2, 100), 10)
plt.show()