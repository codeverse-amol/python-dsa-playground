# Coding Exercise 16: Celsius to Fahrenheit

# def celsius_to_fahrenheit(C):
#     """
#     Function to convert temperature from Celsius to Fahrenheit.
    
#     Parameters:
#     C (float): The temperature in Celsius.
    
#     Returns:
#     float: The temperature in Fahrenheit.
#     """
#     # Your code here
   
#     F = (9/5 * C) + 32
    
    
#     return F
    
# print(celsius_to_fahrenheit(50))
    
    

# Coding Exercise 17: Area of a Rectangle
    
# def area_of_rectangle(length, breadth):
#     """
#     Function to calculate the area of a rectangle.
    
#     Parameters:
#     length (float): The length of the rectangle.
#     breadth (float): The breadth of the rectangle.
    
#     Returns:
#     float: The area of the rectangle.
#     """
#     # Your code here
#     Area=float(length * breadth)
    
#     return Area

# print(area_of_rectangle(5, 3))




# Coding Exercise 18: Distance covered by a Vehicle

# def calculate_distance(speed, time):
#     """
#     Function to calculate the distance traveled by a vehicle.
    
#     Parameters:
#     speed (float): The speed of the vehicle.
#     time (float): The time the vehicle has traveled.
    
#     Returns:
#     float: The distance traveled by the vehicle.
#     """
#     # Your code here

#     distance = speed * time

#     return distance

# print(calculate_distance(50, 10))



# Coding Exercise 19: Number of Rounds of Lift

# import math

# def calculate_lift_rounds(n, capacity):
#     """
#     Function to calculate the number of rounds the lift needs to cover.
    
#     Parameters:
#     n (int): Total number of people.
#     capacity (int): Maximum number of people the lift can carry in one round.
    
#     Returns:
#     int: The number of rounds required to transport all people to the top floor.
#     """
#     # Your code here
    
    
#     trips = math.ceil(n / capacity)

#     return trips

# print(calculate_lift_rounds(10, 4))




# Coding Exercise 20: Line Equation    

# def calculate_y(slope, intercept, x):
#     """
#     Function to calculate the value of y using the slope-intercept form of a line.
    
#     Parameters:
#     slope (float): The slope of the line.
#     intercept (float): The y-intercept of the line.
#     x (float): The value of x for which y needs to be calculated.
    
#     Returns:
#     float: The calculated value of y.
#     """
#     # Your code here
#     y = slope * x + intercept
    
#     return y
    
# print(calculate_y(2, 3, 4))