## Define a function to find factors of a number
def factors():
    n = int(input("Enter the number: "))
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


factors()


# Sum of 2 numbers
def sum(n1, n2):
    s = n1 + n2
    print("Sum:", s)


sum(10, 20)


# Simple Interest
def interest(p, y, r):
    simple_interest = (p * y * r) / 100
    print("Simple Interest:", simple_interest)


interest(10000, 2, 5)


# Count a specific character in a string
def count(text, char):
    count = 0

    for i in text:
        if i == char:
            count = count + 1

    print("Count =", count)


count("banana", "a")


# Product of 3 numbers
def product(num1, num2, num3):
    return num1 * num2 * num3


result = product(2, 3, 4)
print(result)


# Dictionary: words as keys and length as values
def new_dict(text):
    new = {}

    for i in text.split():
        new[i] = len(i)

    return new


text = input("Enter the string: ")
result = new_dict(text)
print(result)


# List of lengths
l = ["red", "green", "orange", "yellow", "blue"]

def new_list(l):
    new = []

    for i in l:
        new.append(len(i))

    return new


r = new_list(l)
print(r)