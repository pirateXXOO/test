# Author:Jack
# Date:2018/8/19

# s2=set('alex')
# print(s2)
# s2.add('op')
# print(s2)


# def f(n):
#     return n*n
# def foo(a,b,func):
#     ret=func(a)+func(b)
#     return ret
# print(foo(1,2,f))

# def fat(n):
#     set = 1
#     for i in range(1,n+1):
#         set=set*i
#     return set
#
# print(fat(5))


# def fact(n):
#     if n == 1 :
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))

# 递归的特性：
## 1. 调用自身函数
## 2. 有一个结束条件

# 但凡是递归可以写的循环都能解决
# 递归的效率在有些时候很低

# 0 1 1 2 3 5 8
def fibo(n):
    if n == 1 or n == 0:
        return n
    # if n == 1:
    #     return 0
    # if n == 2:
    #     return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(5))