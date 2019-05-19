# Author:Jack
# Date:2018/8/25

s = ( x*2 for x in range(10) )

print(s)
# 生成器就是一个可迭代对象（Interable）
for i in s:
    print(i)

## yeild

def foo():
    print('ok')
    yield 1
print(foo())


