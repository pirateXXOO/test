# Author:Jack
# Date:2018/8/25

def outer():
    x = 10
    def inner(): # 条件1 inner 是一个内部函数
        c=100
        print(x) # 条件2：一个外部变量
        print(c)
    return inner # 结论： inner 是一个闭包
# inner  is a closure
# outer()()

 f=outer()
 f()

# 闭包 = 内部函数+ 定义函数时的环境