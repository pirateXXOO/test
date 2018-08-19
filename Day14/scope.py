# Author:Jack
# Date:2018/8/19

# x = int(2.9)
# def outer():
#     o_count = 1
#     def inner():
#         i_count = 2
#         print(i_count)
#     inner()
# outer()

count = 10
def outer():
    # global count
    # count = 5
    # print(count)
    count = 10
    def inner():
        nonlocal count
        count = 123
        print(count)
    inner()
outer()