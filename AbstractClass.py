#abstract classes can be useful when they have other defind methods too.
from abc import ABC, abstractmethod


class exmpAbs(ABC):
    @abstractmethod
    def show(self):
        pass


#another class inheriting abstract class
class childcls(exmpAbs):
    def show(self):
        print("I'm a child class implementing the abstract class.")

class Whiteboard(exmpAbs):
    #so if we inherit from abstract class here, we need to implement its methods here
    def write(self):
        print("Writing on whiteboard.")

class objpass:
    def showup(self, obj):
        print("I'm showing up.")
        obj.show()

#e1=exmpAbs() #abstract classes can not be instantiated

c1=childcls()

c1.show() #cannot instantiate this method even using abstract method unless its defined

w1=Whiteboard()

o1=objpass()
o1.showup(w1)