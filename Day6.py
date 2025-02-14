#Functions & Recursion
#function defination

# def calc_sum(a, b): #parametes
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(5,10) # function call; arguments

# calc_sum(10, 20)

# calc_sum(3, 9)



#average of 3 numbers

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# calc_avg(1,2,3)

#WAP to print the lenght of a list.(list is the parameter)
# cities = ["delhi", "gurgaon", "noida", "pune", "mumbai","chennai"]
# heroes = ["thor", "ironman", "captain america","shaktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

#WAP to print the elemnents of a list in a single line (list is the parameter)
# heroes = ["thor", "ironman", "captain america","shaktiman"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)
# print( )

#WAP to find the factorial of n (n is the parameter)

# n = 5

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(6)

#WAP to convert USD to INR

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =" , inr_val, "INR")

# converter(73)


#Recursion
#recursive function
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

#recursion n!
# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(4))

#WAP recursive function to calculate the sum of first n natural number
# def cal_sum(n):
#     if (n == 0):
#         return 0
#     return cal_sum(n-1) + n

# sum = cal_sum(5)
# print(sum)


#Write a recursive function to print all elemnets in a list
#hint: use list & index as parameters
# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["mango", "lichi", "apple","banana"]

# print_list(fruits)
