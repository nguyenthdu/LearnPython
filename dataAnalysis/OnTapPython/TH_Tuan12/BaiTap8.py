def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:# i=5 , i+2=7,
            return False
        i += 6#11,17,24
    return True

def find_primes_and_sum(limit):
    primes = []
    prime_sum = 0
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
            prime_sum += num
    return primes, prime_sum

try:
    n = int(input("Nhập số tự nhiên n: "))
    if n <= 0:
        print("Vui lòng nhập một số tự nhiên lớn hơn 0.")
    else:
        prime_numbers, total_sum = find_primes_and_sum(n)
        print("Các số nguyên tố nhỏ hơn n:", prime_numbers)
        print("Tổng các số nguyên tố nhỏ hơn n:", total_sum)
except ValueError:
    print("Vui lòng nhập một số tự nhiên hợp lệ.")


'''
Sàng Eratosthenes tối ưu hóa việc kiểm tra số nguyên tố bằng cách loại bỏ 
tất cả bội của mỗi số nguyên tố đã tìm thấy. 
Điều này giúp giảm số lượng phép kiểm tra cần thực hiện, 
làm cho giải thuật nhanh hơn đối với các giá trị n lớn.'''
def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return primes

try:
    n = int(input("Nhập số tự nhiên n: "))
    if n <= 0:
        print("Vui lòng nhập một số tự nhiên lớn hơn 0.")
    else:
        prime_numbers = sieve_of_eratosthenes(n - 1)
        prime_sum = sum(prime_numbers)
        print("Các số nguyên tố nhỏ hơn n:", prime_numbers)
        print("Tổng các số nguyên tố nhỏ hơn n:", prime_sum)
except ValueError:
    print("Vui lòng nhập một số tự nhiên hợp lệ.")


