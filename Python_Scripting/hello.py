# print("Hello from hello.py!")
# print(1)

# print("D:\\SAI\\Programs\\Python Practice\\Python_Scripting")

# a=10.5
# print(a)
# print(type(a))


# x=10 # Re-declare variable
# print("First x value is:",x)
# x=20
# print("Second x value is:",x)
# del x
# print(x)

# x=5
# print(id (x)) # Variable Memory Address or Loacation


# x=3 # x=3;y=4.2;z=3+6j
# y=4.2
# z=3+6j #print(x,y,z)
# print(x,type(x))
# print(y,type(y))
# print(z,type(z))

# Iam_Name="Sai" # String Variable
# print(Iam_Name)
# print(type(Iam_Name))

# s = "Hello, Python!" # String Operations
# print(s.lower())      # 'hello, python!'
# print(s.upper())      # 'HELLO, PYTHON!'
# print(s[0])           # 'H'
# print(s[7:13])        # 'Python'
# print(len(s))         # 14

# first = "Hello"  # String Concatenation and Formatting
# second = "World"
# print(first + " " + second)  # 'Hello World'


# name = "Alice" # f-string formatting
# print(f"Hi, {name}!")        # 'Hi, Alice!'

# value=True
# print(type(value)) # Boolean Variable


# x=56
# print(x,type(x))
# y=str(x)  # Convert integer to string
# print(y,type(y))
# z=float(x) # Convert integer to float
# print(z,type(z))


# x=4 #Print with variables and Strings
# y=5.6
# z=3+6j
# lang_name="Python Scripting" #print(x,y,z,lang_name)
# print("{} {} {} {}".format(x,y,z,lang_name))  # Using format method
# print("{3} {2} {1} {0}".format(x, y, z, lang_name))  # Using format method with indices
# print(f"{x} {y} {z} {lang_name}")  # Using f-string formatting


# a=eval(input("Enter a value:"))  # prefer to use eval rather int or float
# b=eval(input("Enter another value:"))
# result= a + b
# print(result)

# a=int(input("Enter an integer: "))
# b=int(input("Enter another integer: "))
# result = a + b
# print(f"The sum of {a} and {b} is: {result}")


# Role="""
# I am a Python script that provides a simple interface for practicing Python scripting concepts.
# I can help you understand basic data types, variable assignments, and type conversions.
# """
# print(Role)


# My_Str="Python Scripting"
# print(My_Str[0:3])
# print(My_Str[7: ])
# print(My_Str[ :6])
# print(My_Str[::2]) # start : stop : step
# print(len(My_Str))

# a="Hello"
# b="World"
# c= a + " " + b
# print(c)

# my_var = "Python Scripting" # Boolean operations
# print(my_var.startswith("p"))
# print(my_var.islower( ))
# print(my_var.isupper( ))
# print(my_var.istitle( ))
# print(my_var.isspace( ))
# print(my_var.isalpha( ))
# print(my_var.isnumeric( ))


# x="python"  # Join,center and zfill string operation
# y="-".join(x)
# print(y) # p-y-t-h-o-n

# z="python"
# print(z.center(20))
# print(f"{z.center(20)}")

# z="python"
# print(z.zfill(10)) # 0000python


# x="Hello, World!"
# print(x.strip())  # Remove leading and trailing whitespace
# print(x.strip('H')) # Only starting or ending character (lstrip rstrip)
# print(x.rstrip('d!').strip('d').lstrip('H'))

# x="Python is Dynamic Language"
# print(x.split())
# print(x.split('is'))


# x="Python is Dynamic Language"
# print(x.count('a')) # Count occurrences of 'a'
# print(x.index('D')) # Find index of 'D'
# print(x.index('a', 10)) # Find index of 'a' starting from index 10))
# print(x.find('a', 20)) # Find index of 'a', returns -1 if not found

# import os
# t_w=os.get_terminal_size().columns
# a=input("Enter the string: ") # Practice
# print(a.rjust(t_w)) # Mode gives the string length in windows; tput cols in linux
# print(a.ljust(t_w))
# print(a.center(t_w).title())


# Data Structures of python

