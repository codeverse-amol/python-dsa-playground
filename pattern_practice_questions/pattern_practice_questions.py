# Coding Exercise 1: Square of side 'N'

# def generate_square(n):
#     """
#     Function to return a square pattern of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The size of the square.
    
#     Returns:
#     list: A list of strings where each string represents a row of the square.
#     """
#     # Your code here
#     squares = []
#     for i in range(n):
#         list = "*" * n
        
#         squares.append(list)
#     print(squares)


# generate_square(5)

# ======================================================================================


# Coding Exercise 2: Hollow Square of side 'N'

# def generate_hollow_square(n):
#     """
#     Function to return a hollow square pattern of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The size of the square.
    
#     Returns:
#     list: A list of strings where each string represents a row of the hollow square.
#     """
#     # Your code here
#     squares = []
#     for i in range(1,n+1):

#         if i == 1 or i == n:
#             list = "*" * n
            
#         else:
#             list = '*' + (n-2)*" " + '*'
            
        
#         squares.append(list)
            
#     return squares


# print(generate_hollow_square(5))

# ======================================================================================




# Coding Exercise 3: Rectangle Pattern

# def generate_rectangle(n, m):
#     """
#     Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
#     Parameters:
#     n (int): The number of rows in the rectangle.
#     m (int): The number of columns in the rectangle.
    
#     Returns:
#     list: A list of strings where each string represents a row of the rectangle pattern.
#     """
#     # Your code here
    
#     rectangle = []
    
#     for i in range(n):
        
#         list = "*" * m
        
#         rectangle.append(list)
        
#     return rectangle

# print(generate_rectangle(3, 5))
# ======================================================================================

# Coding Exercise 4: Right Angled Triangle


# def generate_triangle(n):
#     """
#     Function to return a right-angled triangle of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The height and base of the triangle.
    
#     Returns:
#     list: A list of strings where each string represents a row of the triangle.
#     """
#     # Your code here
    
    
#     r_triangle = []
    
#     for i in range(1, n):
        
#         list = "*" * i
        
#         r_triangle.append(list)
        
        
#     return r_triangle

# print(generate_triangle(5))
# ======================================================================================




# Coding Exercise 5: Inverted Right Angled Triangle

# def generate_inverted_triangle(n):
#     """
#     Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The height and base of the triangle.
    
#     Returns:
#     list: A list of strings where each string represents a row of the triangle.
#     """
#     # Your code here

#     inverted_triangle = []
    
#     for i in range(1, n+1):
        
#         list = "*" * i 
        
        
#         inverted_triangle.append(list)
#     inverted_triangle.reverse()
        
#     return inverted_triangle


# print(generate_inverted_triangle(5))

# ======================================================================================

# Coding Exercise 6: Pyramid Pattern

# def generate_pyramid(n):
#     """
#     Function to return a pyramid pattern of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The number of rows in the pyramid.
    
#     Returns:
#     list: A list of strings where each string represents a row of the pyramid.
#     """
#     # Your code here


#     pyramid = []
    
#     for i in range(1,n+1):
        
#         row = " "*(n - i) + "*"*(2 * i - 1) + " "*(n - i) 
#         print(row)
#         pyramid.append(row)
        
        
#     return pyramid


# print(generate_pyramid(5))

# ======================================================================================


# Coding Exercise 7: Inverted Pyramid Pattern


# def generate_inverted_pyramid(n):
#     """
#     Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The number of rows in the inverted pyramid.
    
#     Returns:
#     list: A list of strings where each string represents a row of the inverted pyramid.
#     """
#     # Your code here


#     inverted_pyramid = []
    
#     for i in range(n, 0, -1):
        
#         row = " "*(n - i) + "*"*(2 * i - 1) + " "*(n - i) 
#         print(row)
#         inverted_pyramid.append(row)
        
        
#     return inverted_pyramid

# print(generate_inverted_pyramid(5))

# ======================================================================================

# Coding Exercise 8: Right Angled Triangle with Numbers

# def generate_number_triangle(n):
#     """
#     Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
#     Parameters:
#     n (int): The height of the triangle.
    
#     Returns:
#     list: A list of strings where each string represents a row of the triangle.
#     """
#     # Your code here
#     number_triangle = []
    
#     for i in range(1, n):
        
#         row = i * str(i)
#         print(row)
#         number_triangle.append(row)
        
        
#     return number_triangle


# print(generate_number_triangle(5))

# ======================================================================================
# Coding Exercise 9: Floyds Triangle

# def generate_floyds_triangle(n):
#     """
#     Function to return the first n rows of Floyd's Triangle as a list of strings.
    
