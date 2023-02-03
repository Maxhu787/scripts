'''
正五邊形面積 = 10個直角三角形面積
= 10 x 直角三角形面積 = 10 x ( sin(36o) × cos(36o))/2
= 5 × r × sin θ × r × cos θ ( r = 外接圓半徑 ， θ = 180/5=36o )
= 5 × r × sin(36o) × r × cos(36o) ( 假設 圓半徑  r=1 )
'''
import math
print(math.pi)

area=5 * 1 * math.sin(36*math.pi/180) * math.cos(36*math.pi/180)

print(area)