# List
# my_list=[3,5,4.5,"Python",True,3+6j]
# print(my_list)
# print(my_list[5])  # Accessing elements
# print(my_list[3][1]) # Accessing single character in string element
# print(my_list[0:3]) 


# my_list=[3,5,4.5,"Python",True,3+6j]
# my_list[0]=6.7  # Modifying an element
# print(my_list)

# my_list=[3,5,7,5,11]
# print(my_list.index(5))  # Finding index of an element
# print(my_list.index(5, 2))  # Finding index of an element starting from index 2

# print(my_list.count(5))  # Counting occurrences of an element)

# print(my_list)
# my_list.clear()  # Clearing the list
# print(my_list)  # Empty list
# .copy()  # Copying the list

# my_list=[3,5,4.5,"Python",True,3+6j]
# my_list.append("New Element")  # Adding an element to the end
# print(my_list)
# my_list.insert(2, "New Element")  # Inserting an element at a specific index
# print(my_list)

# my_list.extend([8, 9, 10])  # Extending the list with another list
# print(my_list)  # Printing the modified list

# my_list.remove(5)  # Removing an element
# print(my_list)

# my_list.pop()  # Removing the last element
# print(my_list)
# my_list.pop(2)  # Removing an element at a specific index
# print(my_list)

# my_list.reverse()  # Reversing the list
# print(my_list)

# my_list=[8,7,6,4,2]
# my_list.sort()  # Sorting the list
# print(my_list) 


# Tuple
# my_tuple=(3,5,4.5,"Python",True,3+6j)
# print(my_tuple)
# my_tuple=(3,5,4.5,"Python",[2,4,6,8],True,3+6j)
# print(my_tuple)
# print(my_tuple[5])  # Accessing elements
# print(my_tuple[3][1]) # Accessing single character in string element
# print(my_tuple[0:3])  # Slicing the tuple

# x=(4,5,2,5,2,8,7)
# print(x.count(5))  # Counting occurrences of an element
# print(x.index(5))  # Finding index of an element
# print(x.index(5, 2))  # Finding index of an element starting from index
# print(len(x)) # Length of the tuple
# print(type(x)) # Type of the tuple



# Dictionary
# my_dict={"fruit":"Apple", "vegetable":"Carrot", "number":42, "is_valid":True}
# print(my_dict)
# print(my_dict["fruit"])  # Accessing value by key
# print(my_dict.get("vegetable"))  # Accessing value using get method
# my_dict.clear()  # Clearing the dictionary
# print(my_dict)  # Empty dictionary
# print(my_dict.keys())  # Getting all keys
# print(my_dict.values())  # Getting all values
# print(my_dict.items())  # Getting all key-value pairs

# my_dict["new_key"]="New Value"  # Adding a new key-value pair
# print(my_dict)

# my_new_dict={"name":"Alice", "age":30, "city":"New York"}
# my_dict.update(my_new_dict)  # Merging two dictionaries
# print(my_dict)

# my_dict.pop("number")  # Removing a key-value pair
# print(my_dict)

# my_dict.popitem()  # Removing the last inserted key-value pair
# print(my_dict)

# keys=["a","e","i","o","u"]
# new_dic=dict.fromkeys(keys)  # Creating a dictionary from a list of keys
# print(new_dic) # {'a': None, 'e': None, 'i': None, 'o': None, 'u': None}

# my_dict={}
# my_dict.setdefault("new_key", "default_value")  # Setting a default value for a key
# print(my_dict)



# Set
# my_set={9,4,5,9.2,1,"python",True,3+6j}
# print(my_set)  # Printing the set
# print(type(my_set))  # Type of the set


# Operators in Python
# Arithmetic Opeartors
# x=10
# y=3
# result1=x+y # Addition
# result2=x-y # Subtraction
# result3=x*y # Multiplication
# result4=x/y # Division
# result5=x//y # Floor Division
# result6=x%y # Modulus
# result7=x**y # Exponentiation
# print(f'Addition: {result1}',f'Subtraction: {result2}',f'Multiplication: {result3}',
#       f'Division: {result4}', f'Floor Division: {result5}',f'Modulus: {result6}', f'Exponentiation: {result7}')

