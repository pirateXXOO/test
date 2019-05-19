# Author:Jack
# Date:2018/8/25

login_status = False

def check_login_status(func):
    if login_status ==  False:
        def get_account(account_type):
            get = {}
            with open(account_type,'r') as account:
                for line in account.readlines():
                    line = line.strip()
                    if not len(line):
                        continue
                    get[line.split(':')[0]] = line.split(':')[1]

            def check_account():
                username = input("Please input your username: ")
                password = input("Please input your password: ")
                if username == get['username'] and password == get['passowrd'] :
                    login_status = True
                    func
                else:
                    print('Wrong username or password! ')

    else:
        pass
    return check_login_status

@check_login_status(account_type='jdaccount')
def home():
    print('nihao')

@check_login_status(account_type='jraccount')
def finance():
    print('nihao')

@check_login_status(account_type='wechataccount')
def book():
    print('nihao')


