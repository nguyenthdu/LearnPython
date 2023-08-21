# length = float(input("Nhập chiều dài: "))
# width = float(input("Nhập chiều rộng: "))

# def tinhDienTich(length,width):
#     return length*width
# def tinhChuVi(length,width):
#     return (length+width)*2
# print("Chu vi hình chữ nhật là: ",tinhChuVi(length,width))
# print("Diện tích hình chữ nhật là: ",tinhDienTich(length,width))
# viết theo hướng đối tượng
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def tinhDienTich(self):
        return self.length*self.width
    def tinhChuVi(self):
        return (self.length+self.width)*2
    def __str__(self):
        return f"Chiều dài: {self.length}, Chiều rộng: {self.width}"
    
# def main():
#     length = float(input("Nhập chiều dài: "))
#     width = float(input("Nhập chiều rộng: "))
#     rectangle = Rectangle(length,width)
#     print(rectangle)
#     print("Chu vi hình chữ nhật là: ",rectangle.tinhChuVi())
#     #chỉ lấy 2 số thập phân ở kết quả:
#     print("Diện tích hình chữ nhật là: ",round(rectangle.tinhDienTich(),2))

# main()