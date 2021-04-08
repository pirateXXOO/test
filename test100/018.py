#!/usr/bin/python
# -*- coding: UTF:-  -*-

num = int(input('Please input num:'))
times = int(input('Please input times: '))

result = 0
total = 0
i = 0
while i < times:
    print(num)
    result = result*10 + num
    total = total + result
    i += 1

print(total)
