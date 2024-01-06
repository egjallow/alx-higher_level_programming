#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digt = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if last_digt > 5:
    print("Last digit of {} is {} is greater than 5".format(number, last_digt))
elif last_digt == 0:
    print("Last digit of {} is 0".format(number, last_digt))
else:
    print("Last digit of {} is {} is less than 6 and not 0".format(number, last_digt))
