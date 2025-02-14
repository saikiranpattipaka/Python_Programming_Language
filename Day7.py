#File Input & Output

# f = open("file.txt","r")  #files in same location we can give file name, if file is in different location we need to add path
# data = f.read( ) #"C:\Users\saiki\Downloads\acknowledgementSlip_S1891424330000.pdf"
# print(data)
# print(type(data))
# f.close( )

# f = open("file.txt","r")
# data = f.read(5)  # will read only 5 characters
# print(data)

# f.close( )



# f = open("file.txt","r")

# line1 = f.readline()   #reads one line at a time
# print(line1)

# line2 = f.readline()  #reads one line at a time
# print(line2)

# f.close( )


#Write mode
# f = open("file.txt","w") # w will override #a append the data or adds the data to the existing one

# f.write("I want to learn Javascript tomorrow. 123")

# f.close( )



# f = open("file.txt","a") # w will override #a append the data or adds the data to the existing one

# f.write("\nAfter that nodeJS ")

# f.close( )


#With syntax
# with open("file.txt", "r") as f: #using as has alias no need to close the file
#     data = f.read() #read
#     print(data)



# with open("file.txt", "w") as f: 
#     f.write("Writing new data") #write
    

#Deleting a file
# import os 

# os.remove("deletefile.txt")

#Create a new file "practice.txt" using python. Add the following data in it
# hi everyone \n we are learning File I/O \n using Java \n I like programming in python

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in java")


#WAF that replace all occurrences of "java" with "python" in above file
# with open("practice.txt","r") as f:
#     data = f.read( )

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)


#search if the word "learning" exists in the file or not.
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read( )
#     if(data.find(word) != -1):
#         print("FOUND")
#     else:
#         print("NOT FOUND")

#WAF to find in which line of the file does the word "learning" occurs first
#print -1 if word not found

# def check_for_line( ):
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line( )

#From a file containing numbers separated by comma, print the count of even numbers
# 1, 2, 45, 55, 86, 76
# count = 0
# with open("practice.txt", "r") as f:
#     data = f.read( )

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1

# print(count)