def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")

def calculate_area_of_circle(radius):
    import math
    return math.pi * (radius ** 2)

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_bmi(weight, height):
    if height > 0:
        return weight / (height ** 2)
    else:
        raise ValueError("Height must be greater than zero.")