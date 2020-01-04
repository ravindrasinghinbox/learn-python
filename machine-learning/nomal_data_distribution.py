import numpy
import matplotlib.pyplot as plt
'''
Note: A normal distribution graph is also known as the bell curve because of it's characteristic shape of a bell.
    We specify that the mean value is 5.0, and the standard deviation is 1.0.
    Meaning that the values should be consentrated around 5.0, and rarely further away than 1.0 from the mean.
    And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
'''
x = numpy.random.normal(5.0, 5, 100000)

plt.hist(x, 100)
plt.show()