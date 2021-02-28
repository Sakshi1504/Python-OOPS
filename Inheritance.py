class A:

    def feature1(self):
        print("This is feature 1.")

    def feature2(self):
        print("This is feature 2.")

class B(A):

    def feature3(self):
        print("This is feature 3.")

    def feature4(self):
        print("This is feature 4.")

class C(B):

    def feature5(self):
        print("This is feature 5.")

a1=A()
b1=B()

print("A: ", a1.feature2())

c1=C()
  
