class A:

    def __init__(self):
        print("in A")

    def feature1(self):
        print("This is feature 1.")

    def feature0(self):
        print("This is feature0.")

class B(A):

    def __init__(self):
        super().__init__() #to call the constructor of super class
        print("in B")

    def feature3(self):
        print("This is feature3.")

    def feature0(self):
        print("This is feature0")

b1=B()



#multiple inheritance and MRO
class S:

    def __init__(self):
        print("in S")

    def feature1(self):
        print("This is feature 1.")

    def feature0(self):
        print("This is feature0 S.")

class T:

    def __init__(self):
        #super().__init__() #to call the constructor of super class
        print("in T")

    def feature3(self):
        print("This is feature3.")

    def feature0(self):
        print("This is feature0 T")


class U(S,T):

    def __init__(self):
        super().__init__() #will call contructor of left class
        print("IN U")
        super().feature0() #will call function of left class

u1=U()