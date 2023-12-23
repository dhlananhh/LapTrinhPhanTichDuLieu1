# Bài 7. Hãy nhập một số tự nhiên từ bàn phím sau đó, xuất màn hình thông báo số đó có phải là số nguyên tố hay không
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
    
x = int(input("Nhập giá trị x: "))
print(isPrime(x))
