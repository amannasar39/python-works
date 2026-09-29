try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    r=num1 / num2
    print("Result:", r)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")

except:#general code if any error occurs other than above two errors
    print("An unexpected error occurred.")