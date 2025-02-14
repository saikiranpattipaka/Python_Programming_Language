# Dictionary & Set

# info = {
#     "name" : "rama",
#     "learning" : "python",
#     "age":"35",
#     "marks" : "35.6",
#     "subjects":["python", "c","java",],
#     "topics" : ("dict","set"),
#     "is_adult" : True,
#     12.5 : 89.99
# }

# print(info)
# print(info["name"])
# print(type(info))

# info["name"] = "sita" #changes the values
# info["surnmar"] = "surya" #adds the new value to the dictionary
# print(info)

#Nested dictionary
# student = {
#     "name" : "rahul",
#     "subjects" : {
#         "phy" : 87,
#         "chem" : 92,
#         "math" : 90,
#     }
# }
# print(student)
# print(student["subjects"]["chem"]) #relevant information
# print(student.keys()) #returns all keys
# print(student.values())  #returns all values
# print(student.items())  #returns all (key, val) pairs as tuples
# print(student.get("subjects"))  #returns the key according to value
# student.update({"city":"Hyderabad"}) 
# print(student)

# Set
# collection = {1, 2, 3, 4, "hello","world"}
# print(collection)
# print(type(collection))
# print(len(collection)) #length of items

#Empty set
# collection = set() #empty set ; syntax

# print(type(collection))

#set methods

# collection = set( )
# collection.add(1)
# collection.add(2)
# collection.add("college")

# collection.remove(1)
# collection.clear()
# collection = {"hello","world", "program","python"}

# print(collection.pop())

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.union(set2))
# print(set1.intersection(set2))

#WAP in python dictionary table : a piece of furniture , list of facts & figures
#cat : a small animal

# dict = {
#     "table" : ["a piece of furniture", "list of facts & figures"],
#     "cat" : "a small animal",
# }
# print(dict)

#you are given a list of sujects for students.Assume one classroom is equired for 1 subject
#python, java, C++, python, javascript, java, python, java, C++, c
# set = {"python","java","C++","python","javascript","java","python","java","C++","c"}
# print(len(set))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary
#start with an empty dict & add one by one use subject name as key & marks as value
# null_dict = {}

# x = int(input("enter phy marks:" ))
# null_dict.update({"phy":x})

# y = int(input("enter chem marks:"))
# null_dict.update({"chem":y})

# z = int(input("enter soc marks:" ))
# null_dict.update({"soc":z})

# print(null_dict)


#figure out a way to store 9 & 9.0 as separate values in the set
#(you can take help of built-in data types)

# set = {9,"9.0"}
# print(set)

# set = {
#     ("float", 9.0),
#     ("int",9)
# }
# print(set)
