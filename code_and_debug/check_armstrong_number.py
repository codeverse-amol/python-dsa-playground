# Python program to check if the number is an Armstrong number or not
# An Armstrong number of order n is an integer such that the sum of its digits raised to the power n is equal to the number itself.

n = 153

num = n

total = 0

while num > 0:

    nod = len(str(n))

    ld = num % 10

    total = total + (ld ** nod)

    num = num // 10


# display the result

if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")


# TC = O(log10(N))
# SC = O(1)