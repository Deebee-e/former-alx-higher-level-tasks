#!/usr/bin/python3
import random
# Generate a random integer between -10 and 10

number = random.randint(-10, 10)
#check if number is > 0
if number > 0:
    output = "{} is positive" .format(number)

elif number == 0:
    output = "{} is zero" .format(number)
else:
    output = "{} is negative" .format(number)
print(output)
