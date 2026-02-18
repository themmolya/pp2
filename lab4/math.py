# Math and Random Practice

import math
import random

# Built-in functions
nums = [5, 2, 9, 1]
print("Min:", min(nums))
print("Max:", max(nums))
print("Abs:", abs(-10))
print("Round:", round(3.14159, 2))
print("Power:", pow(2, 3))

# math module
print("Sqrt:", math.sqrt(16))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.7))
print("Sin:", math.sin(math.pi / 2))
print("Cos:", math.cos(0))
print("Pi:", math.pi)
print("Euler's number:", math.e)

# random module
print("Random float:", random.random())
print("Random int:", random.randint(1, 10))
print("Random choice:", random.choice(nums))

random.shuffle(nums)
print("Shuffled list:", nums)