# Assignment Opeartors
# a=eval(input("Enter a value: "))
# b=eval(input("Enter another value: "))
# result=a+b
# print(f"The Addition of {a} & {b} is: {result}")


# Comparision Operators
# x = 5 > 4
# print(x, type(x))

# print(ord('a')) # Find ASIC Code
# print(chr(97)) # Find Character from ASIC Code


# Identity Operators
# is & is not


# Membership Operators
# x=[4,6,8]
# print(4 in x) # True
# print(4 not in x) # False


# Logical Operators
# x=5
# y=10
# if x > 0 and y > 0:
#     print("Both x and y are positive.")

# x=-5
# y=10
# if x < 0 or y > 0:
#     print("Either x or y is positive.")

# logged_in=False
# if not logged_in:
#     print("Please log in.")

# age = 20 # Combined 
# has_id = True
# is_banned = False

# if age >= 18 and has_id and not is_banned:
#     print("Access granted")
# else:
#     print("Access denied")


# Bitwise Operators
# 5 in binary 0101
# 3 in Binary 0011
# a=5
# b=3
# print(a & b) # AND  0001 => 1
# print(a | b) # OR 0111 => 7
# print(a ^ b) # XOR 0110 => 6
# print(~a) # NOT 1010  => -6
# print(a << 2) # Left Shift 10100 => 20
# print(a >> 2) # Right Shift 000101 => 1


# Conditional Statements

# x=10
# if x > 5: #if
#     print("x is greater than 5")

# x=3
# if x > 5: # if else
#     print("x is greater than 5")
# else:
#     print("x is not greater than 5")

# x=5
# if x > 5: # if elif else
#     print("x is greater than 5")
# elif x==5:
#     print("x is equal to 5")
# else:
#     print("x is not greater than 5")


# Module
# import module
# print(module.my_value)

# import math
# print(math.sqrt(25))
# print(math.pi)

# import math # Method 1
# print(math.pi)
# print(math.pow(2, 3))

# import math as m # Method 2
# print(m.pi)
# print(m.pow(2, 3))

# from math import * # Method 3
# print(pi)
# print(pow(2, 3))

# from math import pi, pow # Method 4
# print(pi)
# print(pow(2, 3))


# import platform # platfrom Module
# print(platform.system()) # https://docs.python.org/3.13/library/platform.html
# print(platform.processor())
# print(platform.machine())
# print(platform.python_version())
# print(platform.python_version_tuple())
# print(platform.uname())

# import getpass # getpass Module
# password=getpass.getpass("Enter your password: ")
# print("Entered", password)

# import getpass # getuser Module
# current_user=getpass.getuser()
# print("Current User:", {current_user})

# import sys
# help(sys)
# print(sys.path)
# print(sys.version)
# print(sys.modules)
# print(sys.argv)
# print(sys.exit())

# import os # os Module
# print(os.sep)
# print(os.getcwd()) # current working directory
# print(os.chdir("D:\\SAI\\Programs")) # change directory)
# print(os.getcwd())
# print(os.listdir()) # list directory
# print(os.listdir("D:\\SAI\\Programs")) # list directory)
# print(os.mkdir("Test")) # create directory)
# print(os.rmdir("Test")) # Deleting directory
# print(os.getpid()) # Process ID
# print(os.system("pwd"))

# path="D:\\SAI\\Programs\\My_Resume_Website"
# print(list(os.walk(path))) # Walk through directory

# import datetime
# print(datetime.datetime.now()) # Date & Time
# print(datetime.datetime.today())
# https://strftime.org/ # Format




# fruits=["Apple","Banana","Cherry","Date","Elderberry"] # Loops
# for fruit in fruits:
#     print(fruit)

# for i in range(5):
#     print(i)

# i=1
# while i <= 5:
#     print(i)
#     i+=1

# for i in range(10): # Stops the loop immediately
#     if i == 5:
#         break
#     print(i)

# for  i in range(5): # Skips the current iteration and goes to the next one
#     if i == 2:
#         continue
#     print(i)

# for i in range(3):
#     print(i)
# else:
#     print("Loop completed successfully")

# for i in range(2): # Nested Loops - Loops inside loop
#     for j in range(3):
#         print(f"i={i}, j={j}")

    

