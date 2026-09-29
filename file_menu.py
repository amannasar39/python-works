def fileread():
    filename=input('enter the file name')
    f=open(filename,'r')
    content=f.read()
    print(content)
    f.close()
def filewrite():
    filename=input('enter the file name')
    f=open(filename,'w')
    content=input('enter the content')
    f.write(content)
    f.close()
def fileappend():
    filename = input('enter the file name')
    f = open(filename, 'a')
    content = input('enter the content')
    f.write(content)
    f.close()
def filesearch():
    filename=input("enter file name")
    f=open(filename,'r')
    content=f.read()
    word=input("enter the word")
    if word in content:
        print("word found")
    else:
        print("word not found")
def file_delete():
    import os
    filename=input("enter the filename")
    os.remove(filename)
    print("file deleted")
while(True):
    print('1.read')
    print('2.write')
    print('3.append')
    print('4.search')
    print('5.delete')
    print('6.exit')
    ch=int(input('enter your choice'))
    if ch==1:
        fileread()
    elif ch==2:
        filewrite()
    elif ch==3:
        fileappend()
    elif ch==4:
        filesearch()
    elif ch==5:
       file_delete()
    else:
        exit()