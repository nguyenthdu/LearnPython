def StrBool(s):
    return s.lower() in ("yes", "true", "t", "1")

print("Nhap vao bool:")
x = StrBool(input())
print("Ban nhap kieu: " ,x)
print("Kieu cua x la: ",type(x))