# my_list=[3,4,5,6,8,9] # Loops Pratice
# for val in my_list:
#     rem=val % 2
#     if rem==0:
#         print(f"{val} is even")
#     else:
#         print(f"{val} is odd")

# a=input("Enter a value: ") # Loops  Practice
# for index, character in enumerate(a):
#     print(f"Index: {index}, Character: {character}")


# print(list(range(0,100,10))) # Range with step
# print(list(range(100,0,-10)))

# cnt=1 # While loop
# while cnt <=5:
#     print("Hello")
#     cnt=cnt+1

# for val in [1,2,3,4,5,]: # Break
#     print(val)
#     if val==3:
#         break


# for val in range(0,10): # continue
#     if val==2:
#         continue
#     print(val)


# import subprocess # Practice java version
# cmd=["java","--version"]
# sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
# rc=sp.wait()
# o,e=sp.communicate()
# if rc==0:
#     for each_line in o.splitlines():
#         if each_line.startswith("java"):
#             version=each_line.split()[1]
#             print(version)
#             break
# else:
#    print("command failed")


# f=open("Test.txt",'r') # File Handling
# content=f.read() # read() readline() readlines()
# print(content)
# f.close()

# f=open("Test.txt",'w')
# f.write("Hello World")
# f.close()

# lines=["line 1\n","line 2\n"]
# f=open("Test.txt", 'w')
# f.writelines(lines)
# f.close()


# import os # Deleting file
# os.remove("Test.txt")

# try: # Exception Handling
#     x=10/0
# except ZeroDivisionError:
#     print("Can't divide by zero!")

# try: # try,except,else
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input.")
# else:
#     print(f"Result is {result}")

# try: # finally
#     file = open("example.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("File not found.")
# else:
#     print(content)
# finally:
#     print("Closing the file.")
#     try:
#         file.close()
#     except:
#         pass

# try:
#     x = 10 / 0
# except Exception as e: # Don't know which error you are handling about
#     print(f"An error occurred: {e}")



# def greet(): # Function
#     print("Hello, World!")
# greet()

# def greet(name): # Function with Parameters
#     print(f"Hello, {name}!")
# greet("Saikiran")

# def add(a, b): # Function with Return Value
#     return a+b
# result=add(5,3)
# print(result)



# import re  # RegEx
# text="This is easy to learn"
# pattern="easy"
# print(re.findall(pattern,text))

# import re 
# text="it is easy to learn"
# pattern="i[st]"
# print(re.findall(pattern,text))

# import re 
# text="it is easy to learn"
# pattern="[st]"
# print(re.findall(pattern,text))

# import re 
# text="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# pattern="[a-zA-Z0-9]"
# print(re.findall(pattern,text))

# import re 
# text="it is easy to learn two"
# pattern="\w"            # \w\w for two words in seq 
# print(re.findall(pattern,text)) # Refer RegEx Tables

# import re 
# text="it is easy to learn aaa"
# pattern="a{3}"
# print(re.findall(pattern,text))



# import paramiko # paramiko Nodule SSH to Remote Server
# ssh = paramiko.SSHClient() # Create SSH client instance
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Automatically add host keys (not recommended for production)
# ssh.connect(hostname='example.com', username='user', password='your_password') # Connect to the server
# stdin, stdout, stderr = ssh.exec_command('ls -l /home/user') # Run a command
# print(stdout.read().decode()) # Print the output
# print(stderr.read().decode())
# ssh.close() # Close the connection

# import paramiko  # SFTP File Transfer with Paramiko
# transport = paramiko.Transport(('your.server.com', 22))
# transport.connect(username='your_username', password='your_password')
# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.put('local_file.txt', '/remote/path/remote_file.txt')  # Upload
# sftp.get('/remote/path/remote_file.txt', 'local_file.txt')  # Download
# sftp.close()
# transport.close()



# import shutil # shutil Module
# shutil.copy('source.txt', 'destination.txt')



# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def display_info(self):
#         print(f"Car: {self.year} {self.make} {self.model}")        

# my_car = Car("Toyota", "Camry", 2022)

# my_car.display_info()