#     Parameters:
#     n (int): The number of rows in the triangle.
    
#     Returns:
#     list: A list of strings where each string represents a row of Floyd's Triangle.
#     """
#     # Your code here
#     floyds_triangle = []
#     num = 1 

#     for i in range(1, n+1):

#         row = []
        
#         for j in range(i):
#             row.append(str(num))
#             num = num + 1
#         print(row)
#         floyds_triangle.append(" ".join(row))
       
        

#     return floyds_triangle


# print(generate_floyds_triangle(5))




# ======================================================================================
# Coding Exercise 10: Diamond Pattern

# def generate_diamond(n):
#     """
#     Function to return a diamond pattern of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The number of rows for the upper part of the diamond.
    
#     Returns:
#     list: A list of strings where each string represents a row of the diamond.
#     """
#     # Your code here
#     diamond = []
#     for i in range(1, n):     
#         row = " "*(n - i) + "*"*(2 * i - 1) + " "*(n - i) 
#         print(row)
#         diamond.append(row)


#     for i in range(n, 0, -1):     
#         row = " "*(n - i) + "*"*(2 * i - 1) + " "*(n - i) 
#         print(row)
#         diamond.append(row)

#     return diamond

# print(generate_diamond(5))

# ======================================================================================
# Coding Exercise 11: Right Angled Triangle II

# def generate_right_angled_triangle(n):
#     """
#     Function to return a right-angled triangle of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The height of the triangle.
    
#     Returns:
#     list: A list of strings where each string represents a row of the triangle.
#     """
#     # Your code here

#     right_angled_triangle = []
    
#     for i in range(1, n+1):
#         row = (n-i) * " " + i * "*"
#         right_angled_triangle.append(row)

#     return right_angled_triangle

# print(generate_right_angled_triangle(5))

# ======================================================================================
# Coding Exercise 12: Sandglass Pattern

# def generate_sandglass(n):
#     """
#     Function to return a sandglass pattern of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The height of the sandglass.
    
#     Returns:
#     list: A list of strings where each string represents a row of the sandglass pattern.
#     """
#     # Your code here

#     sandglass = []
#     for i in range(n, 0, -1):     
#         row = " "*(n - i) + "*"*(2 * i - 1) + " "*(n - i) 
#         print(row)
#         sandglass.append(row)

#     for i in range(2, n+1):     
#         row = " "*(n - i) + "*"*(2 * i - 1) + " "*(n - i) 
#         print(row)
#         sandglass.append(row)
#     return sandglass

# print(generate_sandglass(3))
# ======================================================================================
# Coding Exercise 13: Hollow Right Triangle
# def generate_hollow_right_angled_triangle(n):
#     """
#     Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The height of the triangle.
    
#     Returns:
#     list: A list of strings where each string represents a row of the triangle.
#     """
#     # Your code here
#     list = []
#     for i in range(1, n+1):
#         if i == 1 or i == 2 or i == n:
#             row = i * "*"
#             list.append(row)

#         else:
#             row = "*" + " "*(i-2) + "*"
#             list.append(row)
#         print(row)
#     return list


# print(generate_hollow_right_angled_triangle(15))
# ======================================================================================
# Coding Exercise 14: Hollow Inverted Right Triangle

# def generate_hollow_inverted_right_angled_triangle(n):
#     """
#     Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The height of the triangle.
    
#     Returns:
#     list: A list of strings where each string represents a row of the triangle.
#     """
#     # Your code here
#     # Your code here
#     list = []
#     for i in range(n, 0, -1):
#         if i == 1 or i == 2 or i == n:
#             row = i * "*"
#             list.append(row)

#         else:
#             row = "*" + " "*(i-2) + "*"
#             list.append(row)
#         print(row)
#     return list

# print(generate_hollow_inverted_right_angled_triangle(10))

# ======================================================================================
# Coding Exercise 15: Number Pyramid Pattern


# def generate_number_pyramid(n):
#     """
#     Function to return a pyramid pattern of numbers of height n as a list of strings.
    
#     Parameters:
#     n (int): The height of the pyramid.
    
#     Returns:
#     list: A list of strings where each string represents a row of the pyramid pattern.
#     """
#     # Your code here

#     pyramid = []

#     for i in range(1, n+1):

#         spaces = " " * (n - i)
#         nums = " ".join(str(x) for x in range(1, i+1))

#         pyramid.append(spaces + nums + spaces)
        

#     return pyramid

# print(generate_number_pyramid(3))


# ======================================================================================