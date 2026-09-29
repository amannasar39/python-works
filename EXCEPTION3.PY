# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

import math

try:
    num = int(input("Enter a number: "))
    print("Factorial =", math.factorial(num))
except ValueError:
    print("Please enter a valid number")


# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:
        try:
            print("Result =", num1 / num2)
        except ZeroDivisionError:
            print("Cannot divide by zero")

    else:
        print("Invalid choice")

except ValueError:
    print("Invalid input")



# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

try:
    file = open("sample.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File does not exist")


#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

d = {
    "name": "arun",
    "age": 23,
    "place": "ekm"
}

try:
    key = input("Enter a key: ")
    print("Value =", d[key])

except KeyError:
    print("Key does not exist")


