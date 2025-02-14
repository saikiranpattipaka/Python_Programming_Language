# OOPs 2

# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("rama")
# print(s1.name)
# del s1.name
# print(s1.name)


#Private attributes & method

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())

#Inheritance
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.color)


#Define a Circle class to create a circle with radius r using the constructor
#Define an Area() method of the class which calculates the area of the circle. pir^2
#Define a Perimeter() method of the class which allows you to calculate the permiter o fthe circle 2pi r

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimeter(self):
#         return 2 + (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())


# Define a Employee class with attributes role, department & salary.This class also a showDetails( ) method
# Create an Engineer class that inhetites properties from Employee & has additional attributes : name & age.

# class Employee:
#     def __init__(self, role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
    
#     def showDetails(self):
#         print("role = ", self.role)
#         print("dept =", self.dept)
#         print("salary =",self.salary)
        

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")

# engg1 = Engineer("Musk", 40)
# engg1.showDetails( )

# e1 = Employee("accountant", "Finance", "60,000")
# e1.showDetails()


#Create a class called Order which stores item & its price
#Use Dunder function _ _gt_ _ to convey that:
#order1> order2 if price of order1 > price of order2

# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price

#     def __gt__(self, odr2):
#         return self.price > odr2.price

# odr1 = Order("chips",20)
# odr2 = Order("tea", 15)

# print(odr1 > odr2) #True
