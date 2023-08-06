jon_snow = ["Jon Snow", "Winterfell", 30]
print(jon_snow)

# Indexing
print(jon_snow[0])

# Length
print(len(jon_snow))
print("=====================")
#TODO: Mở rộng list:
jon_snow1 = ["Jon Snow", "Winterfell", 30]
print(jon_snow1[2])
jon_snow1[2] += 3
print(jon_snow1[2])
print(jon_snow1)
print("=====================")
#TODO: Range
num_seq = range(0, 10)  # A sequence from 0 to 9
num_list = list(num_seq)  # The list() method casts the sequence into a list
print(num_list)

num_seq = range(3, 20, 3)  # A sequence from 3 to 19 with a step of 3
print(list(num_seq))
print("=====================")
#TODO: list trong list
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners)
#TODO:Lập chỉ mục tuần tự 
'''
Để truy cập các phần tử của một danh sách hoặc một chuỗi tồn tại bên trong một danh sách khác, chúng ta có thể sử dụng khái niệm lập chỉ mục tuần tự.

Mỗi cấp độ lập chỉ mục đưa chúng ta đi sâu hơn một bước vào danh sách, cho phép chúng ta truy cập bất kỳ phần tử nào trong một danh sách phức tạp.

Tất cả những gì chúng ta phải làm là chỉ định tất cả các chỉ số theo trình tự:'''
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[0])#2006, "Italy"
print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0])  # Accessing 'S'

#TODO: Gộp list
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
merged_list = part_A + part_B
print(merged_list)
#use extend - thêm list này vào cuối danh sách list khác
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)