"""
获取系统时间
"""
import time

now_time= time.localtime()

mday=now_time.tm_mday#当月天数

wday= now_time.tm_wday#星期几的天数，取值0-6

result='现在是%s年%s月，并且是当月的'%(now_time.tm_year,now_time.tm_mon)

if mday<=15:
	result +='上旬,'
else:
	result+='下旬,'

if wday==0:
	result+="而且是星期一哦."
elif wday==1:
	result+="而且是星期二哦."
elif wday==2:
	result+="而且是星期三哦."
elif wday==3:
	result+="而且是星期四哦."
elif wday==4:
	result+="而且是星期五哦."
elif wday==5:
	result+="而且是星期六哦."
elif wday==6:
	result+="而且是星期天哦."
else:
	result +="hahh"

print(result)