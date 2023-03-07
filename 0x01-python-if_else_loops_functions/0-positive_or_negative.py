#!/usr/bin/python3
import random
digit = random.randint(-10, 10)
if digit > 0:
    print("{} is positive".format(digit))
elif digit == 0:
    print("{} is zero".format(digit))
else:
    print("{} is negative".format(digit))
