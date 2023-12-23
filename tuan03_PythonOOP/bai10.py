"""
Bài 10:
    Hãy viết chương trình xuất ra file out.txt các số chẵn nhỏ số n được nhập từ bàn phím. 
    Biết rằng mỗi dòng thì lưu 1 số
"""
# Input: 10
# Output: 2 4 6 8 10

import os
import sys

__file__ = "../data/out.txt"
_currentDir = os.path.dirname(os.path.realpath(__file__))
_parentDir = os.path.dirname(_currentDir)
sys.path.append(_parentDir)

n = int(input("Nhập số n: "))
fw = open("../data/out.txt", "w")
for i in range(1, n+1):
    if i % 2 == 0:
        fw.write(str(i) + "\n")
fw.close()
