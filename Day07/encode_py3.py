# Author:Jack
# Date:2018/6/3
import  sys
print(sys.getdefaultencoding())
s = "特斯拉"
print(s)
s_to_gbk=s.encode("gbk")
print(s_to_gbk)
print(s_to_gbk.decode("gbk"))