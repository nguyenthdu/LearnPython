


sodien = int(input("Nhập số điện: "))
if sodien <= 100:
    print("Số tiền điện là: ",sodien*2000)
else:
    print("Số tiền điện là: ",100*2000+(2000*(sodien-100))
          +100*(sodien-100)
          +100*(sodien-100-1))