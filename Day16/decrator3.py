# Author:Jack
# Date:2018/8/25

# 装饰器加参数
import time

def logger(flag):
    def show_time(f):
        def inner(*x,**y):
            start = time.time()
            f(*x,**y)
            time.sleep(1)
            end = time.time()
            print("spend %s"%(end-start))
            if flag == 'true':
                print('Logging')
        return inner
    return show_time

@logger('true') # @show_timw
def add(*a,**b):
    sum = 0
    for i in a:
        sum+=i
    print(sum)

add(1,2,3,4,5)