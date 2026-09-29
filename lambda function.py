#simple anonymous function written in a single line and defines using 'lambda' keyword
#it is mainly used to define simple operations in higher order type functions


#user defined
#define a function that takes number as an argument and return its square

# def fn(num):
#     return num * num
# r=fn(4)
# print(r)

# lambda

# square of number
# s=lambda n: n**2
# print(s(5))

# cube of a number
# s=lambda n: n**3
# print(s(2))


#sum of 2 num
# s=lambda n1,n2:n1+n2
# print(s(3,2))

#product of 3 numbers
# s=lambda n1,n2,n3:n1*n2*n3
# print(s(3,2,4))

#length of a string
# s=lambda text:len(text)
# print(s("red"))

#square root of a number
# s=lambda n:n**0.5
# print(s(81))



#first letter of a string
# s=lambda text:text[0]
# print(s("red"))

#last letter of a string
# s=lambda text:text[-1]
# print(s("red"))

#name value from dictionary
# s = lambda d: d["name"]

# person = {"name": "Aman", "age": 22, "salary": 30000}
# print(s(person))

#salary value from dictionary
# s = lambda d: d["salary"]
# person = {"name": "Aman", "age": 22, "salary": 30000}
# print(person["salary"])

#add 10 to a number
# s=lambda n:n+10
# print(s(5))

#map

# create a new list of squares

# l=[1,2,3,4]
# print(list(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))
# print(dict(map(lambda x:x**2,l)))


#create a new list of cubes
# print(list(map(lambda x:x**3,l)))


#create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l)))


#create a new list of lengths
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda text:len(text),colors)))


#create a new list of first characters
# print(list(map(lambda text:text[0],colors)))




#create a new list of last characters
# print(list(map(lambda text:text[-1],colors)))




#create a new list of reverse of each elemnt
# print(list(map(lambda text:text[::-1],colors)))



# l=[23,78,12,56]
#Add 10 to each element in the given sequence
# print(list(map(lambda x:x+10,l)))






##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]

# # create a new list of emails
# print(list(map(lambda x:x['email'],l)))

#filter
# l=[23,65,89,12,20,33,85,40]
#filter element greater than 50
# print(list(filter(lambda x:x>50,l)))


#filter even values less than 50
# print(list(filter(lambda x:x%2==0 and x<50,l)))


# l=["apple","orange","pineapple","grapes","avacado"]
#filter elemnt whose length is greater than 5
# print(list(filter(lambda text:len(text)>5,l)))