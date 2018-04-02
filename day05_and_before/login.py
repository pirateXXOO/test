# Author:Jack
# Date:2018/1/18

# _user = "Jack"
# _pass = "abc123"

# while 1 == 1:
#     username = input("Username: ")
#     password = input("Password: ")
#
#     if username == _user  and  password == _pass :
#         print("Hello! %s"%(username))
#         break
#     else:
#         print("Incorrect username or password.")
#         continue
#
# # for i in range(1,101,2): # 2 步长
# #     print(i)
# # print(range(3))


##########################################################################3
## While practice

# _user="Jack"
# _passwd="123"
#
# username=input("Please input your username: ")
# for i in range(3):
#     password=input("Please input your password:")
#
#     if username == _user and password == _passwd:
#         print("Welcome to GUNDAM!")
#         break
#     else:
#         continue
# else:
#     print("Invalid username or password.")

#######################################################
## Flag

for  i in range(10):
    if i < 5 :
        print(i)
    else:
        for j in range(20):
            print("Layer2: ",j)
            if j > 10 :
                exit_flag = True
                break
        if exit_flag:
            break



