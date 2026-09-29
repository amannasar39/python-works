#read
f=open('k.txt','r')
#returns file content as a string format
#readlines()
#returns file content as list format

s=f.read()
print(s)
print(type(s))
f.close()