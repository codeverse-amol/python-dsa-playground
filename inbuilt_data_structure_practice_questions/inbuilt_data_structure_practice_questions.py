# ===================================================================================
# Coding Exercise 21: Sum of List Elements
# ===================================================================================

'''
def sum_list(numbers):
    # Your code goes here
    sum = 0
    for i in numbers:
        sum += i

    return sum

print(sum_list([10, -5, 7, 8, -2]))
'''

 # ===================================================================================
# Coding Exercise 22: Largest Element in a List
# ===================================================================================
'''
def find_largest(numbers):
    # Your code goes here
    if not numbers:
        return None

    max = numbers[0]

    for i in numbers:
        if i > max:
            max = i
    return max

print(find_largest([10, -5, 7, 8, -2]))
'''
# ===================================================================================
# Coding Exercise 23: Remove Duplicate in a List
# ===================================================================================
'''
lst = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(lst):
    # Your code goes here
    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
            
    return unique_list

print(remove_duplicates(lst))
'''

# ===================================================================================
# Coding Exercise 24: Check if all elements in a list are Unique
# ===================================================================================
'''
lst = [1, 2, 3, 3, 4, 5]
def check_unique(lst):
    # Your code goes here
    for i in lst:
        if lst.count(i) > 1:
            return False

    else: 
        return True

print(check_unique(lst))
'''
# ===================================================================================
# Coding Exercise 25: Program to Reverse a List
# ===================================================================================
'''
lst = [1, 2, 3, 4, 5]

def reverse_list(lst):
    # Your code goes here
    # lst.sort(reverse=True)    # don't use method directly, use two pointer technique
    start = 0
    end = len(lst) - 1

    while start < end:

        lst[start], lst[end] = lst[end], lst[start]

        start = start + 1
        end = end - 1

    return lst
print(reverse_list(lst))
'''
# ===================================================================================
# Coding Exercise 26: Count Number of Odd and Even Elements in a List
# ===================================================================================
'''
lst = [1, 2, 3, 4, 5]
def count_even_odd(lst):
    # Your code goes here

    even = []
    odd = []

    for num in lst:
        if num % 2 == 0:
            even.append(num)

        else:
            odd.append(num)
    return len(even), len(odd)

# # another way to solve this:
#     # Initialize counters for even and odd numbers
#     even_count = 0
#     odd_count = 0
    
#     # Iterate through each number in the list
#     for num in lst:
#         if num % 2 == 0:  # Check if the number is even
#             even_count += 1
#         else:  # Otherwise, it's odd
#             odd_count += 1
    
#     # Return a tuple containing the counts of even and odd numbers
#     return even_count, odd_count

print(count_even_odd(lst))
'''

    


# ===================================================================================
# Coding Exercise 27: Maximum difference between two consecutive elements in a list.
# ===================================================================================
'''
lst = [10, 11, 15, 3]

def max_consecutive_difference(lst):
    # Your code goes here
    # max = lst[0]
    # min = lst[0]
    
    # for num in lst:
    #     if num > max:
    #         max = num
        
    #     if num < min:
    #         min = num

    # max_diff = max - min
    # return max_diff
    
    maximum_diff = 0

    for i in range(len(lst)-1):
        diff = abs(lst[i] - lst[i+1])

        if diff > maximum_diff:
            maximum_diff = diff

    return maximum_diff

print(max_consecutive_difference(lst))
'''

# ===================================================================================
# Coding Exercise 28: Merge two Sorted List
# ===================================================================================
'''
def merge_two_sorted_lists(list1, list2):
    # Initialize pointers for both lists
    i, j = 0, 0
    result = []  # Initialize an empty list to store the merged result
 
    # Traverse both lists and merge them in sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])  # Add the smaller element to the result list
            i += 1
        else:
            result.append(list2[j])  # Add the smaller element to the result list
            j += 1
 
    # If there are remaining elements in list1, add them to the result
    while i < len(list1):
        result.append(list1[i])
        i += 1
 
    # If there are remaining elements in list2, add them to the result
    while j < len(list2):
        result.append(list2[j])
        j += 1
 
    return result  # Return the merged sorted list


print(merge_two_sorted_lists([1, 3, 5], [2, 4, 6]))
'''

# ===================================================================================
# Coding Exercise 29: Rotate a List

#  Write a Python function to rotate the list to the right by k positions without using slicing. 
#  A rotation shifts elements from the end of the list to the front.
# ===================================================================================
'''
lst = [1, 2, 3, 4, 5]
k = 2

new_lst = []
j = lst[0]
def rotate_list(lst, k):
    # Your code goes here

    for _ in range(k):
        if len(lst) != 0:
            lst.insert(0, lst.pop())
    return lst
print(rotate_list(lst, k))
'''
# ===================================================================================
# Coding Exercise 30: Merge 2 List into Dictionary

# Design a Python function named merge_lists_to_dictionary to merge two lists into a dictionary where elements from the first list act as keys and elements from the second list act as values.

# Parameters:
# keys (List): A list of keys.
# values (List): A list of values.

# Returns:
# A dictionary containing merged key-value pairs.

# Example:

# Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}

# Input: keys = ['x', 'y', 'z'], values = [10, 20, 30]
# Output: {'x': 10, 'y': 20, 'z': 30}


# ===================================================================================
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# def merge_lists_to_dictionary(keys, values):
#     # Your code goes here

#     dict = {}
    
