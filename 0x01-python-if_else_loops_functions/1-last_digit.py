#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string = "last digit of "
inttosrt = str(number)

if int(inttosrt[-1]) > 5:
    print(string + f"{number:d}" + " " + "is greater than 5")
elif int(inttosrt[-1]) == 0:
    print(string + f"{number:d}" + " " + "is 0")
else:
    print(string + f"{number:d}" + " " + "is less than 6 and not 0")
