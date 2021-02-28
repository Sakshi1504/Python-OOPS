'''
num=[5,1,2,3]

print(num[2])

it = iter(num)

print(it.__next__())
print(it.__next__())
#iterator takes forward further values, and don't repeat the same value again
for i in it:
    print(i)
'''
class TopTen:

    def __init__(self):
         self.num=1


    def  __iter__(self):
        return self

    def __next__(self):
        if(self.num<=10):
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration

t=TopTen()

for i in t:
    print(i)

#print(t.__iter__())
#print(t.__next__())
#print(next(t))