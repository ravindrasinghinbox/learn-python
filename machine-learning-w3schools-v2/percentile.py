import numpy

ages = [1,1,1,2,2,2,4,4,6,6]
# ages = [2,2,2,1,1]
# ages = [5,5,5,1,1]

'''
interpolation : {'linear', 'lower', 'higher', 'midpoint', 'nearest'}
        This optional parameter specifies the interpolation method to
        use when the desired percentile lies between two data points
        ``i < j``:

        * 'linear': ``i + (j - i) * fraction``, where ``fraction``
          is the fractional part of the index surrounded by ``i``
          and ``j``.
        * 'lower': ``i``.
        * 'higher': ``j``.
        * 'nearest': ``i`` or ``j``, whichever is nearest.
        * 'midpoint': ``(i + j) / 2``.
'''
x = numpy.percentile(ages, 60,interpolation='nearest')
x = numpy.percentile(ages, 60,interpolation='midpoint')
x = numpy.percentile(ages, 30,interpolation='higher')
# x = numpy.percentile(ages, 30,interpolation='lower')
# x = numpy.percentile(ages, 60)

print(x)