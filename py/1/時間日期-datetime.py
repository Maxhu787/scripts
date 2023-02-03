import time;        # 引入time 模組

localtime = time.localtime(time.time())
print ("本地時間: :", localtime)


# 格式化成 2018-11-24 11:28:31 格式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
# 格式化成 Sat Nov 24 11:28:31 2018 格式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) )
# 將格式字符串轉換為時間戳 ， 這種格式目前少用
a = "Sat Nov 24 11:30:06 2018"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

import calendar     # 引入calendar 模組
 
cal = calendar.month(2019, 1)
print ("以下輸出2019年1月份的日曆:")
print ( cal )

import datetime      # 引入datetime 模組
i = datetime.datetime.now()
print ("當前的日期和時間是 %s" % i)
print ("ISO格式的日期和時間是 %s" % i.isoformat() )
print ("當前的年份是 %s" %i.year)
print ("當前的月份是 %s" %i.month)
print ("當前的日期是 %s" %i.day)
print ("dd/mm/yyyy 格式是 %s/%s/%s" % (i.day, i.month, i.year) )
print ("當前小時是 %s" %i.hour)
print ("當前分鐘是 %s" %i.minute)
print ("當前秒是 %s" %i.second)
