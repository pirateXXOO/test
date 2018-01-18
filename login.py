# Author:Jack
# Date:2018/1/18

_user = "Jack"
_pass = "abc123"

while 1 == 1:
    username = input("Username: ")
    password = input("Password: ")

    if username == _user  and  password == _pass :
        print("Hello! %s"%(username))
        break
    else:
        print("Incorrect username or password.")
        continue

# for i in range(1,101,2): # 2 步长
#     print(i)
# print(range(3))