#     for i, j in zip(keys, values):
#         if len(keys) == len(keys):
#             dict[i] = j
#         else:
#             return False
#     return dict

#     # if(len(keys) != len(values)):
#     #     return False
#     # # Create an empty dictionary to store the result
#     # result = {}
 
#     # # Use a loop to iterate through both lists
#     # for i in range(len(keys)):
#     #     # Add each key-value pair to the dictionary
#     #     result[keys[i]] = values[i]
 
#     # return result


# print(merge_lists_to_dictionary(keys, values))
# ===================================================================================
# Coding Exercise 31: Merge Multiple Dictionaries
# ===================================================================================
'''
t = ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    merged_dict  = {**dict1, **dict2, **dict3}

    return merged_dict

print(merge_three_dictionaries(dict1, dict2, dict3))

'''

# ===================================================================================
# Coding Exercise 32: Words Frequency in a Sentence

# Design a Python function named count_word_frequency to count the frequency of words in a sentence and store the counts in a dictionary.

# Parameters:
# sentence (str): The input sentence where you need to count the frequency of each word.

# Returns:
# A dictionary where the keys are words from the sentence and the values are their corresponding frequencies.

# Example:

# Input: "hello world hello"
# Output: {'hello': 2, 'world': 1}

# Input: "the quick brown fox jumps over the lazy dog"
# Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

# ===================================================================================
'''
sentence  ="the quick brown fox jumps over the lazy dog"
def count_word_frequency(sentence):
    # Your code goes here
    list = sentence.split()
    print(list)
    dict = {}
    for key in list:
        if key not in dict:
            count = list.count(key)
            dict[key] = count
    return dict


#  # Initialize an empty dictionary to store word frequencies
#     word_count = {}
    
#     # Split the sentence into words using space as the delimiter
#     words = sentence.split()
    
#     # Iterate through each word in the list of words
#     for word in words:
#         # If the word is already in the dictionary, increment its count
#         if word in word_count:
#             word_count[word] += 1
#         # If the word is not in the dictionary, add it with a count of 1
#         else:
#             word_count[word] = 1
    
#     return word_count


print(count_word_frequency(sentence))
'''
# ===================================================================================
# Coding Exercise 33: Palindromic Tuple

# Check if Tuple is Palindromic
# Design a Python function named is_palindromic_tuple to check if a tuple is palindromic, meaning it reads the same forwards and backwards.

# Parameters:
# tup (tuple): The input tuple that you need to check for palindromic property.

# Returns:
# True if the tuple is palindromic, False otherwise.

# Example:
# Input: (1, 2, 3, 2, 1)
# Output: True

# Input: ('a', 'b', 'c', 'b', 'a')
# Output: True

# Input: (1, 2, 3, 4, 5)
# Output: False

# Input: ('x', 'y', 'z', 'x')
# Output: False

# Input: ('a',)
# Output: True
# ===================================================================================
'''
tup = ('a', 'b', 'c', 'b', 'a', 'l')
def is_palindromic_tuple(tup):
    # Your code goes here

    start = 0
    end = len(tup) - 1

    while start <= end:

        if tup[start] != tup[end]:
            return False

        start = start + 1 

        end = end - 1

        return True

        
print(is_palindromic_tuple(tup))
'''
# ===================================================================================
# Coding Exercise 34: Merge Dictionaries with Common Keys

# Problem Description
# Merge Dictionaries with Overlapping Keys

# Design a Python function named merge_dicts_with_overlapping_keys that merges multiple dictionaries into a single dictionary. If a key appears in more than one dictionary, sum up their values.

# Parameters:
# dicts (list): A list of dictionaries where keys might overlap.

# Returns:
# A single dictionary where values for overlapping keys are summed.

# Example:
# Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
# Output: {'a': 1, 'b': 5, 'c': 9, 'd': 6}

# Input: [{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]
# Output: {'x': 70, 'y': 50, 'z': 90}
# ===================================================================================
'''
dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]


def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here
    merged_dicts = {}

    for d in dicts:

        for key, value in d.items():

            if key in merged_dicts:
                merged_dicts[key] += value

            else:
                merged_dicts[key] = value


        
    return merged_dicts


print(merge_dicts_with_overlapping_keys(dicts))
'''
# ===================================================================================
# Coding Exercise 35: Check if List is Subset of another List

# Check if a List is a Subset of Another List (Brute Force Approach)

# You are given two lists of integers. Write a Python program that checks whether the first list is a subset of the second list using a brute-force approach, without using the in keyword. A list is considered a subset if all elements of the first list are present in the second list.

# Parameters:
# lst1 (List of integers): The first list, which is being checked as a subset.

# lst2 (List of integers): The second list, which is the list to compare against.

# Returns:
# A boolean value True if lst1 is a subset of lst2, otherwise False.

# Example:
# Input: lst1 = [1, 2, 3], lst2 = [1, 2, 3, 4, 5]
# Output: True

# All elements in lst1 are present in lst2.

# Input: lst1 = [1, 6], lst2 = [1, 2, 3, 4, 5]
# Output: False

# The element 6 is not present in lst2.
# ===================================================================================
'''
lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]

def is_subset(lst1, lst2):
    # Your code goes here
    
    # result = all(item in lst2 for item in lst1)

    # return result

    for element in lst1:
        found = False

        for item in lst2:

            if item == element:
                found = True
                
                break

        if not found:
            return False
    return True

print(is_subset(lst1, lst2))
'''