# Author:Jack
# Date:2018/8/25

import time


def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print("spend %s"%(end-start))
    return inner

@show_time
def foo():
    start = time.time()
    time.sleep(1)
    end = time.time()

show_time(foo)

foo=show_time(foo)
foo()


