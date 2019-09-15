# -*- coding:utf-8 -*-

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

# for i in myiter:
#     print(i)

a = (x*x for x in range(10))
print(a)
print(sum(a))

print(sum(i for i in range(100)))

def is_odd(n):
    return n%2 == 1
print(is_odd(3))
L = list(filter(is_odd,range(1,20)))
print(L)
print("-"*50)

L2 = filter(lambda n: n%2 == 1,range(1,20))
print(list(L2))


info = [0,1,2,3,4,5,6,7,8,9]
b = []
for index,i in enumerate(info):
    print(index,i+1)
    b.append(i+1)
print(b)

c = [i+1 for i in info]
print(c)

