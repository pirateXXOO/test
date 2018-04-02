'''

age_of_princal = 56
guess_age = int(input(">>:"))

if guess_age == age_of_princal:
    print("Right")
elif guess_age > age_of_princal:
    print("Bigger")
else:
    print(Smaller")
'''
'''
num = 1
SUM = 0
while num < 100:
    if num % 2 == 0:
        SUM += num
    num += 1
print(SUM)
'''

'''
a = 1
b = 1
while a <= b :
    print(str(a)+ "x" str(b)+ "=" str(a*b) end="\t")
    b += 1
'''
'''
a = 1
b = 4
while a < b:
    print("*",end='')
    a += 1
    if a == b:
        a = 1
        b -= 1
        print()
        continue

'''
'''
a = 1
b = 1
while a <= b:
    print("*",end='')
    a += 1
    if a > b:
        print()
        a = 1
        b += 1
        if b > 4:
            break
        continue
'''
'''
a = 1
b = 1
while a <= b:
    print(str(a) + "x" + str(b) + "=" + str(a*b) ,end='\t' )
    a += 1
    if a > b:
        if b == 9:
            break
        print()
        a = 1
        b += 1
        continue
'''

msg = '''
    nihao wo shi wangshuai
    woshi wangshuai
'''

print(msg)


