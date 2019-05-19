# Author:Jack
# Date:2018/8/25

a = [x for x in range(10)]
print(a)

b=[x*2 for x in range(10)]
print(b)

def f(n):
    return n*n*n
c=[f(x) for x in range(10)]
print(c)

t = ('abc',9)
a,b = t
print(a,b)
