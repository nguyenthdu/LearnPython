number = int(input("Nhập một số nguyên có 3 chữ số: "))

# Tách các chữ số
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

# Tính tổng các chữ số
sum_digits = digit1 + digit2 + digit3

print("Tổng các chữ số của", number, "là", sum_digits)
