# d = {'a':23,'b':25,'c':28,'d':30,'e':22}

# # Even values in dictionary
# print("Even values:")
# for value in d.values():
#     if value % 2 == 0:
#         print(value)

# colors = ['red','green','blue','orange','black']

# # Starting letter
# print("\nStarting letter:")
# for color in colors:
#     print(color[0])

# # Last letter
# print("\nLast letter:")
# for color in colors:
#     print(color[-1])

# # Reverse
# print("\nReverse:")
# for color in colors:
#     print(color[::-1])

# # All colors containing letter 'b'
# print("\nColors containing 'b':")
# for color in colors:
#     if 'b' in color:
#         print(color)

# # Range function

# # 100-200
# print("\n100 to 200:")
# for i in range(100, 201):
#     print(i, end=" ")

# # 1,2,3,4,5
# print("\n\n1 to 5:")
# for i in range(1, 6):
#     print(i, end=" ")

# # 1,3,5,7,9,11
# print("\n\nOdd numbers:")
# for i in range(1, 12, 2):
#     print(i, end=" ")

# # 2,4,6,8,10
# print("\n\nEven numbers:")
# for i in range(2, 11, 2):
#     print(i, end=" ")

# # 100,200,300,400,500
# print("\n\nMultiples of 100:")
# for i in range(100, 501, 100):
#     print(i, end=" ")

# # 5,4,3,2,1
# print("\n\nReverse 5 to 1:")
# for i in range(5, 0, -1):
#     print(i, end=" ")

# # 3,6,9,12,15,18,21
# print("\n\nMultiples of 3:")
# for i in range(3, 22, 3):
#     print(i, end=" ")

# # 1,4,9,16,25,36
# print("\n\nSquares:")
# for i in range(1, 7):
#     print(i**2, end=" ")

# # Print all 3-digit numbers (100-999)
# print("\n\n3-digit numbers:")
# for i in range(100, 1000):
#     print(i, end=" ")

# # Print all numbers divisible by 3 in the range 100-200
# print("\n\nNumbers divisible by 3 (100-200):")
# for i in range(100, 201):
#     if i % 3 == 0:
#         print(i, end=" ")

# # 1,8,27,64,125 (Cubes)
# print("\n\nCubes:")
# for i in range(1, 6):
#     print(i**3, end=" ")

colors=['red','green','blue','orange','yellow','black']
# # print each color
# for i in colors:
#     print(i)

#colors containing letter 'b'
# for i in colors:
#     if 'b' in i:
#         print(i)

#collors strating with g
# for i in colors:
#     if i[0]=='g':
#         print(i)

#colors ending with e
# for i in colors:
#     if i[-1]=='e':
#         print(i)

#all colors strating with 'b'
# for i in colors:
#     if i[0]=='b':
#         print(i)

#all colors except strating with 'b'
# for i in colors:
#     if i[0]=='b':
#         continue
#     print(i)

l=[23,45,12,78,90,51,75]
# print all numbers
# for i in l:
#   print(i)
# #print all even numbers
# for i in l:
#   if i%2==0:
#     print(i)

# print those numbers divisible by 5
# for i in l:
#   if i%5==0:
#     print(i)

#stops the loop if i>50
# for i in l:
#     if i>50:
#         break
#     print(i)

#skips all even numbers
# for i in l:
#     if i%2==0:
#         continue
#     print(i)

#print the first even numbers whose value is greater than 50
# for i in l:
#     if i>50 and i%2==0:
#         print(i)
#         break
#count of all even numbers
# count=0
# for i in l:
#     if i%2==0:
#         count+=1

# print(count)

#sum of list
# sum=0
# for i in l:
#     sum+=i
# print(sum)

# product of odd numbers
# product=1
# for i in l:
#     if i%1==0:
#         product*=i
#         print(product)  
