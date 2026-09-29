#factorial of a number entered by a user 5!=5*4*3*2*1
n=int(input("enter a number: "))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
    print(fact)

#sum of digits of a number
n=(input("enter a number: "))
s=0
while n>0:
    d=n%10
    s=s+d=n//10
    print(s)