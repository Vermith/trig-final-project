# Final Project COP1500
# Trignomtric Function Plotter
import numpy as np
from matplotlib import pyplot as pt
import math as m
import os
import random

# file saving
output_directory = './trigplots'

#creating output_directory
if not os.path.exists(output_directory):
    os.mkdir(output_directory)
else:
    print('Folder already exists!')

# psudeo random name generator

randgint = random.randint(0,1000)
name = "plot" + str(randgint) + ".png"

# functions

def periodCalc(b):
    solve = (2 * m.pi)/b
    return float(solve)

def phaseShift(b,c):
    solve = (2 * m.pi) / b
    solve2 = c // solve
    return solve2

def periodCalculator(b,c):
    solve = (2 * m.pi) / b
    solve2 = c // solve
    solve3 = (solve + solve2)/4
    return float(solve3)


while True:

    choice = input("specify the function to continue.."
                   "lowercase letters only")
    print("Enter 'quit' to exit the program")

    if choice == "quit":
        exit()

    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    d = float(input("Enter the value of d: "))

    # conditonal statements
    if a < 1:
        print("invalid input, amplitude needs to be greater than 1")
        quit()
    if b == 0:
        print("invalid input, period needs to be greater than zero")
        quit()
    if c > b:
        print("invalid input, phase shift needs to be greater then b")
        quit()
    if c == b:
        print("invalid input, phase shift needs to be greater then b")
        quit()


    if choice == "cos":
        a = a + d
        x = np.arange(0, b * 4, periodCalculator(b, c))
        y = a * np.cos(x)

    if choice == "sin":
        a = a + d
        x = np.arange(0,b * 4,periodCalculator(b,c))
        y = a * np.sin(x)

    if choice == "tan":
        a = a + d
        x = np.arange(0,b * 4,periodCalculator(b,c))
        y = a * np.tan(x)


    # printer for variables
    if choice != "quit":
        print("Amplitude: " + str(a))
        print("Period: "+ str(periodCalc(b)))
        print("Phase Shift: " + str(phaseShift(b,c)))
        print("Vertical Shift: " + str(d))

    # windows

    pt.ylim(-a ,a)
    pt.plot(x, y, color='blue', linewidth=2)

    # saves plot to folder
    pt.savefig(os.path.join(output_directory, name))
    pt.show()

