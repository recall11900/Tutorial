# 打开文件
# 阅读、写入
# 关闭
# f = open('recood.txt','r+',encoding='utf-8')
# # f.write('hello world~~~~ ,深深的飒爽')
# # f.close()

# #读取文件
# #with.as
# print(f.readline()) 

# f.close()

# 接收用户的输入你，并将用户输入的内容以追加的方式写入文件，
# 直到输入exit或者quit则退出程序，退出的时候显示记录的文件内容

while True:
    mystr = input("请输入信息：")
    if mystr in ['exit', 'quit']:
        with open('recood1.txt', 'r')as f:
            for v in f:
                print(v)
        break
    with open('recood1.txt', 'a+')as f:
        f.writelines(mystr + ' \n')
