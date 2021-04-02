from math import sqrt
n = 0
for i in range(101, 200):
    k = int(sqrt(i+1))
    for j in range(2, k+1):
        if i % j == 0:
            break
        else:
            if j == k:
                n += 1
                print(i, j, k)
            continue
print(n)


