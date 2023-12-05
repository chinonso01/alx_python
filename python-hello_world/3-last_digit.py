#!/usr/bin/python3
import random
number = int(random.randint(-10000, 10000))

if int(number[-1:]) > 5:
    result = "and is greater than 5"
elif int(number[-1:]) == 0:
    result = "and is 0"
elif int(number[-1:]) < 6 and not 0:
    result = "and is less than 6 and not 0"
    
print("Last digit of {} is {} {}".format(number, int(number[-1:]), result))
