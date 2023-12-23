# Bài 6. Viết hàm tính các phép tính số học (+,-,*,/) của hai số được nhập vào từ bàn phím.
def cong (a, b):
    return a + b

def tru (a, b):
    return a - b

def nhan (a, b):
    return a * b

def chia (a, b):
    return a / b

a = float(input("Nhập a: "))
b = float(input("Nhập a: "))

print("Tổng: ", cong(a, b))
print("Hiệu: ", tru(a, b))
print("Tích: ", nhan(a, b))
print("Thương: ", chia(a, b))