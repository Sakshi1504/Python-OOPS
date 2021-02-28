class Sakshi:

    def __int__(self):
        print("Surname is.")
        #creating object for inner class
        self.innerclsobj=self.skills()

    def show(self):
        print ("Hi")
        #self.innerclsobj.skillshow()

    #inner class
    class skills:

        def __init__(self):
            print("I've technical skills.")

        def skillshow(self):
            print("Showcase skills")


s1=Sakshi()

s1.surname="Agrawal"
print("SN: ", s1.show())
#print("Calling innerclassobject: ", innerclsobj)

innerobj=Sakshi.skills()

#innerobj.skillshow()