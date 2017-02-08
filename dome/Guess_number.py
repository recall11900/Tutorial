import random

"""项目描述
在视频课程猜数字游戏的基础增加一些有趣的功能和效果：
1、计算机在所设定的范围内随机生成一个数，作为被猜数。
2、每猜一个数，计算机首先判断在不在所设定的范围：如果不在，提示用户重新输入；如果在，提示用户新的数字范围。
3、增加有趣的互动语句，请尽情上，发挥吧。
"""


# d定义函数，默认参数
#  生成随机数
# 有五次机会猜数
# 获取用户数
# 判断随机数和用户数是否一致，如果一致中五百万大奖，如果不一致还有四次机会猜
# 用户可以中途退出猜数 输入exit退出程序
def guess(number=10):
    cishu = 5
    while cishu <= 5:
        input_test = int(input('********欢迎来到猜数字游戏******' + '\n''请输入你猜的数字: '))
        sun = random.randrange(number)
        cishu -= 1
        if sun == input_test:
            print('恭喜猜中了,获得五百万大奖！！！')
            break
        elif cishu < 1:
            print('已经没有机会了')
            break
        else:
            print('你猜错了，还有%s次机会，加油！！！' % cishu)
            print('正确的数是%d' % sun)


# 接收用户输入数据
guess()
