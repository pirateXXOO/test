flist = []

num = int(input("length of list: "))

if num == 1:
    flist.append(1)
elif num == 2:
    flist = [1, 1]
else:
    flist = [1, 1]
    for i in range(2, num):
        flist.append(flist[i-2]+flist[i-1])

print(flist)

