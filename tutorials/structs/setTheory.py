#TODO: Union - Hợp
'''
Hợp của hai tập hợp là tập hợp tất cả các phần tử duy nhất của cả hai tập hợp.
Trong Python, phép hợp có thể được thực hiện bằng cách sử dụng toán tử đường ống |hoặc union()phương thức:

'''
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

print("====================")
#TODO: Intersection - Giao
set_C = {1, 2, 3, 4}
set_D = {2, 8, 4, 16}

print(set_C & set_D)
print(set_C.intersection(set_D))
print(set_D.intersection(set_C))
#TODO: Difference  - khác nhau
print("=========================")
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}


print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))