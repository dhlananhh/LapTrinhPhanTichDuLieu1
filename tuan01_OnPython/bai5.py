# Bài 5. Viết hàm tính giá trị bình phương của một số Sau đó, gọi hàm.
def square (num):
    return num ** 2

x = int(input("Nhập giá trị x: "))
print("Bình phương của ", x, " là: ", square(x))