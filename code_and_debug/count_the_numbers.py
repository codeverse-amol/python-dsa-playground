# Count the Number of Digits in an Integer

n = 5438

num = n

def count_number(num):

    count = 0

    while num > 0:

        count += 1

        num = num//10

    return count

print(count_number(num))

# TC = O(log10(N))
# SC = O(1)



# count using log

from math import *

def count_digits(num):

    return int(log10(num) + 1)

print(count_digits(num))

