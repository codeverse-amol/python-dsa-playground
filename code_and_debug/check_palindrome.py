
n = 1234

num = n



def is_palindrome(num):
    original = num
    result = 0

    while num > 0:
        digit = num % 10
        result = (result * 10) + digit
        num = num // 10

    print(result)

    return original == result

print(is_palindrome(num))



