#TODO: Thêm 1 phần tử vào list sử dụng append()
num_list = []  # Empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)
# Thêm 1 phần tử vào 1 địa điểm cụ thể - aList.insert(index, newElement)
num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
print(num_list)
print("============== THÊM 1 PHẦN TỪ VÀO CHUỖI ==================")
#TODO: Xóa 1 phần tử sử dụng pop()
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)
print("=============== XÓA 1 PHẦN TỬ KHỎI CHUỖI ================")
# Xóa 1 giá trị cụ thể sử dụng hàm remove()
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
print(houses)
houses.remove("Ravenclaw")
print(houses)

# For nested lists
populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)
print("=============== CẮT CHUỖI ================")
#TODO: Cắt list
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])
# TÌM GIÁ TRỊ TRONG CHUỖI
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities)
print("Moscow" not in cities)

#TODO: SẮP XẾP CHUỖI
num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)