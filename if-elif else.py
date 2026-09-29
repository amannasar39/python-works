# # # # # # write a program to check whether a number is positive, negative or zero
# # # # # # n=int(input("enter a number: "))
# # # # # # if n>0:
# # # # # #     print("positive")
# # # # # # elif n<0:
# # # # # #     print("negative")
# # # # # # else:
# # # # # #     print("zero")

# # # # # # write a program to find the greatest of three numbers
# # # # # n1=int(input("enter first number: "))
# # # # # n2=int(input("enter second number: "))
# # # # # n3=int(input("enter third number: "))
# # # # # if n1>n2 and n1>n3:
# # # # #     print(n1,"is greatest")
# # # # # elif n2>n1 and n2>n3:
# # # # #     print(n2,"is greatest")
# # # # # else:
# # # # #     print(n3,"is greatest")
# # # # # write a program to calculate electricity bill based on the following criteria
# # # # #units consumer rates per unit
# # # #     # #<=100 0
# # # #     # #100-200 5rs/unit
# # # #     # #200-300 10rs/unit
# # # #     # #>300 15rs/unit
# # # #     # units=int(input("enter the number of units consumed: "))
# # # #     # if units<=100:
# # # #     #     bill=0
# # # #     # elif units<=200:
# # # #     #     bill=(units-100)*5
# # # #     # elif units<=300:
# # # #     #     bill=(100*5)+(units-200)*10
# # # #     # else:
# # # #     #     bill=(100*5)+(100*10)+(units-300)*15
# # # #     # print("the electricity bill is: ", bill)

# # # # #write a check whether the user entered number is 2digit or 3 digit number or 4 digit number
# # # # n=int(input("enter a number: "))    
# # # # if n>=10 and n<=99:
# # # #     print("the number is a 2 digit number")
# # # # elif n>=100 and n<=999:
# # # #     print("the number is a 3 digit number")
# # # # else:
# # # #     print("the number is a 4 digit number")

# # # # write a basic calculator program to perform arithmetic operations
# # # #(+, -, *, /,//,%)
# # # n1=int(input("enter first number: "))
# # # n2=int(input("enter second number: "))
# # # operator=input("enter operator (+, -, *, /, //, %): ")
# # # if operator=="+":
# # #     print(n1+n2)
# # # elif operator=="-":
# # #     print(n1-n2)
# # # elif operator=="*":
# # #     print(n1*n2)
# # # elif operator=="/":
# # #     print(n1/n2)
# # # elif operator=="//":
# # #     print(n1//n2)
# # # elif operator=="%":
# # #     print(n1%n2)
# # # else:
# # #     print("invalid operator")    

# # # write a program to print number of days in a month
# # month=int(input("enter month number: "))
# # if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
# #     print("31 days")
# # elif month==4 or month==6 or month==9 or month==11:
# #     print("30 days")
# # elif month==2:  
# #     print("28 days")
# # else:
# #     print("invalid month number")

# #write a program to print grades based on following criteria
# #91-180 A
# #81-90 B
# #71-80 C
# #61-70 D
# #<=60 F
# grade=int(input("enter your grade: "))
# if grade>=91 and grade<=180:
#     print("A")
# elif grade>=81 and grade<=90:
#     print("B")
# elif grade>=71 and grade<=80:
#     print("C")
# elif grade>=61 and grade<=70:
#     print("D")
# elif grade<=60:
#     print("F")
# else:
#     print("invalid grade")
