#!/usr/bin/python
# -*- coding = UTF-8 -*-

start = 100
during = [100]
for i in range(1, 100):
    during.append(start * (0.5 ** i))

print(during)
total = 100
for j in range(1, 10):
    total += (during[j] * 2)

print(total)
print(during[10])
