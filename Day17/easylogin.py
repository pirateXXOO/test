# Author:Jack
# Date:2019/5/18
import time
account = open('account', 'r', encoding='Utf-8')
# real_username = account.readline().strip()
# real_password = account.readline().strip()
real_username = account.readline().strip().split(':')[1]
real_password = account.readline().strip().split(':')[1]
account.close()
print(real_username)
print(real_password)
login_status = False


def timecal(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        print('Time used : %s' % (endtime - starttime))
    return wrapper


@timecal
def login():
    def output_login_error():
        print("Username or Password error !")
        print(login_status)

    def print_welcome():
        print("Welcome !")
        login_status = True
        print(login_status)

    username = input("Please input your username: ")
    password = input("Please input your password: ")

    if username == real_username and password == real_password:
        print_welcome()
    else:
        output_login_error()


login()
