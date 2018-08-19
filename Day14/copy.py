# Author:Jack
# Date:2018/7/29

# s=[1,'alex','alvin']
# s1=[1,'alex','alvin']
# s1[0]=2
# print(s)
# print(s1)
# s=[[1,2],'alex','alvin']
# s2=s.copy()
# s2[0]=3
# print(s)
# print(s2)
# s3=s.copy()
# s3[1]='lining'
# print(s3)
#
# s3[0][1]=3
# print(s3)
# print(s)
import copy

husband = ["xiaohu",123,[15000,9000]]

wife = husband.copy()
wife[0]="xiaopang"
wife[1]=345

#xiaosan = copy.copy() # shallow copy
#xiaosan = copy.deepcopy(husband)
# xiaosan[0]="jinxin"
# xiaosan[1]=789
#
# xiaosan[2][1] -= 1999
# print(xiaosan)
# #husband[2][1]-=3000

print(wife)