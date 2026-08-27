# Coding Exercise 43: Reverse a string

# Reverse a string
# Problem Description:

# You are given a string s. Your task is to return the reversed version of the string.

# Input:
# A single string s, where the length of s is between 1 and 1000.

# Output:
# A single string that is the reverse of the input string.

# Example:
# Input: "hello"
# Output: "olleh"
 
# Input: "Python"
# Output: "nohtyP"
# ===========================================================
# Solution:
'''
s = "hello"

def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Your code here

    # str = s[::-1]

    # return str

    # Initialize an empty string to hold the reversed version
    reversed_str = ''
    
    # Loop through the string in reverse order
    for i in range(len(s) - 1, -1, -1):
        # Concatenate each character to the reversed string
        reversed_str += s[i]
    
    # Return the reversed string
    return reversed_str

print(reverse_string(s))
'''
# ===========================================================
# Coding Exercise 44: Count Vowels in a string

# Count Vowels in a string
# Problem Description:
# You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) in the string and return the total count.

# Input:
# A single string s, where the length of s is between 1 and 1000.

# Output:
# An integer representing the total count of vowels in the input string.

# Example:
# Input: "Hello, World!"
# Output: 3
 
# Input: "Python Programming"
# Output: 4

# ===========================================================
# Solution: 
'''
s = "Python Programming"
def count_vowels(s):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    # Your code here
    # Define the set of vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    # Initialize a counter for the vowels
    count = 0
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            count += 1  # Increment the count if it is a vowel
    
    # Return the total count of vowels
    return count

print(count_vowels(s))
'''
# ===========================================================
# Coding Exercise 45: Check for same strings

# Check for same strings
# Problem Description:
# You are given two strings s and t. Your task is to check if the two strings are equal.
# Two strings are considered equal if they have the same length and the same characters at each position. You are not allowed to use any built-in string comparison functions.
# Two strings s and t, where 1 <= len(s), len(t) <= 1000.

# Output:
# A boolean value (True or False) indicating whether the two strings are equal.

# Example:
# Input: s = "hello", t = "hello"
# Output: True
 
# Input: s = "hello", t = "world"
# Output: False
# ===========================================================
# Solution:
'''
s = "hello"
t = "hello"
def are_equal_strings(s, t):
    """
    Function to check if two strings are equal without using built-in functions.
    
    Parameters:
    s (str): The first string.
    t (str): The second string.
    
    Returns:
    bool: True if the strings are equal, False otherwise.
    """
    # Your code here

    # if s == t:
    #     return True

    # else:
    #     return False

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        
        if s[i] != t[i]:
            return False

    return True


print(are_equal_strings(s, t))
'''
# ===========================================================
# Coding Exercise 46: Check Palindrome

# Check Palindrome
# Problem Description:
# You are given a string s. Your task is to check if the string is a palindrome. 
# A string is considered a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.

# Input:
# A single string s, where the length of s is between 1 and 1000.

# Output:
# A boolean value: True if the string is a palindrome, and False otherwise.

# Example:
# Input: "A man a plan a canal Panama"
# Output: True
 
# Input: "Hello, World!"
# Output: False
# ===========================================================
'''
s = "A man a plan a canal Panama"
def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here

    normalized_str = " ".join(ch.lower() for ch in s if s.isalnum())

    return normalized_str == normalized_str[::-1]

    # str = s.lower().replace(" ", "")
    # if str == str[::-1]:
    #     return True

    # else:
    #     return False


print(is_palindrome(s))
'''

# ===========================================================
# Coding Exercise 47: Count words in a string

# Count words in a string
# Problem Description:
# You are given a string s. Your task is to count the number of words in the string and return the total count. A word is defined as a sequence of characters separated by spaces.

# Input:
# A single string s, where the length of s is between 1 and 1000.

# Output:
# An integer representing the total count of words in the input string.

# Example:
# Input: "Hello, World!"
# Output: 2
 
# Input: "Python programming is fun."
# Output: 4
# ===========================================================
'''
s = "Python programming is fun."
def count_words(s):
    """
    Function to count the number of words in the input string.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    # Your code here
    
    count = 0
    
    in_word = False
    
    
    for ch in s:
        
        if ch != " ":

            if not in_word:
                in_word = True
                
                count += 1
        else:
            in_word = False
            
    return count
                   

print(count_words(s))
'''

# ===========================================================
# Coding Exercise 48: Remove Duplicates in a string
# Remove Duplicates in a string
# Problem Description
# You are given a string s. Your task is to remove duplicate characters from the string while preserving the order of the first occurrences and return the modified string.

# Input:
# A single string s, where the length of s is between 1 and 1000.

# Output:
# A string that contains only the first occurrence of each character from the input string.

# Example:
# Input: "programming"
# Output: "progamin"
 
# Input: "Hello, World!"
# Output: "Helo, Wrd!"

# ===========================================================

