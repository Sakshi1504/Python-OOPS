def topten():
    yield 5
    yield 1
    yield 2
    yield 3

values=topten()
print(values)
print(values.__next__())
#works same as generator, don't repeat the values that are already processed
for i in values:
    print(i)


#now if we want to process multiple values

def top():

    num=1

    while num<=10:
        yield num
        num+=1

vals=top()

for i in vals:
    print(i)