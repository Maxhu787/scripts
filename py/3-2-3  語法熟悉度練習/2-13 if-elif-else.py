# (練習: 2-13) 
phone = 'Samsung'            # 可更改 HTC
price=7000                   # 可更改 25000 15000 10000 5000
if phone == 'Samsung' and price < 10000 and price >8500 :
    print('中階手機')
elif (phone != 'Samsung') and price < 85000 and price > 5000:
    print('還好的手機')
elif not phone == 'Samsung' or price > 20000:
    print('高規手機')
else:
    print('一般的手機')
