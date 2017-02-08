list1=['a','b','c']
list2=[1,2,3]

new_list=[]

for m in list1:
	for n in list2:
		if n==3:
			break#跳出for循环
			continue#跳出当前循环
		new_list.append([m,n])
print(new_list)