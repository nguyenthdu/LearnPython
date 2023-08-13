def my_print_function():  # No parameters
    print("This")
    print("is")
    print("A")
    print("function")
# Function ended
# Calling the function in the program multiple times
def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)


num = 20


def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return n

num_list = [10, 20, 30, 40]
print(num_list)


def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10


multiply_by_10(num_list)
print(num_list)  # The contents of the list have been changed