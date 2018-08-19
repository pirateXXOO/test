# Author:Jack
# Date:2018/8/19

# def print_info(name,age,sex='male'):
#     print('Name:\t %s'%name)
#     print('Age:\t %d'%age)
#     print('Sex:\t %s'%sex)
# print_info('Jack',age=24,sex='female')

# def add(x,y,z):
#     print(x+y+z)
#
# add(1,2,3)

# def add(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(12,23,43,)

def print_info(sex='mael',*args1,**args2):
    print(sex)
    print(args1)
    print(args2)
    for i in args2:
        print('%s:\t%s'%(i,args2[i]))
print_info()
print_info('alex',age=24,job='IT',hobby='girls',height=185)
