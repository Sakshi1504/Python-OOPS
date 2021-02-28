class test:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def __add__(self, other):
        op1=self.num1+other.num1
        op2=self.num2+other.num2
        op=test(op1,op2)
        return op

    def __gt__(self, other):
        n1=self.num1+self.num2
        n2=other.num1+other.num2
        if(n1>n2):
            return True
        else:
            return False

    def __str__(self):
        return "{} {} ".format(self.num1, self.num2)


t1=test(1,1)
t2=test(2,2)
res=t1+t2

print(t1+t2)
print(res.num1)

if(t2>t1):
    print("greater")
else:
    print("lesser")


a=10
print(a)

print(a.__str__())

print(t1)
print(t2)
print(t1.__str__())
print(t2.__str__())