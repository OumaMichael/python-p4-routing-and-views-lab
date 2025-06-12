#!/usr/bin/env python3

from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define route for the home page
@app.route('/')
def index():
    # Return a simple HTML heading
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Define route that prints and returns a string parameter
@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print the parameter to the console
    return param  # Return the parameter as response

# Define route that counts from 0 up to (but not including) the given integer
@app.route('/count/<int:param>')
def count(param):
    numbers = ""
    for i in range(param):
        numbers += f"{i}\n"  # Append each number followed by a newline
    return numbers  # Return the numbers as a string

# Define route that performs a math operation on two integers
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2  # Addition
    elif operation == '-':
        result = num1 - num2  # Subtraction
    elif operation == '*':
        result = num1 * num2  # Multiplication
    elif operation == 'div':
        if num2 == 0:
            return "Cannot divide by zero"  # Handle division by zero
        result = num1 / num2  # Division
    elif operation == '%':
        result = num1 % num2  # Modulo
    else:
        return "Invalid operation"  # Handle invalid operation

    return str(result)  # Return the result as a string

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)
