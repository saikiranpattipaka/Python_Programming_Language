# Day 2 Strings & Conditional stmt

#strings

# str1 = "Ram"
# str2 = 'sita' # campus's 
# str3 = """laxman"""

# str1 = "This is string.\nNewline" # Newline
# str2 = "This is string\tTab space" #Tabspace
# print (str2)

# str1 = "Python"
# len1 = len(str1)
# print(len1)

# str2 = "Life"
# len2 = len(str2)
# print(len2)

# final_str = (str1 + " " + str2)
# print(final_str)
# print(len(final_str))

#Indexing
# str = "Apna-nam"
# print(str[0])

# str = "Apna-nam"
# ch = str[0]
# print(ch)

#slicing
# str = "Apna College"
# print(str[ 5: 12])
# print(str[ 5: len(str)])

#Negative indexing
# str = "Apple"
# print(str[-3 : -1])

#String functions
# str = "I am a doctor"

# print (str.endswith("or"))
# print (str.capitalize( )) 
# print (str.replace("doctor", "coder")) 
# print (str.find("am")) 
# print(str.count("t"))

#WAP to input first name & print its length
# name = input("Enter your Name : ")
# print(len(name))

#WAP to find the occurance of S in string
# str = "Hi $ Iam the $ symbol $99.9"
# print(str.find("$"))

# Conditional statement
# light = "Pink"
# if(light=="Red"):
#     print("Stop") # Four spaces/tab space called as Indentation(Proper spacing)
# elif(light=="Green"):
#     print("Go")
# elif(light=="Yellow"):
#     print("Look")
# else:
#     print("Light is broken")

# print("End of Code")

#Grade based on Marks
# marks = int(input("Enter Marks : "))
# if(marks>=90):
#     grade = "A"
# elif(marks >=80 and marks <90):
#     grade = "B"
# elif(marks >=70 and marks <80):
#     grade = "c"
# else:
#     grade = "D"
# print("grade of the students ->", grade)

#Nesting
# age = 70
# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

#WAP to check if a number entered by the user is odd or even
# num = int(input("Enter Number: "))
# if(num%2==0):
#     print("Even")
# else:
#     print("odd")

#WAP to find the greatest of 3 number entered by user
# num1 = int(input("Enter number : " ))
# num2 = int(input("Enter number : " ))
# num3 = int(input("Enter number : " ))
# if(num1>=num2 and num1>=num3):
#     print(num1)
# elif(num2>=num3):
#     print(num2)
# else:
#     print(num3)


#WAP to check if a number is a multiple of 7 or not
# num = int(input("Enter Number: "))
# if(num % 7==0):
#      print("Multiple by 7")
# else:
#      print("Not Multiple by 7")
