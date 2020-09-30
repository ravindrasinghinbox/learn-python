import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 10.0, 100000)

# x = [1,1,3,4,5,6,7,8,9,10]
# histgram reprensent bar chart of frequencies
plt.hist(x,100)
plt.show()