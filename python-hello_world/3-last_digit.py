#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = str(number)[-1:]

if number < 0:
    lastDigit = str(number)[0] + str(number)[-1]
    if int(lastDigit) < 6 and not 0:
        result = "and is less than 6 and not 0"
else:
    if int(lastDigit) > 5:
        result = "and is greater than 5"
    elif int(lastDigit) == 0:
        result = "and is 0"
    
print("Last digit of {} is {} {}".format(number, lastDigit, result))
