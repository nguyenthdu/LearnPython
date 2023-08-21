print('Nhap vao n:')
n = input()

# in ra tong các số từ 0 đến n dùng vòng lặp for
# cách 1
tong = 0
for i in range(0, int(n)+1):
    tong += i
print(f'Cach 1: Tong cac so tu 0 den {n} la: {tong}')

# cách 2 dùng while
tong2 = 0
i2 = 0
while i2 <= int(n):
    tong2 += i2
    i2 += 1
print(f'Cach 2: Tong cac so tu 0 den {n} la: {tong2}')
