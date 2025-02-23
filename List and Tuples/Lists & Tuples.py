#Lists & Tuples

# marks1 = 94.5
# marks2 = 64.2
# marks3 = 69.1
# marks4 = 91.0
# marks5 = 35.3

# marks = [94.5, 64.2, 69.1, 91.0, 35.3]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[1])

#list slicing
# marks = [94.5, 64.2, 69.1, 91.0, 35.3]
# print(marks[1:4])
# print(marks[:3])
# print(marks[1:])
# print(marks[-3:-1]) #Negative indexing

#List method
#list = [2, 1, 3, 6, 5, 8] #list = ["banana", "Apple", "Orange"]
#print(list.append(4))
#print(list.sort( )) # Assending order
#print(list.sort(reverse=True )) # Descending order
#list.reverse( )
#list = [2, 1, 3, 1]
#list.insert(1,5)
#list.pop(1)
#print(list)

#Tuple
# tup = (1,2,3,4,) #close the number with ,
# print(tup)
# print(type(tup))
# print(tup[1:3])

# tup = (1,2,3,4,2)
# print(tup.index(2)) 
# print(tup.count(2)) #No of times 2 repeated

#WAP enter names of 3 movie names & store them in a list
# list = []
# list1 = input("Enter the movie name") #list.append(input("enter 1st movie: "))
# list2 = input("Enter the movie name")
# list3 = input("Enter the movie name")
# list.append(list1)
# list.append(list2)
# list.append(list3)
# print(list)
# print(type(list))


#WAP to check if a list contains a palindrome of elements(Copy method) maam,racecar
# list1 = [1, 2, 1]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("Palindrome")
# else:
#     print("NOT palindrome")

#WAP to count the no of A grades
#[C,D,A,A,B,B,A]
# tup = ("C","D","A","A","B","B","A",)
# print(tup.count("A"))

#store the above values in a list & sort them from A to D
#[C,D,A,A,B,B,A]
# list=["C","D","A","A","B","B","A"]
# (list.sort( ))
# print(list)