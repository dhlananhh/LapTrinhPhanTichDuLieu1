"""
Bài 9: 
    Hãy viết chương trình đọc file in.txt 
    và hiển thị ra màn hình nội dung từng dòng trong file đó
"""

file = open('../data/in.txt')
flines = file.readlines()

for line in flines:
    print(line)
file.close()