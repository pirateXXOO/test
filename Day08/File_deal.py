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


f=open('test','r')
file=f.readlines()
for i in file:
    print(i.strip())
f.close()
