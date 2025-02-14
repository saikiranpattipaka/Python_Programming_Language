# Basics of Python

1. History of Python
Developed by: Guido van Rossum in 1989.
First release: Python 0.9.0 was released in 1991.
Design philosophy: Emphasizes code readability, simplicity, and ease of learning.
Versions:
Python 2.x (1991–2020) – Earlier version, now deprecated.
Python 3.x (2008–present) – Current version, backward incompatible with Python 2.
Popular Usage: Widely used in web development, data science, machine learning, automation, and scientific computing.

2. Character Set
Python supports the Unicode character set, which means it can handle characters from most human languages, including alphabets, symbols, and emojis.

String literals in Python can be defined using:
Single quotes: 'hello'
Double quotes: "hello"
Triple quotes (for multi-line strings):

"""This is a 
multi-line string"""

3. Variables
A variable is a name given to a memory location used to store data.

Declaration: Python does not require explicit declaration of variables (no need to declare type).

x = 10   # integer variable
y = 3.14 # float variable
name = "Alice" # string variable

Dynamic typing: Python is dynamically typed, meaning variables can change types during execution.

x = 10       # x is an integer
x = "hello"  # x is now a string

4. Data Types
Python has various built-in data types:

Numeric types:

int: Integer (whole number).
float: Floating-point number (decimal).
complex: Complex number (x + yj).
Example:

x = 10      # int
y = 3.14    # float
z = 2 + 3j  # complex
Text Type:

str: String (a sequence of characters).
Example:

name = "Python"
Sequence Types:

list: Ordered, mutable collection.
tuple: Ordered, immutable collection.
range: Sequence of numbers.
Example:

numbers = [1, 2, 3]    # list
coordinates = (1, 2)    # tuple
Mapping Type:

dict: Key-value pairs (dictionary).
Example:

person = {"name": "Alice", "age": 25}
Set Types:

set: Unordered collection of unique elements.
frozenset: Immutable version of set.
Example:

unique_numbers = {1, 2, 3}
Boolean Type:

bool: Represents True or False.
Example:

is_valid = True
Binary Types:

bytes, bytearray, memoryview.
5. Strings
String operations:

Concatenation: "Hello" + " " + "World"
Repetition: "Hello" * 3
Slicing: "Hello"[1:4] → "ell"
Methods:

text = "hello"
print(text.upper())      # "HELLO"
print(text.lower())      # "hello"
print(text.find("e"))    # 1 (index of 'e')
print(text.replace("e", "a"))  # "hallo"
Multiline Strings:

multiline = """This is 
a multiline string."""
6. Conditional Statements
Conditional statements allow you to perform different actions based on different conditions.

Syntax:

if condition:
    # Code to run if condition is true
elif another_condition:
    # Code to run if the second condition is true
else:
    # Code to run if none of the above conditions are true
Example:

python
Copy
x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

7. Indexing
Indexing allows you to access individual characters in a string or elements in a sequence (like lists or tuples).

name = "Python"
print(name[0])    # P
print(name[-1])   # n

8. Lists and Tuples
List:

Ordered, mutable collection.
Methods: append(), remove(), insert(), pop(), sort(), etc.
Example:

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adds to the list
Tuple:

Ordered, immutable collection.
Example:

coordinates = (10.0, 20.0)


9. Directory Methods
These are methods related to file and directory manipulation.

os module: Provides methods for directory operations.

import os
os.mkdir("new_folder")     # Create a new directory
os.listdir()               # List files in a directory
os.remove("file.txt")      # Remove a file
os.rmdir("empty_folder")   # Remove an empty directory

10. Sets
A set is an unordered collection of unique elements.
Set Operations:
Union: set1 | set2
Intersection: set1 & set2
Difference: set1 - set2
Symmetric Difference: set1 ^ set2
Example:
python
Copy
numbers = {1, 2, 3, 4}
numbers.add(5)           # Adds 5
numbers.remove(1)        # Removes 1

11. Loops
Loops allow you to execute a block of code multiple times.

For loop:


for i in range(5):
    print(i)
While loop:


i = 0
while i < 5:
    print(i)
    i += 1
Break and Continue:

break: Exits the loop.
continue: Skips the current iteration and continues with the next one.

12. Functions
Functions allow you to group code into reusable blocks.

Defining a Function:


def greet(name):
    return f"Hello, {name}!"
Calling a Function:


print(greet("Alice"))
Arguments and Return Values:

Functions can accept parameters and return values using the return keyword.

13. File Input and Output (I/O)
Python allows reading from and writing to files.

Opening a file:

python
Copy
file = open("example.txt", "w")  # Open file in write mode
file.write("Hello, world!")
file.close()
Reading from a file:


file = open("example.txt", "r")  # Open file in read mode
content = file.read()
print(content)
file.close()
With statement (automatically closes the file):


with open("example.txt", "r") as file:
    content = file.read()
    print(content)

14. Object-Oriented Programming (OOP) Concepts
a. Classes and Objects
Class is a blueprint for creating objects.
Object is an instance of a class.
Example:

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Buddy", 3)
dog1.bark()  # Calling the method

b. Inheritance
Inheritance allows one class to inherit attributes and methods from another class.


class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Output: Woof!

c. Encapsulation
Encapsulation is the concept of restricting access to certain details of an object.

Using private variables (prefix with double underscore):

class Person:
    def __init__(self, name):
        self.__name = name  # private attribute

    def get_name(self):
        return self.__name

d. Polymorphism
Polymorphism allows methods to behave differently based on the object calling them.


class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()

make_sound(cat)  # Meow
make_sound(dog)  # Bark