# Bài 2: Các kiểu dữ liệu List, Tuple

# Kiểu dữ liệu danh sách: LIST
# Đây kiểu dữ liệu có khả năng chứa nhiều phần tử khác nhau
# kể cả khác kiểu dữ liệu
listA = ['red',100,'blue',5.5,"yellow",2+4j]
# Có đánh chỉ chỉ số dương lẫn âm
# listA đánh chỉ số dương: 0,1,2,3,4,5
# listA đánh chỉ số âm: -6,-5,-4,-3,-2,-1
print(listA[2])
print(listA[-2])
# Kết quả trả về của việc lấy theo một dãy các
# phần tử theo chỉ sô
# trong danh sách cũng là danh sách
# --> Cái này cũng được gọi là kỹ thuật SLICE
subListA = listA[2:5]
print(subListA)
print(subListA[1])
print(listA[1:-2])
# Đếm số lượng phần tử của danh sách
soluongpt = len(listA)
print(soluongpt)
print(len(listA))
# Lấy phần tử cuối cùng trong list
print(listA[-1]) # Lấy theo chỉ số âm
print(listA[soluongpt-1]) # Lấy theo chỉ số dương