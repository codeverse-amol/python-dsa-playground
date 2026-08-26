# Coding Exercise 36: Sum of N Even Natural Numbers

# Sum of N Even Natural Numbers
# Problem Description:
    # You are given an integer n. Your task is to calculate and return the sum of the first n even natural numbers. 
    # The even natural numbers are: 2, 4, 6, 8, ...

# Input:
# A single integer n where 1 <= n <= 10^4.

# Output:
# Return the sum of the first n even natural numbers.

# Example:

# Input: n = 3
# Output: 12  # (2 + 4 + 6)
 
# Input: n = 5
# Output: 30  # (2 + 4 + 6 + 8 + 10)
# ==============================================
# Solution:
'''
def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    total_sum = 0
    for i in range(n+1):
        total_sum += i*2
    
    return total_sum

# or write only without loop
# def sum_of_even_numbers(n):
#     return n * (n + 1)

print(sum_of_even_numbers(3))
'''
# ==============================================
# Coding Exercise 37: Check for Even Number
# Check for Even Number
# Problem Description:
# You are given an integer n. Your task is to check whether the number is even or not. 
# Return True if the number is even, and False otherwise.

# Input:
# A single integer n where -10^9 <= n <= 10^9.

# Output:
# Return True if n is an even number, otherwise return False.

# Example:
# Input: n = 4
# Output: True
 
# Input: n = 7
# Output: False
# ==============================================
# Solution:
'''
def is_even(n):
    """
    Function to check if a number is even.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is even, False otherwise.
    """
    # Your code here
    if n % 2 == 0:
        return True
    else:
        return False
'''
# ==============================================
# Coding Exercise 38: Check for Prime Number
# Check for Prime Number

# Problem Description:
# You are given an integer n. Your task is to check whether the number is prime or not. 
# A prime number is a number greater than 1 that has no divisors other than 1 and itself. 
# Return True if the number is prime, and False otherwise.

# Input:
# A single integer n where 1 <= n <= 10^6.

# Output:
# Return True if n is a prime number, otherwise return False.

# Example:
# Input: n = 5
# Output: True
 
# Input: n = 4
# Output: False

# ==============================================
# Solution:
'''
def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Your code here
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False # only if 0 == 0
    
    return True

print(is_prime(23))
'''
# i = 2  → 23 % 2 = 1
# i = 3  → 23 % 3 = 2
# i = 4  → 23 % 4 = 3
# i = 5  → 23 % 5 = 3
# i = 6  → 23 % 6 = 5
# ...
# i = 22 → 23 % 22 = 1

# None of these divisions give a remainder of 0.

# So the condition:

# if 23 % i == 0:
# never becomes True.

# After the loop finishes, execution reaches:
# return True

# ==============================================
# Coding Exercise 39: Valid Perfect Square
# Valid Perfect Square
# Problem Description:

# You are given a positive integer num. Your task is to check whether num is a perfect square or not. 
# A perfect square is an integer that is the square of an integer (e.g., 1, 4, 9, 16, ...). Return True if num is a perfect square, and False otherwise.

# Input:
# A single positive integer num where 1 <= num <= 10^9.

# Output:
# Return True if num is a perfect square, otherwise return False.

# Example:
# Input: num = 16
# Output: True
 
# Input: num = 14
# Output: False
# ==============================================
'''
def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    # Your code here
    # for i in range(1, num+1):
    #     if i * i == num:
    #         return True
    # return False

    if num < 1:
        return False  # No perfect squares for numbers less than 1
    
    # Initialize a variable to keep track of the current number to check
    i = 1
    
    # Loop until i squared is greater than or equal to num
    while i * i <= num:
        if i * i == num:
            return True  # Found a perfect square
        i += 1  # Increment i to check the next integer
    
    return False  # No perfect square found


print(is_perfect_square(16))
print(is_perfect_square(25))
print(is_perfect_square(0))
print(is_perfect_square(17))
'''
# ==============================================
# Coding Exercise 40: Decimal to Binary
# Decimal to Binary
# Problem Description:
# You are given an integer n. Your task is to return its binary representation as a string. Do not use any built-in functions for conversion.
# Input:
# A single integer n, where -10^9 <= n <= 10^9.

# Output:
# A string representing the binary representation of n.

# Example:
# Input: n = 5
# Output: "101"
 
# Input: n = -5
# Output: "-101"
# ==============================================
# Solution:
'''
def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here

    binary = ""
    if n == 0:
        return "0"  # Special case for zero  
        
    # Handle negative numbers
    is_negative = n < 0
    if is_negative:
        n = -n  # Work with the absolute value
 
    # Convert to binary 
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    # Add the negative sign for negative numbers
    if is_negative:
        binary = "-" + binary
         
    return binary

print(int_to_binary(12))
'''
# ==============================================
# Coding Exercise 41: Binary to Decimal
# Binary to Decimal
# Problem Description:
# You are given a string binary_str representing a binary number. 
# Your task is to convert this binary string to its corresponding decimal integer. Do not use any built-in functions for conversion.

# Input:
# A string binary_str, consisting of characters '0' and '1', where the length of the string is between 1 and 30 (inclusive).

# Output:
# An integer representing the decimal value of the binary string

# Example:
# Input: binary_str = "101"
# Output: 5
 
# Input: binary_str = "1101"
# Output: 13
# ==============================================
# Solution: 
'''
def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    # Without Built-in Functions
    decimal = 0
    power = 0

    for digit in reversed(binary_str):
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal

    # using built-in functions
    # return int(binary_str, 2)

print(binary_to_decimal("1011"))
'''

# ==============================================
# Coding Exercise 42: GCD of Two Numbers
# GCD of Two Numbers
# Problem Description:
# You are given two integers n and m. Your task is to find the GCD of these two numbers. 
# The GCD is the largest positive integer that divides both numbers without leaving a remainder. Do not use any built-in functions and do not use recursion.

# Input:
# Two integers n and m, where 1 <= n, m <= 10^9.

# Output:
# An integer representing the GCD of n and m.

# Example:
# Input: n = 48, m = 18
# Output: 6
 
# Input: n = 56, m = 98
# Output: 14
# ==============================================
# Solution: 
'''
def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    # Your code here

    # Ensure n and m are positive
    n = abs(n)
    m = abs(m)

    while m != 0:
        n, m = m, n % m
    return n

print(gcd(48, 18))
'''
# ==============================================
