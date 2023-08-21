# TODO: Dùng for in để liệt kê các ký tự trong chuỗi
def LietKeKyTu(str):
    for i in str:
        print(i,end='\t')
print('==============================================')
# TODO: Liệt kê các giá trị có trong 1 danh sách, danh sách được nhập từ bàn phím

def LKDS(n):
    ds = []
    for i in range(0, n):
        ds.append(input(f'Nhap phan tu thu {i + 1}: '))
    for i in ds:
        print(f'ds[{ds.index(i)}] = {i}',end='; ')
def LKSoChan(n):
    ds = []
    for i in range(0,n):
        ds.append(input(f'Nhap vao phan tu thu {i+1}:'))
    for i in ds:
        if int(i)%2==0:
            print(f'ds[{ds.index(i)}]: {i}',end='; ')
def XuLyChuoi(str,text):
    n=0
    for i in range(len(str)):
        if str[i:i+len(text)]==text:#str[i:i+len(text)] là cắt chuỗi str từ vị trí i đến vị trí i+len(text)
            n+=1
            print(f'Vi tri xuat hien cua chuoi {text} la: {i}')
    print('So lan xuat hien cua chuoi la: ', n)
    print(f'Do dai cua chuoi {text} la: ', len(text))
#TODO:========== MAIN ======================================
'''
str = "Hello World"
LietKeKyTu(str)
n = int(input('\nNhập vào số lượng phần tử trong danh sách:'))
LKDS(n)

n = int(input('\nNhập vào số lượng phần tử trong danh sách:'))
LKSoChan(n)

'''
str = 'ab cd ab ca cd ab'
text = 'ab'
XuLyChuoi(str,text)