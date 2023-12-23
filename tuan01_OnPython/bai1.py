# Bài 1: Viết các lệnh xuất các biến

# Kiểu dữ liệu số
x = 10 #Python hiểu đây là số nguyên
y = 10.5 #Python hiểu đây là số thực
z = 5 #Python hiểu đây là số nguyên
t = x + z #Python hiểu t là số nguyên
t = x + y #Python hiểu t là số thực

# Kết luận
# số nguyên (+,-,*,/) số nguyên = số nguyên
# số nguyên (+,-,*,/) số thực = số thực
# số thực (+,-,*,/) số thực = số thực

# Kiểu thực
a = 1.4
a = 31.4e-10
# Kiểu số phức: a +(-)ib
z = 2 + 7j
# Kiểu số dạng bát phân (8), thập lục phân (16) hoặc nhị phân (2)
x = 0b100100
y = 0xf400
# True và False
u = True # u -> 1
v = False # v -> 0
# Kiểu dữ liệu chuỗi
a = "Hello" # Python hiểu a là kiểu chuỗi
print(a)
b = 'World' # Python hiểu b là kiểu chuỗi
print(b)
# Sử dụng \n để xuống dòng
print("Python programming \n for Data Analysis")
# Sử dụng f để hiện thị giá trị
print(f'Giá trị biến a là: {a}')
print("Giá trị biến a là:",a)