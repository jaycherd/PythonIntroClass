# Getting Started with Python

# Printing to the console
print("Hello, Python!")

# Variables and basic data types
number = 42                 # An integer assignment
pi_value = 3.14159          # A floating-point
name = "Alice"              # A string

print(number, pi_value, name)

# Lists: Ordered, mutable (you can change it), and allows duplicate elements
my_list = [1, 2, 3, 4, 5]
my_list.append(6)           # Adding an element to the end of the list
print(my_list)

# Tuples: Ordered, immutable (you can NOT change it), allows duplicates
my_tuple = (1, 2, 3)
print(my_tuple)

# Dictionaries: Key-value pairs, unordered, mutable
my_dict = {'name': 'Bob', 'age': 25}
print(my_dict)
my_dict['age'] = 26         # Changing an element
print(my_dict)

# Conditional Statements
if number > 50:
    print("Number is greater than 50")
elif number == 42:
    print("Number is 42")
else:
    print("Number is less than 50")

# Loops
# For loop
for i in range(5):          # Range from 0 to 4
    print(i)

# While loop
count = 5
while count > 0:
    print(count)
    count -= 1

# Functions
def add_numbers(a, b):
    return a + b

# Using the function
result = add_numbers(10, 15)
print("Result of add_numbers:", result)

# Reading from a file (make sure a file named 'test.txt' exists)
try:
    with open('test.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

# Writing to a file
with open('output.txt', 'w') as file:
    file.write("Hello from Python!")

# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object of the class Person
person = Person("John", 30)
print(person.greet())

# Example of importing modules
import math
print("The cosine of pi is:", math.cos(math.pi))
