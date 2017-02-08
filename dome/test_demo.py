"""
项目描述
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：isalpha方法判断是否是字母，isspace方法判断是否是空格，isdigit方法判断是否是数字
"""
#声明字符
str_test='asdasdas . daadasd ,das1231'
sum=0
kongge=0
shuzi=0
#result='总共有%s个字母,%s个空格，%s个数字'%()
# for m in str_test:
# 	if m.isalpha()==True:
# 		sum+=1
# 		#print('总共有%s字母'%(sum))
# 	if m.isspace()==True:
# 		kongge+=1
# 		#print('总共有%s个空格'%(kongge))
# 	if m.isdigit()==True:
# 		shuzi+=1
# 		#print('总共有%s个数字'%(shuzi))
# print('总共有%s个字母,%s个空格，%s个数字'%(sum,kongge,shuzi)) 

for m in str_test:
	if m.isalpha()==True:
		sum+=1
	elif m.isspace()==True:
		kongge+=1
	elif m.isdigit()==True:
		shuzi+=1
print('总共有%s个字母,%s个空格，%s个数字'%(sum,kongge,shuzi))