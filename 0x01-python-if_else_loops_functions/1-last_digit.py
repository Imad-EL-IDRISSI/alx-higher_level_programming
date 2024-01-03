#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string = "last digit of "
inttosrt = str(number)
n = int(inttosrt[-1])

if int(inttosrt[-1]) > 5:
    print (string + f"{number:d}" + " " + "is " + f"{n:d} " + "and is greater than 5")
elif int(inttosrt[-1]) == 0 :
    print (string + f"{number:d}" + " " + "is " + f"{n:d} " + "and is 0")
else:
    print (string + f"{number:d}" + " " + "is " + f"{n:d} " + "and is less than 6 and not 0")
