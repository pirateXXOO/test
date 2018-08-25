# Author:Jack
# Date:2018/8/25
import time

# 功能函数加参数
def show_time(f):
    def inner(*x,**y):
        start = time.time()
        f(*x,**y)
        end = time.time()
        print("spend %s"%(end-start))
    return inner

@show_time # add=show_time(add)
def add(*a,**b):
    sum = 0
    for i in a:
        sum+=i
    print(sum)


add(3,4,9)

