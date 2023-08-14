#TODO: 1d->7d
tong = 0
#tinh tong so le tu 1 den 15. 3 va 11 khong tinh

for i in range(1,16):
    if i%2!=0:
        if i==3 or i == 11:
            continue
        tong += i


print("Tong la: ", tong)