#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string = "last digit of"
inttostr = str(number)
print(inttostr)
n = int(inttostr[-1])
if number > 0:
    if int(inttostr[-1]) > 5:
        print (string + f"{number:d}" + "is" + f"{n:d}" + "and is greater than 5")
    elif int(inttostr[-1]) == 0:
        print (string + f"{number:d}" + "is" + f"{n:d}" + "and is 0")
    else:
        print (string + f"{number:d}" + "is " + f"{n:d}" + "and is less than 6 and not 0")
elif number == 0:
    print(string + f"{number:d}" + "is" + f"{n:d}" + "and is 0")
else:
    if int(inttostr[-1]) > 5 or int(inttostr[-1]) < 5:
        print (string + f"{number:d}" + "is" + f"-{n:d}" + "and is less than 6 and not 0")
    else:
        print (string + f"{number:d}" + "is" + f"{n:d}" + "and is 0")
