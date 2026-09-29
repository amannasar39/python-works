# 1. Given a string
s = "I am learning Python"
# Find the length of the string
print("Length:", len(s))
# Find the reverse of the string
print("Reverse:", s[::-1])
# Find the last character of the string
print("Last Character:", s[-1])
# Find the 13th character (counting from 1)
print("13th Character:", s[12])
# Print the characters from 2nd index to 15th index
print("Characters from index 2 to 15:", s[2:16])
# Combine the string with the word "Programming"
print("Combined String:", s + " Programming")
# 2. Given a list
l = ['Guitar', 'Piano', 'Violin', 'Drums', 'Flute']
# Add a new item 'Veena'
l.append("Veena")
print("Updated Instrument List:", l)
# 3. Declare a list of 5 food items
food = ["Pizza", "Burger", "Biryani", "Dosa", "Pasta"]
# Add new food item
food.append("Sandwich")
# Change the second food item
food[1] = "Noodles"
# Print updated list
print("Updated Food List:", food)
# Print the last food item
print("Last Food Item:", food[-1])
# Print the number of food items
print("Number of Food Items:", len(food))
# 4. Given a string
s = "python is a programming language"
# Remove the first 10 characters
print("After Removing First 10 Characters:", s[10:])
# Print the last 5 characters
print("Last 5 Characters:", s[-5:])
# 5. Interchange 2nd index and 5th index numbers
l = [10, 56, 23, 67, 19, 70]
l[2], l[5] = l[5], l[2]
print("Updated List:", l)
# 6. Given a set
s = {10, 20, 30, 40}
# Add a new number 50
s.add(50)
print("Updated Set:", s)