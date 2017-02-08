#格式化字符串
h="%s,你好，我是%s,我今年%s"%('张三','lll','20')
print(h)

#声明列表
dome=['zhangsan','lisi','wanwu']

#往列表添加元素
dome.append('wanmazi')

#删除列表元素
del dome[0]

#删除指定元素
dome.remove('lisi')

#列表推导式

b='hello world'
c=[i for i in b]

#声明元组
ad=(1,2,3,)

#字典Dict,字典就是一个容器
#字典声明
dict_a=dict()
bd={0:'22','b':100}
#访问字典值
print(bd['b'])
#修改字典中的值
bd['b']=200

#增加字典中的值
bd['c']='haha'
print(bd['c'])

print(len(bd))

print(dome)
print(c)

#声明集合
set_test={1,2,3,3,4,5,5,}


#集合增加元素
set_test.add('dds')


#删除集合中元素
set_test.remove('dds')
print(set_test)

#判断摸个元素是否在集合中存在
print(12 in set_test)

#集合的交集、合集.查找其他资料
#

#切片
val='nizui jin hao ma'
#slice(起始位置，截止位置，步长)
s=slice(1,5,2)
print(val[s])
print(val[1:6])

#import导入库，from import导入具体 