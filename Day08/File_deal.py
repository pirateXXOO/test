# Author:Jack
# Date:2018/6/3


# data = open("test",'r').read()
# r=open('test','r',encoding='utf-8')
# data=r.read(10)
# r.close()
# print(data)

# w=open('test','w')
# data=w.write('shell')
# type(data)
# print(data)
# w.close()

# open('test2','w')
# w=open('test','w')
# w.write('shell')
# w.write('shell3')
# w.close()
# w=open('test','w')
# w.write('bash')
# w.close()
# r=open('test','r')
# data = r.read()
# print(data)
# r.close()

# f=open('test','a')
# f.write('shell\n')
# f.write('config')
# f.close()


# f=open('test','r')
# file=f.readlines()
# for i in file:
#     print(i.strip())
# f.close()


# f = open('test','r') # for 内部将f 做成迭代器，用一个取一个
# for i in f:
#     print(i.strip())
# f.close()

#
# f=open('test','r',encoding='utf8')
# for i in f.readlines():
#     print(i.strip())
# f.close()


# f=open('test','r')
# number=0
# for i in f: # 迭代器
#     number+=1
#     if number == 1:
#         i=''.join([i.strip(),'####'])
#     print(i.strip())
# f.close()


f=open('test','r')
print(f.tell())
print(f.read(3))
print(f.tell())
f.seek(0)
print(f.tell())
print(f.read(4))
f.close()


