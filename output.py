# Author:Jack
# Date:2018/1/18

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = int(input("Salary:"))

# if salary.isdigit(): # 判断salary是否类似数字
#     salary = int(salary)
# else:
# #    print("Salary must input digit!")
#     exit("Salary must input digit!")

print(name,age,job,salary)


# %s string
# %d digit
# %f float

msg = '''
--------- info of %s ----------
Name : %s 
Age  : %d
Job  : %s
Salary: %f
You will be retired in %s years old
------------- end -------------
'''% (name,name,age,job,salary,65-age)

print(msg)
