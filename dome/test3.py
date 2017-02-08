#while 循环
#while 表达式：
#	满足条件执行
#else：
#	不满足执行
i=0
mystr='woaini,nihaiaiwoma'	
while  i<len(mystr):
	print(mystr[i])
	i+=1
else:
	print('执行完成')

"""
for循环
"""

for i in mystr:
	print(i,'')

#使用while和for分别完成从1累加到100求奇数
num=1
sum=0
while num<=100:
	if num%2!=0:
	   sum+=num
	num+=1
print(sum)