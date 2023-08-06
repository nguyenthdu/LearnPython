nums = [10, 20, 30, 40, 50]
nums_double = []

for n in nums:
    nums_double.append(n * 2)

print(nums)
print(nums_double)

print("========================")
nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums]

print(nums)
print(nums_double)

print("=======================================")
# Thêm điều kiện nếu chia hết cho 4 thì nhân đôi
nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums if n % 4 == 0]

print(nums)
print(nums_double)
print("================================")
# Multiple list
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)