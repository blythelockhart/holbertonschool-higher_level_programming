#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = -1 * (number % 10)
else:
    last_digit = number % 10
message = f'Last digit of {number} is {last_digit} and is'
if last_digit > 5:
    message += ' greater than 5'
elif last_digit == 0:
    message += ' 0'
else:
    message += f' less than 6 and not 0'
print(message)
