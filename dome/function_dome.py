"""
学会自定义函数
def 函数名(参数1，参数2.....)
	函数代码

参数、参数默认值
"""
#声明函数，及调用
def myfunc(age,name='很好',*args, **kwargs):#默认值
	print('现在学习函数,%s'%name)
	print(args)
	print(kwargs)
	return age,name
test=myfunc(20)
print(test)函数