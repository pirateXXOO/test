# Author:Jack
# Date:2018/8/25

import time
# s = (x*2 for x in range(10))
#
# print(s)
# # 生成器就是一个可迭代对象（Interable）
# for i in s:
#     print(i)
#
# # yeild
#
#
# def foo():
#     print('ok')
#     yield 1
#     print('OK2')
#     yield 2
#
#
# g = foo()
#
# # print(g)
#
# # next(g)
# # next(g)
#
# for i in g:
#     print(i)


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
# # print(b)
#         yield b
#         a, b = b, a+b
#         n = n+1
#
#
# g = fib(8)
#
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def foo():
#     print('ok')
#     count = yield 1
#     print(count)
#
#     yield 2
#
#
# b = foo()
#
# s = b.send(None)
# print(s)
# b.send('fff')
# def consumer(name):
#     print("%s is ready to eat!" % name)
#     while True:
#         baozi = yield
#
#         print("baozi %s coming , it is ate by %s" % (baozi, name))
#
#
# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     next(c)
#     next(c2)
#     print("I am going to make baozi!")
#     for i in range(10):
#         time.sleep(2)
#         print("Two baozi made!")
#         c.send(i)
#         c2.send(i)
#
#
# producer('Alix')

lis = [1, 2, 3, 4]
d = iter(lis)
print(d)

print(next(d))
print(next(d))
print(next(d))
print(next(d))
