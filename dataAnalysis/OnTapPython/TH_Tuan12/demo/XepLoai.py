#TODO: 1d----
#Nhap vao diem trung binh
diemTB = float(input("Nhap diem trung binh: "))
#Xep loai
if diemTB>=9:
    print("Loai gioi")
elif diemTB>=7:
    print("Loai kha")
elif diemTB>=5:
    print("Loai trung binh")
else:
    print("Loai yeu")


#Phep gan

a = 5
b = 6
if a!=b:
    c = 110
else:
    c = 100
print(c)
# 1 cach khac
c = 110 if a!=b else 100

#TODO: 1d -> 5d + 1d
#for n in range(10) ket qua la: 0 1 2 3 4 5 6 7 8 9
#for n in range(1,10) ket qua la: 1 2 3 4 5 6 7 8 9
#for n in range(1,10,2) ket qua la: 1 3 5 7 9
#for n in range(10,0,-1) ket qua la: 10 9 8 7 6 5 4 3 2 1
#for n in range(10,0,-2) ket qua la: 10 8 6 4 2
#for n in range(2,11,2) ket qua la: 2 4 6 8 10