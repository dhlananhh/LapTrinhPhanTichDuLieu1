# Bài 16: Hãy tạo danh sách myEvenSquare là các bình phương các số chẵn trong myNumber

myNumber = [0,1,2,3,4,5,6,7,8,9,10]
myEven = [x for x in myNumber if x % 2 == 0]
myEvenSquare = [y*y for y in myEven]
print(myEvenSquare)