from pip._vendor.distlib.compat import raw_input

i = int(raw_input('净利润：'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += (i-arr[idx])*rat[idx]
        print("第", 6-idx, "部分", (i-arr[idx]), "提成率：", rat[idx], "提成：", (i-arr[idx])*rat[idx])
        i = arr[idx]
print(r)
