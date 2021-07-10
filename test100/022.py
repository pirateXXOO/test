#!/usr/bin/python
# -*- coding = UTF-8 -*-

top = ['a', 'b', 'c']
bottom = ['x', 'y', 'z']
test={}
for i in top:
    for j in bottom:
        print(i, j)
        bottom.remove(j)

        # test[i] = j
        #
        # if i == 'a' and j == 'x':
        #     continue
        # elif i == 'c' and (j == 'x' or j == 'z'):
        #     continue
        # else:
        #     print(i, j)
        #     bottom.remove(j)
        #     break
