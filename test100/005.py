num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
num3 = int(input("Number3: "))


num_list1 = [num3, num2, num1]
least = 0


def find_least(a, b):
    if a < b:
        smaller = a
    else:
        smaller = b
    return smaller


least = find_least(num_list1[0], find_least(num_list1[1], num_list1[2]))
print(least)

num_list1.remove(least)
least = find_least(num_list1[0], num_list1[1])
print(least)

num_list1.remove(least)
print(num_list1[0])





# if num1 < num2:
#     if num1 < num3:
#         if num2 < num3:
#             print(num1, num2, num3)
#         else:
#             print(num1, num3, num2)
#     else:
#         print(num3, num1, num2)
# else:  # num1 > num2
#     if num1 < num3:
#         print(num2, num1, num3)
#     else:
#         if num2 < num3:
#             print(num2, num1, num3)
#         else:
#             print(num3, num2, num1)
