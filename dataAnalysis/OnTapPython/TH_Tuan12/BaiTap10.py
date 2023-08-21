#Hãy viết chương trình xuất ra file out.txt các số chẵn
# nhỏ số n được nhập từ bàn phím.
# Biết rằng mỗi dòng thì lưu 1 số
n = int(input("Nhập số n: "))
with open('file/out.txt','w') as f:
     for i in range(1,n+1):
         if i%2==0:
             f.write(str(i)+'\n')
