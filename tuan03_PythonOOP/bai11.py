"""
Bài 11:
    Đọc file dữ liệu num_input.csv 
    Hãy lưu trữ các số trong file vào chương trình. 
    Sau đó, xuất ra màn hình tổng của các số trong file.
"""

import os
import sys
import numpy as np

__file__ = "../data/num_input.csv"
_currentDir = os.path.dirname(os.path.realpath(__file__))
_parentDir = os.path.dirname(_currentDir)
sys.path.append(_parentDir)

file = open(__file__, "r")
flines = file.readlines()

list = []

for line in flines:
    list = list + line.strip().split(",")

list.remove('')
print(list)

list = [int(i) for i in list]
print(list)

sum = 0
for i in list:
    sum += i
print("\nSum = ", sum)