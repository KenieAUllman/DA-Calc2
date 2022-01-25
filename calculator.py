"""CLI application for a prefix-notation calculator."""

from numbers import Number
from operator import truediv
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes )




while True:
    user_input = input("Enter your equation > ")
    tokens = user_input.split(" ")

    if "q" in tokens:
        print("Calculator is quiting")
        break

    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue


    operator = tokens[0]
    num1 = tokens[1] 

    if len(tokens) < 3:
        num2 = "0"

    else:
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    result = None

    if not num1.isdigit() or not num2.isdigit():
        print("Please input numbers")
        continue

   
    elif operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))

    elif operator == "x+":
        result = add_mult(float(num1), float(num2), float(num3))

    elif operator == "cubes+":
        result = add_cubes(float(num1), float(num2))

    else:
        result = "Please enter an operator followed by two integers."

    print(result)

