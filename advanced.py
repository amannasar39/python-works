#non local/enclosing scope
#non local variaable declered indise nested functions

def outer():
    x=20 #non local


    def inner():
        y=30 #local
        print("inside inner function",x)
    inner()
    print("inside outer function",x)
outer()


#built in scope
#scope of all names decleared inside python value