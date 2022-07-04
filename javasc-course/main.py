

from requests import delete


mystring = 'hello'
mystring += 'world'
print(mystring)

name = mystring +  ' muhammad' + ' nasr.' 
print(name)

# string is not imutable  mystring[0] = 'y'
print(mystring[-1])


list = [5, 6, 7]
list.pop()
print(list)

def function(l, i):
    l.append(id)
    return l 
    

lis = [1, 2, 3]
print(lis)
function(lis, 4)
lis.append(6)
print(lis)

def con(num):
    if num == 6:
        return True

print(con(6))


if 5 == '5':
    print('true')
else:
    print('false')

class Dog:
    __name='rex',
    legs=4
    taile=1

del Dog.taile
delattr(Dog, 'legs')

#print(Dog.__dict__)

heppy = Dog()
#print(heppy.__name)   # abstract attributes


class S:
    def __init__(self):
        self.x = 0
    def m(self):
        self.x += 1
        print(self.x)

u = S()
u.m()
print(u.x)
u.m()
print(u.x)
u.m()


    