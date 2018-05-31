# Author:Jack
# Date:2018/4/2

# a = (1,2,3,4)
# print(a[1:2])
#
# product = [('Mac',5000),('bicycle','400')]
# print(product[1][1])
#
# for i,j in enumerate(product,1):
#     print(i,"\t",j)


dict = {'name':'alex','age':'35','hobby':'girl','is_handsome':'True'}
# for i in range(1,100):
#     print(dict)
dict = {'name':'alex','age':'35','hobby':{'name':'tiechui','age':'56'},'is_handsome':'True'}
print(dict['hobby'] )

### 字典两大特点：无序，键唯一

#
# a = list((1,2,3))
# print(a)
#
# b = dict((('name','jack'),))
# print(b)

# setdefault
#  键存在，不改动，返回字典中相应的键对应的值
# 键不存在，在字典中增加新的键值对，并返回值
dic1 = {'name':'alex'}
dic1['age'] = 18
print(dic1.setdefault('age',34))
print(dic1)

print(dic1['name'])
print(type(dic1.keys()))
print(list(dic1.keys()))
print(dic1.keys())


print(dic1.values())

print(dic1.items())


dict.update(dic1)
print(dict)
print(dic1)

del dic1['name']
print(dic1)
print(dic1.pop('age'))

print(dic1)
dic1.clear()
print(dic1)

del dic1
