"""
异常
try:
    <语句>
    except
"""

try:
    int("dsdasda")
    print(dasd)
except ValueError as e:
    print('出现异常',e)
else:
    print('没有出现异常情况')
finally:
    print('始终执行finally块代码！！')