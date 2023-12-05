#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = int(str(number)[-1:])

if number < 0:
    lastDigit = int(str(number)[0:-1])
    if lastDigit < 6 and not 0:
        result = "and is less than 6 and not 0"
else:
    if lastDigit > 5:
        result = "and is greater than 5"
    elif lastDigit == 0:
        result = "and is 0"
    
print("Last digit of {} is {} {}".format(number, lastDigit, result))
