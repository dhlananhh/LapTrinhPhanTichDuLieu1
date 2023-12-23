# Bài 3: Các cấu trúc điều khiển

# Câu 1. Viết chương trình giải phương trình bậc 1 ax + b = 0, trong đó, a, b là các số thưc được nhập từ bàn phím
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

if a > 0 or a < 0:
    x = -b/a
    print("Nghiệm của phương trình là: ", x)
else:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")

# Câu 2. Tính tổng s = 0 + 1 + ... + n, trong đó n là số tự nhiên nhập từ bàn phím. Yêu cầu viết bằng for…range, while.
# Dùng for...range
n = int(input("Nhập n: "))
s = 0
for i in range(n+1):
    s += i
print("Tổng các số từ 1 đến", n, "là", s)

# Dùng while
n = int(input("Nhập n: "))
i = 0
s = 0

while i <= n:
    s += i
    i += 1
print("Tổng các số từ 1 đến", n, "là", s)

# 3. Dùng for...in:
# a> Liệt kê danh sách các ký tự có trong 1 từ, với từ được nhập vào từ bàn phím
# Liệt kê danh sách các ký tự có trong 1 từ, với từ được nhập vào từ bàn phím
# Ví dụ: Nhập vào từ "Hello", kết quả là: H, e, l, o
def non_duplicate_characters (str):
    result = ""
    for char in str:
        if char not in result:
            result += char
    return result        

str = input("Nhập vào một chuỗi: ")
print("DS các ký tự có trong từ vừa nhập là: ", non_duplicate_characters(str))

# b> Liệt kê danh sách các giá trị có trong 1 danh sách, với danh sách được nhập vào từ bàn phím.
# Liệt kê danh sách các giá trị có trong 1 danh sách, với danh sách được nhập vào từ bàn phím.
try:
    list = []
    while True:
        list.append(int(input()))
except:
    print(list)

# c> In ra màn hình các số chẵn của 1 mảng được nhập vào từ bàn phím.
# In ra màn hình các số chẵn của 1 mảng được nhập vào từ bàn phím.
list = []

try:
    while True:
        list.append(int(input()))
except:
    for num in list:
        if num % 2 == 0:
            print(num, end = " ")

# d> Nhập vào một chuỗi ký tự, nhập ký tự cần tìm. In ra ký tự đó xuất hiện bao nhiêu lần tại vị trí nào và cho biết chiều dài chuỗi ký tự nhập vào.
# Nhập vào một chuỗi ký tự, nhập ký tự cần tìm. In ra ký tự đó xuất hiện bao nhiêu lần tại vị trí nào và cho biết chiều dài chuỗi ký tự nhập vào.
# Ví dụ: Chuỗi ký tự nhập vào là: “Hello world”, ký tự cần tìm là “o”.
# Ký tự “o” xuất hiện 2 lần tại vị trí 4 và 7.
s = input("Nhập vào một chuỗi ký tự: ")
k = input("Nhập ký tự cần tìm: ")
print("Chiều dài chuỗi ký tự nhập vào là: ", len(s))
print("Ký tự", k, "xuất hiện", s.count(k), "lần tại vị trí", end=" ")
for i in range(len(s)):
    if s[i] == k:
        print(i, end=" ")
