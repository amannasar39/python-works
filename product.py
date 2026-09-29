# #product of series 1,2,3,4,5
# product=1
# i=1
# while i<=5:
#     product*=i
#     i+=1
#     # print(product)

#product of first 10 odd numbers (1,3,5,...19)
# product=1
# i=1
# while i<=19:
#     product*=i
#     i=i+2
#     print(product)

#product of num that contains digit '3' in range(1,50)
product=1
i=1
while i<50:
    if '3' in str(i):
        product=product*i
    i+=1
    print(product)
