def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")



# Example of a basic function
def greet():
    print("Hello, welcome to learning Python functions!")

# Calling the function
greet()

# Function with parameters
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Calling the function with arguments
sum_result = add_numbers(5, 10)
print("Sum of 5 and 10 is:", sum_result)

# Function with default parameters
def introduce(name, age=25):
    print(f"My name is {name} and I am {age} years old.")

# Calling the function with one argument (age will take the default value)
introduce("Alice")

# Calling the function with both arguments
introduce("Bob", 30)

# Function with multiple return values
def calculate(num1, num2):
    sum_value = num1 + num2
    difference = num1 - num2
    return sum_value, difference

# Unpacking multiple return values
sum_value, difference = calculate(20, 10)
print("Sum:", sum_value)
print("Difference:", difference)

# Recursive Function Example (Factorial Calculation)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Calling the recursive function
number = 5
print(f"Factorial of {number} is:", factorial(number))
