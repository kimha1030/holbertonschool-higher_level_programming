#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s1 = "Last digit of"
s2 = "is"
s3 = "and is greater than 5"
s4 = "and is less than 6 and not 0"
s5 = "and is 0"
if (number < 0):
    number = -number
    last = (number % 10) * (-1)
    print("{} {} {} {} {}".format(s1, -number, s2, last, s4))
else:
    last = number % 10
    if (last > 5):
        print("{} {} {} {} {}".format(s1, number, s2, last, s3))
    elif ((last < 6) and (not(last == 0))):
        print("{} {} {} {} {}".format(s1, number, s2, last, s4))
    else:
        print("{} {} {} {} {}".format(s1, number, s2, last, s5))
