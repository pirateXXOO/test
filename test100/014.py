# num = int(input('Number: '))

# i = 2

# def find_little(a):
#     while i not in [1]:
#         if a % i == 0:
#             a = a/i
#             print(i)
#             find_little(a)
#         else:
#


def find_little(num):
    print('{} ='.format(num), end=" ")
    # if num in [1]:
    #     print('{}'.format(num))
    while num not in [1]:
        for index in range(2, num+1):
            if num % index == 0:
                num = num // index
                if num == 1:
                    print(index)
                else:
                    print('{} *'.format(index), end=" ")
                break


find_little(90)