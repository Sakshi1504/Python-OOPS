#Method overloading doesn't exit in Python, this is a work around
class A:

    def sum(self, a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a


a1=A()

print(a1.sum(5,6))
#what if I want to do sum of 3 numbers
print(a1.sum(5,7,3)) #error will be generated, so we're modifying the function now


#Method Overriding

class D:

    def show(self):
        print("In A show")
class B(D):

    def show(self):
        print("now in B show")
    pass

d1=B()

d1.show()