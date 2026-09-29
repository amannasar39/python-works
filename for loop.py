# s="hello"
# for i in s:
#     print(i)

# s={1,2,3,4}
# for i in s:
#     if i%2==0:
#     print(i)

#print each colors l=['red','green','blue']
# s=['red','green','blue']
# for i in s:
#     print(i)

# d={'a':10,'b':20,'c':30}
# for i in d:
#     print(i, ":",d[i])

#print the sum of numbers in the list l=[56,89,34,10]
# l=[56,89,34,10]
# sum=0
# for i in l:
#     sum=sum+i
#     print(i)

#l=[12,34,56,45,89,16,69,33]
#print each number in a list
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     print(i)

#print even values
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if i%2==0:
#         print(i)

#print those numbers div by 3
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if i%3==0:
#         print(i)

#print those number contains digit '3'
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if '3' in str(i):
#         print(i)

#sum of list
# l=[12,34,56,45,89,16,69,33]
# sum=0
# for i in l:
#     sum+=i
#     print(sum)

#count of even num
# l=[12,34,56,45,89,16,69,33]
# count=0
# for i in l:
#     if i%2==0:
#         count+=1
#         print(count)

#product of list
# l=[12,34,56,45,89,16,69,33]
# product=1
# for i in l:
#     product*=i
# print(product)

#print only float
# l=[12,4,5,6.8,30,"arun","hello"]
# for i in l:
#     if type(i)==float:
#         print(i)

#string values
# l=[12,4,5,6.8,30,"arun","hello"]
# for i in l:
#     if type(i)==str:
#         print(i)
    

#d={'a':23,'b':25,'c':28,'d':30,'e':22}
#even values
# d={'a':23,'b':25,'c':28,'d':30,'e':22}
# for i in d.values:
#     if d[i]%2==0:
#         print(d[i])

#colors=['red','green','blue','orange','black']
#print starting letter
# colors=['red','green','blue','orange','black']
# for i in colors:
#     print(i[0])

#last letter
# colors=['red','green','blue','orange','black']
# for i in colors:
#      print(i[-1])

#reverse
# colors=['red','green','blue','orange','black']
# rev=[]
# for i in colors:
#      rev=[i]+rev
#      print(rev)

#all colors contains letter b
colors=['red','green','blue','orange','black']
for i in colors:
    if 'b' in i:
        print(i)

