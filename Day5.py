# Loops

# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# while True :
#     print("Hello") # prints infinite times True=True

# count = 1
# while count <= 5 :
#     print("Hello",count)
#     count += 1
# print(count)

# i = 1
# while i <= 5 :
#     print(i)
#     i += 1
# print("Loop ended")

# i = 5
# while i >= 1 :
#     print(i)
#     i -= 1
# print("Loop ended")

#WAP to print 1 to 100
# i = 1
# while i <=100 :
#     print(i)
#     i +=1
# print("End of program")

#WAP to print 100 to 1
# i = 100
# while i >=1 :
#     print(i)
#     i -=1
# print("End of program")

#print multiplication table
# n = int(input("Enter the number: "))
# i = 1
# while i <= 10 :
#     print(n*i)
#     i +=1

#print the elements of the following list using a loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # heros = ["thor", "Ironman", "superman"]
# idx = 0
# while idx < len(nums):
#    print(nums[idx])
#    idx +=1

#search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,64,81,100)

# nums = (1,4,9,16,25,36,49,64,64,81,100)
# x = 36
# i = 0 #initialization
# while i < len(nums):
#     if(nums[i]==x):
#         print("FOUND at idx",i)
#     i += 1


#Break & continue
# i = 1
# while i <= 5:
#     print(i)
#     if(i==3):
#         break
#     i += 1

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 64, 81, 100, 36)

# x = 36

# i = 0 #initialization
# while i < len(nums):
#      if(nums[i]==x):
#          print("FOUND at idx",i)
#          break
#      else:
#          print("finding..")
#      i += 1
# print("end of loop")


# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue #skip
#     print(i)
#     i +=1

# nums = [1, 2, 3, 4, 5]

# for val in nums:
#     print(val)

# tup = (1, 2, 3, 4, 5, 6) #tuples

# for num in tup:
#     print(num)

# str = "appnacollege" #string

# for char in str:
#     print(char)

# str = "appnacollege" #string

# for char in str:
#     print(char)
# else:
#     print("END")

#WAP print the elements of the following list using a loop
# [1,4,5,16,25,36,49,64,81,100] using for 
 
# nums = [1, 4, 5, 16, 25, 36, 49, 64, 81, 100]

# for el in nums:
#     print(el)

#WAP to search for a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = 49

# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#         break
#     idx += 1

#Range

# seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])

# seq = range(10)
# for i in seq:
#     print(i)




# for i in range(10):
#     print(i)

# for i in range(10): #range (stop)
#     print(i)

# for i in range(2, 10): # range(start, stop)
#     print(i)

# for i in range(2, 10, 2): # range(start, stop, step)
#     print(i)

# for i in range(2,100,2): #Even numbers
#     print(i)

#WAP using for & range( ) 
#prime numbers 1 to 100

# for i in range(1, 101): #prime numbers
#     print(i)

# 100 to 1
# for i in range(100,0, -1): #100 to 1
#     print(i)

#multiplication table n
# n = int(input("enter number :" ))

# for i in range(1, 11):
#     print(n*i)

# pass statement
# for i in range(5):
#     pass
# print("some future work")



# WAP to find the sum of first n numbers (using while)

# n = 5
# sum = 0
# for i in range(1, n+1):
#     sum += i
    
# print("Total sum =", sum)

# n = 7
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print("Total sum =", sum)



#WAP to find the factorial of first n numbers.(using for) 5 factorial 1*2*3*4*5
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1

# print("Factorial =", fact)
