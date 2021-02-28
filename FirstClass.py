class Computer:

    #class/static variable
    father="Charles Babbage"

    def __init__(self):
        print("I'm the constructor for class  Computer. I'll be called everytime.")

    def about(self, ram, cpu):
        #instance variable, instance method - using self
        self.ram=ram
        self.cpu=cpu
        print("Hi I'm a computer and my ram is ", ram , " and cpu is ", cpu)

    #instant method  - any method that accepts self
    def comp(self):
        print("Hi, I'm an instant method since I've self.")

    def get_ram(self):
        #I'm an accessor method - getter
        return self.ram
    def set_ram(self, ramval):
        #I'm a mutator method - setter
        self.ram=ramval

    #class method - uses cls as the parameter
    @classmethod
    #used decorator to not pass cls inside it
    def computerowner(cls):
        print("My owner is you.")
        return 'YOU'

    #static method - don't get affected by the kind of variable that is there, it is uniform for all.
    @staticmethod
    def statexmp():
        return "Hi I'm static method, who are you?"

c1=Computer()#obj1
c2=Computer()#obj2
c1.about(3,'i5')
#everytime objects are assigned different address and their size depends on the kind/size of variables and methods
print("Address of object 1: ",id(c1))
print("Address of object 2: ",id(c2))

c1.ram=8

print(c1.ram)
c2.about(2,'i3')
print("Father of computer is: ", Computer.father)

print("Ram of c1 is: ", c1.get_ram())
print("Ram of c2 is: ", c2.get_ram())

#modififying ram values
c1.set_ram(9)
c2.set_ram(7)

print("Ram of c1 is: ", c1.get_ram())
print("Ram of c2 is: ", c2.get_ram())

#class method can be called using both object and class too.
print ("Owner info: ", c1.computerowner())
print ("Owner info: ", Computer.computerowner())

#calling static method
print("Calling static: ", c1.statexmp())
print("Calling static: ", Computer.statexmp())