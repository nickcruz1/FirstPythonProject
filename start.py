import mysql.connector
import json


# # Start of First Python File - My Python Reference

# # Creating a variable
# x = 10
# print(x)

# # Casting (Changing Variable Types)
# x = 10  # currently is an int
# x = str("10")  # now x is a string
# print(x)

# x = 1j  # Complex

# # x = ["apple", "banana", "cherry"]  # list

# x = {"name": "John", "age": 30}  # dict

# y = True  # bool
# print(y)


# Picture of a Person Smiling

# print("**********")
# print("***HI*****")
# print("*Nick*****")


theData = {
    "name": "Nick",
    "model": "Subaru",
    "year": 400,
    "isIt": True
}

print("Hello Python World ")


mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

print(mydb)
