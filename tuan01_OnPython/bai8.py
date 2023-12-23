"""
Bài 8. Hãy nhập từ bàn phím số tự nhiên n và xuất ra màn hình:
    1. Các số nguyên tố nhỏ hơn n
    2. Xuất ra tổng các số nguyên tố nhỏ hơn n
"""

def isPrime (n):
    if (n < 0):
        return False
    elif (n == 0):
        return False
    elif (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for i in range(2, n):
            if (n % i == 0):
                return False
        return True
    
arr = []
n = int(input("Nhập n: "))
sum = 0
i = 0

for i in range(n):
    if (isPrime(i) == True):
        sum += i
        arr.append(i)

print("1. Các số nguyên tố nhỏ hơn n: ", arr)
print("2. Tổng các số nguyên tố nhỏ hơn n: ", sum)