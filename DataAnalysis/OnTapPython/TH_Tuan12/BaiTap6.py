#1d
def calculate(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Không thể chia cho 0"
    else:
        return "Phép tính không hợp lệ"

# Nhập phép tính và hai số từ bàn phím
operation = input("Chon phép tính (+, -, *, /): ")
number1 = float(input("Nhập số thứ nhất: "))
number2 = float(input("Nhập số thứ hai: "))

# Tính kết quả và in ra
result = calculate(operation, number1, number2)
print("Kết quả:", result)
