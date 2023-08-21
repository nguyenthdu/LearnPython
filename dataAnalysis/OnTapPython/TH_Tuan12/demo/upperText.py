
# myCharacter = ['a','b','c']

# myUpper =[x.upper() for x in myCharacter]

# print(myUpper)

# # create arry 1 to 10
# myNumber =[0,1,2,3,4,5,6,7,8,9,10]

# myGreater5 = [x for x in myNumber if x > 5]
# print(myGreater5)
# myPower2 = [x**2 for x in myNumber]
# print(myPower2)
# # print number not /2
# myNotDivide2 = [x for x in myNumber if x%2 != 0]
# print(myNotDivide2)
# # pow number not /2
# myNotDivide2Pow = [x**2 for x in myNumber if x%2 != 0]
# print(myNotDivide2Pow)
#viết hàm tính lập phương của 1 số
def tinhLapPhuong(x):
    return x**3
print("Lập phương của 3 là: ",tinhLapPhuong(3))
# viết bằng lamda
tinhLapPhuong2 = lambda x: x**3
print("Lập phương của 3 là: ",tinhLapPhuong2(3))