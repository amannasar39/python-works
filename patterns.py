
# n=[1,2,3]
# qns=['what','when','why']
# #print in patterns
# #n=[1,2,3]
# #qns=['what','when','why']
# #1
# #what when why
# #2
# #what when why
# #3
# #what when why
# for i in n:
#     print(i)
#     for j in qns:
#         print(j,end=" ")
#     print()

# for i in range(1,4):
#     for j in range(1,5):
#         print('*',end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

#2222
#4444
#6666
#8888
# for i in range(1,5):
#     for j in range(1,5):
#         print(i*2,end=" ")
#     print()

#55555
#4444
#333
#22
#1
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#1111
#2222
#3333
#4444
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()

#1000
#0200
#0030
#0004
# for i in range(1,5):
#     for j in range(1,5):
#         if (i==j):
#             print(i,end=" ")
#         else:
#             print("0",end=" ")
#     print()

#1
#10
#101
#1010
# for i in range(1,5):
#     for j in range(1,i+1):
#         if (j%2==0):
#             print("0",end="")
#         else:
#             print("1",end="")
#     print()


# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#1
#23
#456
#78910

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=1
#     print()

#1
#4 9
#16 25 36
#49 64 81 100
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k**2,end=" ")
#         k+=1
#     print()

#1
#3 5
#7 9 11
#13 15 17 19
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=2
#     print()

#a
#b c
#d e f
#g h i j
# k=ord('a')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()

#a
#b b
#c c c
#d d d d
# k=ord('a')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k+=1
#     print()
#a
#a b
#a b c
#a b c d

# for i in range(1,5):
#     k=ord('a')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()

#l=[23,65,42,80,56,41]
#print all even numbers from the list

# l=[23,65,42,80,56,41]
# for i in l:
#     if i%2==0:
#         print(i)

#print prime numbers from the list
# l=[23,65,42,80,56,41]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

#print all prime numbers in the range of (1,100)
# for i in range(1,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

#print all armstrong numbers in the range of (100,1000)
# for i in range(100,1000):
#     s=str(i)
#     l=len(s)
#     sum=0
#     for j in s:
#         sum+=int(j)**l
#     if sum==i:
#     print(i)

# k=6
# for i in range(1,5):
#     print(end="  ")

# k=k-2
# for j in range(1,i+1):
#     print(end="  ")

k=ord('e')
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k+=1
    print()