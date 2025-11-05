import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, integrate, limit, sympify, oo
from sympy.utilities.lambdify import lambdify
import math
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re

# Create our mathematical variable x
x = symbols('x')

# Print a welcome message
print("welcome brother")

while True:

    print("Find a derivative")
    print("find a integral")
    print("integrate")
    print("graph")
    print("trig calculator")
    print("basic math")

    choice = input("1, 2, 3, 4, 5, 6, 7: ")

    if choice == '1':
        question = input("Enter problem to find the derivative of: ")
       
        if '=' in question:
            question = question.split('=')[1].strip()
        
        # Convert math notation to Python notation
        question = question.replace('^', '**')
        question = question.replace(' ', '')  # Remove spaces
        
        question = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', question)
        
        math_expression = sympify(question)
        derivative_result = diff(math_expression, x)
        print("the derivative is:", derivative_result)

    
    elif choice == '2':
        print("do you want in indefinte or definite: ")
        definite_or_indefinte = input("definite or indefinte: ")
        if definite_or_indefinte == 'indefinte':
            question_integral = input("Enter the problem you would like to integrate: ")
            math_expression_integral = sympify(question_integral)
            
            integral_result = integrate(math_expression_integral, x)
            print("The integral is:", integral_result)

        elif definite_or_indefinte == 'definite':
            question_integral_definite = input("Enter the definite integral you would like to integrate: ")
            math_expression_integral_definite = sympify(question_integral_definite)
            lower = float(input("Enter lower limit: "))
            upper = float(input("Enter upper limit: "))
    
            integral_result_definite = integrate(math_expression_integral_definite, (x, lower, upper))
            print("the integral is:", integral_result_definite)

    elif choice == '3':
        limit_function = input("enter the function for the limit: ")
        math_expression_limits = sympify(limit_function)
        limit_asker = input("what value is x approaching: ")
        limit_result = limit(math_expression_limits, x, limit_asker)
        print("the limit is:", limit_result)

    
    elif choice == '4':
        func_input = input("Enter function to graph: ")
        func = sympify(func_input)
        
        f = lambdify(x, func, 'numpy')
        
        # Create x values
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)
        
        # Create the plot
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, 'b-', linewidth=2)
        plt.grid(True)
        plt.title(f"Graph of {func}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.show()

    elif choice == '5':
        print("1. degress to radians")
        print("2. radians to degrees")
        print("3. solve right angle triangle ")
        
        trig_choice = input("choose 1-3: ")

        if trig_choice == '1':
            degrees = float(input("enter degrees: "))
            radians = degrees * (3.14159/ 180)
            print(f"{degrees}° = {radians:.4f} radians")

        elif trig_choice == '2':
            radians = float(input("enter radians: "))
            degrees = radians * (180 / math.pi)
            print(f"{radians} radians = {degrees:.4f}°")

        elif trig_choice == '3':
            print("Right triangle solver - finding hypotenuse")
            adjacent = float(input("Enter adjacent side: "))
            opposite = float(input("Enter opposite side: "))
            hypotenuse = math.sqrt(adjacent**2 + opposite**2)
            print(f"Hypotenuse = {hypotenuse:.4f}")


       elif choice == '6':
        print("Basic Math Calculator")
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /, **, sqrt): ")
        
        if operation == '+':
            num2 = float(input("Enter second number: "))
            result = num1 + num2
        elif operation == '-':
            num2 = float(input("Enter second number: "))
            result = num1 - num2
        elif operation == '*':
            num2 = float(input("Enter second number: "))
            result = num1 * num2
        elif operation == '/':
            num2 = float(input("Enter second number: "))
            result = num1 / num2
        elif operation == '**':
            num2 = float(input("Enter power: "))
            result = num1 ** num2
        elif operation == 'sqrt':
            result = math.sqrt(num1)
        else:
            result = "Invalid operation"
        
        print(f"Result: {result}")


        