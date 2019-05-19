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


# f=open('test','r')
# print(f.tell())
# print(f.read(3))
# print(f.tell())
# f.seek(0)
# print(f.tell())
# print(f.read(4))
# f.close()


# import sys,time
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.2)

# import sys,time
# for i in range(30):
#     print("*",end="",flush=True)
#     time.sleep(0.1)

# f=open("test",'w')
# d=f.truncate(5)
# print(d)
# print(f)
# f.close()

# f=open('test','a+',encoding='utf8')
# print(f.readline())
# print(f.tell())
# f.write('yuefei')
# f.seek(0)
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()

# f=open('test','r+',encoding='utf8')
# number = 0
# for line in f:
#     number+=1
#     if number == 6:
#         f.write('alex')
# f.close()

# f=open('test','r',encoding='utf-8')
# d=open('test3','w',encoding='utf-8')
# number=0
# for i in f:
#     number+=1
#     if number==5:
#         i=''.join([i.strip(),'shellllkjsdijfijei'])
#     d.write(i)
# d.close()
# f.close()

# f=open('test','r')
# f.close()
# with open('test','r') as f:
#     f.readline()
#     f.read()
# print('hello')

# with open('test','r') as f_read , open('test3','w') as f_write:
#     for line in f_read:
#         f_write.write(line)

f = open('account', 'r', encoding='utf-8')
print(f.readline().strip().split())
print(f.readline().strip())
f.close()
