random_set = {"Educative", 1408, 3.142,
              (True, False)}
print(random_set)
print(len(random_set))  # Length of the set
# cách khai báo khác
empty_set = set()
print(empty_set)

random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)
print("======================")
#TODO: Thêm vào set()
empty_set = set()
print(empty_set)

empty_set.add(1)
print(empty_set)

empty_set.update([2, 3, 4, 5, 6])
print(empty_set)
#TODO: xóa
print("===========================")
random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

random_set.discard(1408)
print(random_set)

random_set.remove((True, False))
print(random_set)

#TODO: Lặp set()
odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

print(unordered_set)

for num in unordered_set:
    if(not num % 2 == 0):
        odd_list.append(num)

print(odd_list)