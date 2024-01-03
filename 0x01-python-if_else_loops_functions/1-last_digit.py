#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string="last digit of "
inttosrt=str(number)
n=inttostr[-1]
if n > 5:
    print (string + f"{number:d}" + " " + "is greater than 5")
elif n == 0 :
    print (string + f"{number:d}" + " " + "is 0")
else:
    print (string + f"{number:d}" + " " + "is less than 6 and not 0")
