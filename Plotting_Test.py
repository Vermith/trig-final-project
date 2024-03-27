# Final Project COP1500
# Trignomtric Function Plotter
import numpy
from matplotlib import pyplot as pt
import time
import math as m
#
# vars
# amplitude = a, period = b, phaseshift = c, vertical shift = d

a = 1
b = 1
c = 0
d = 0


# test plotting
x = numpy.arange(0,b,periodCalculator(b,c))
y = a * numpy.cos(x)

# windows
pt.plot(x, y, color='red')
pt.show()