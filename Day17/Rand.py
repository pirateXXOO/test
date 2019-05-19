# Author:Jack
# Date:2019/5/19

import random

# print(random.random())
# # print(random.random(1, 9))
# print(random.choice('name'))
# print(random.choice(['bsuudhufe','ksjdhfuhe','ksdhufheuhs']))
#
# print(random.shuffle(['bsuudhufe','ksjdhfuhe','ksdhufheuhs']))
# print(random.sample(['bsuudhufe', 'ksjdhfuhe', 'ksdhufheuhs'], 3))
# print(random.randrange(1,3))

# def va_co():
#     code = ''
#     for i in range(5):
#         if i == random.randint(0, 4):
#             add = random.randrange(10)
#         else:
#             add = chr(random.randrange(65, 91))
#         code += str(add)
#     print(code)

def va_co():
    code = ''
    for i in range(5):
        ad = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        code += str(ad)
    print(code)

va_co()

# print(chr(83))

