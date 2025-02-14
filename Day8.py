#OOPS Class & object

# class Car:
#     color ="blue"
#     brand = "mercedes"

# car1 = Car( )
# print(car1.color)
# print(car1.brand)



# class Student:
#     #default constructors
#     def __init__(self):
#         pass

#     #parameterized constructors
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database...")

# s1 = Student ("karan", 97)
# print(s1.name, s1.marks)   #object attr > class attr

# s2 = Student ("arjun", 67)
# print(s2.name, s2.marks)


#Methods
# class Student: #class
#     college_name = "ABC College"

#     def __init__(self,name,marks): #constructor (initlization of object__init__)
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome students,", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("karan", 97) #object
# s1.welcome( )
# print(s1.get_marks())



#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi",self.name,"your avg score is:",sum/3)

# s1 = Student("Laxman",[99,99,100])
# s1.get_avg()



#Create account class with 2 attributes - balance & account no
#Create methods for debit,credit & printing the balance


# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     #debit method
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs",amount,"was debited")
#         print("total balance =",self.get_balance())

#     def credit(self,amount):
#         self.balance +=amount
#         print("Rs",amount,"was credited")
#         print("total balance =",self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000, 12345)
# # print(acc1.balance)
# # print(acc1.account_no)
# acc1.debit(1000)
# acc1.credit(500)
