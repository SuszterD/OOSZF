import this

print('Hello World')

age = 5

for i in range(5):
    print(age + i)


def substract(a, b):
    return a-b

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


result=substract(10, 3)
print(result)

result=add(10,11)
print(result)

result=multiply(5,6)
print(result)

result=divide(10,2)
print(result)

thislist= ["Alma", "Szolo", "Banan", "Ananasz", "Korte"]
print(thislist)

thislist.sort()
print(thislist)

for fruits in thislist:
    a = fruits.startswith('A')
    print(a)

def kerulet(a):
    return a*a

result=kerulet(5)
print(result)