#Viet ham giai phuong trinh bac 1\
#TODO: 1d -> 8d
def GiaiPTB1(a,b):
    if a == 0:
        if b == 0:
            print('Vo so nghiem')
        else:
            print('Vo nghiem')
    else:
        print(f'x = {-b/a}')


a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
GiaiPTB1(a,b)
