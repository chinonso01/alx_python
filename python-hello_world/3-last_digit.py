#!/usr/bin/python3
import random
number = str(random.randint(-10000, 10000))
lastDigit = int(number[-1:])

if lastDigit > 5:
    result = "and is greater than 5"
elif lastDigit == 0:
    result = "and is 0"
elif lastDigit < 6 and not 0:
    result = "and is less than 6 and not 0"
    
print("Last digit of {} is {} {}".format(number, str(lastDigit), result))
