# Author:Jack
# Date:2018/8/11

a=[1,2,3]
b=list([4,5,6])
print(a)
print(b)
print(type(a))
print(type(b))

c=(1,2,3)
d=tuple([4,5,6])
print(c)
print(d)
print(type(c))
print(type(d))


s=set('alex')
print(s)
print(type(s))


s=set(['1','2','3','who'])
print(type(s),s)
s.add('shell')
print(type(s),s)

s=set('alex')
b=set("slexxxeeelll")
print(s==b)

c=s.intersection(b)
print(c)
print(s&b)

print(b.difference(s))
print(b-s)
print(s.union(b))
print(s | b)

print(s.symmetric_difference(b))
print(s^b)

print(s.issuperset(b))
print(s.issubset(b))

