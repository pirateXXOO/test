#!/usr/bin/python
# -*- coding = UTF-8 -*-

list = [1]

for i in range(1, 10):
    list.append((list[i-1]+1)*2)

print(list[9])