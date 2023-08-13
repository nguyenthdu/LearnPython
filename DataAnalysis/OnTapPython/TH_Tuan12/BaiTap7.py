def SoNT(n):
    if n==2 or n==3:
        print(f'{n} la so nguyen to')
    else:
        for i in range(2,n-1):
            if n%i==0:
                print(f'{n} khong phai la so nguyen to!!!')
                break
            else:
                print(f'{n} la so nguyen to!!!')
            break


SoNT(17)