'''
s = "programming"

def remove_duplicates(s):
    """
    Function to remove duplicate characters from the input string.
    
    Parameters:
    s (str): The input string from which duplicates need to be removed.
    
    Returns:
    str: The modified string with duplicates removed.
    """
    # Your code here
    # seen = set()
    # result = ""

    # for ch in s:
    #     if ch not in seen:
    #         seen.add(ch)
    #         result += ch

    # return result
    result = ''  # Initialize an empty string to store the result
    seen = ''  # Initialize an empty string to track seen characters
    
    # Loop through each character in the input string
    for char in s:
        # Check if the character has not been seen before
        if char not in seen:
            seen += char  # Add the character to seen
            result += char  # Add the character to the result string
    
    return result  # Return the modified string with duplicates removed

print(remove_duplicates(s))
'''
# ===========================================================
# Coding Exercise 49: Count consonants in a string

# Count consonants in a string
# Problem Description:
# You are given a string s. Your task is to count the number of consonants in the string and return the total count. A consonant is any alphabetic character that is not a vowel (a, e, i, o, u).

# Input:
# A single string s, where the length of s is between 1 and 1000.

# Output:
# An integer representing the total count of consonants in the input string.

# Example:
# Input: "Hello, World!"
# Output: 7
 
# Input: "Python Programming"
# Output: 13
# ===========================================================
'''
s = "Python Programming"

def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    vowels = 'aeiouAEIOU'  # Define the set of vowels (both uppercase and lowercase)
    count = 0  # Initialize a counter for consonants
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is a letter (from 'a' to 'z' or 'A' to 'Z')
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            # Check if the character is not a vowel
            if char not in vowels:
                count += 1  # Increment the count if it is a consonant
    
    # Return the total count of consonants
    return count

print(count_consonants(s))
'''
# ===========================================================
# Coding Exercise 50: Check for anagrams
# Check for anagrams
# Problem Description:

# You are given two strings s and t. Your task is to determine if string t is an anagram of string s. 
# An anagram is a word or phrase formed by rearranging the characters of a different word or phrase, using all the original characters exactly once.

# Input:
# Two strings s and t where both lengths are between 1 and 1000.

# Output:
# Return True if t is an anagram of s, and False otherwise.

# Example:
# Input: s = "anagram", t = "nagaram"
# Output: True
 
# Input: s = "rat", t = "car"
# Output: False
# ===========================================================
'''

def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    s1 = s.replace(" ", "").lower()
    t1 = t.replace(" ", "").lower()


    if sorted(s1) == sorted(t1):
        return True

    else:
        return False

'''
# ===========================================================
# Coding Exercise 51: Check Subsequence

# Check Subsequence
# Problem Description:
# You are given two strings s and t. Your task is to determine if string t is a subsequence of string s.
# A subsequence of a string is a new string that is formed from the original string by deleting some (or no) characters without changing the order of the remaining characters.

# Input:
# Two strings s and t where the length of s is between 1 and 1000, and the length of t is between 1 and 1000.

# Output:
# Return True if t is a subsequence of s, and False otherwise.

# Example:

# Input: s = "abcde", t = "ace"
# Output: True
 
# Input: s = "abcde", t = "aec"
# Output: False

# ===========================================================
'''
s = "abcde"
t = "ace"


def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    # Your code here
    
    i = 0

    for char in s:
        if i < len(t) and t[i] == char:
            i += 1

    return i == len(t)    


print(is_subsequence(s, t))
'''
# ===========================================================
# Coding Exercise 52: Check for Substring

# Check for Substring
# Problem Description:
# You are given two strings, s and t. Your task is to determine if the string t is a substring of the string s. 
# A substring is a contiguous sequence of characters within a string. Do not use any built-in functions for string operations and do not use recursion.

# Input:
# Two strings s and t, where 1 <= len(s), len(t) <= 1000.

# Output:
# A boolean value (True or False) indicating whether t is a substring of s.

# Example:
# Input: s = "hello world", t = "world"
# Output: True
 
# Input: s = "hello world", t = "worlds"
# Output: False
# ===========================================================
'''
s = "hello world"
t = "world"

def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    # Your code here
    len_s = 0
    len_t = 0
    
    # Calculate lengths of s and t
    while s[len_s:]:
        len_s += 1
    while t[len_t:]:
        len_t += 1
    
    # If t is longer than s, it cannot be a substring
    if len_t > len_s:
        return False
 
    # Check for substring
    for i in range(len_s - len_t + 1):  # Only check up to len_s - len_t
        j = 0
        while j < len_t and s[i + j] == t[j]:  # Check each character
            j += 1
        if j == len_t:  # If we matched the whole t
            return True
 
    return False  # t is not a substring of s


print(is_substring(s, t))

'''

# ===========================================================
# Coding Exercise 53: Length of the Longest Word

# Length of the Longest Word
# Problem Description:
# You are given a string s. Your task is to find the length of the longest word in the string. 
# A word is defined as a sequence of characters separated by spaces. Do not use any built-in functions for string manipulation.

# Input:
# A string s, where the length of s is between 1 and 1000 characters.

# Output:
# An integer representing the length of the longest word in the string.

# Example:

# Input: s = "The quick brown fox jumps over the lazy dog"
# Output: 5
 
# Input: s = "Hello World"
# Output: 5

# ===========================================================
'''

s = "The quick brown fox jumps over the lazy dog"

def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest word.
    """
    # Your code here

    words = s.split()

    lengths = [len(word) for word in words]

    max = 0

    for i in lengths:
        if i > max:
            max = i


    return max


print(longest_word_length(s))


'''

# ===========================================================