# 9-6-2-1 天干地支查詢歲次及生肖
'''
天干地支對照表:
-----------------------------
天干 
 1  2  3  4  5  6  7  8  9 10
甲 乙 丙 丁 戊 己 庚 辛 壬 癸
-----------------------------------
地支
 1  2  3  4  5  6  7  8  9 10 11 12
子 丑 寅 卯 辰 巳 午 未 申 酉 戌 亥
-----------------------------------
60年一甲子

生肖 西元  歲次 
  鼠 1924  甲子 
  鼠 1984  甲子 

從甲子年開始，通過天干和地支循環組合，最終到下一個甲子年正好是60年，如何循環組合呢？比如2017年是丁酉年，那2018年就是戊戌年，2019年就是己亥年，依次類推，因為天干是10個，地支是12個，所以天干和地支循環組合一次，天干要比地支多組合兩位，這樣10個天干總共跟12個地支循環組合了5次，5乘以12正好是60，也就是60年；

原文網址：https://kknews.cc/culture/reamoln.html
'''

strA="甲乙丙丁戊己庚辛壬癸"
strB="子丑寅卯辰巳午未申酉戌亥"
strC="鼠牛虎兔龍蛇馬羊猴雞狗豬"

y=int(input("西元 (>2) = "))
yy= (y-4) % 60

a=yy % 10; b= yy % 12

print("歲次: ",strA[a:a+1],strB[b:b+1])
print("生肖: ",strC[b:b+1])
