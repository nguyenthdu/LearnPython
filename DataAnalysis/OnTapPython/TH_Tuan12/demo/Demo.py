#xem thong tin thu vien
import sys
'''
print("Thong tin int:")
print(sys.int_info)
print("Thong tin float:")
print(sys.float_info)'''
name = input("Nhap vao ten cua ban: ")
tuoi = int(input("Nhap vao tuoi cua ban: "))
luong  = float(input("Nhap vao luong cua ban: "))
print("Xin chao " + name)
print("Ban " + str(tuoi) + " tuoi")
print("Luong cua ban la " + str(luong))
print(type(name))
print(type(tuoi))
print(type(luong))
print('*'*10)#in ra 10 dau *
