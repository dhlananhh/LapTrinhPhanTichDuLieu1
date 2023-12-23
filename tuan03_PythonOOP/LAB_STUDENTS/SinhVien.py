class Student:
    def __init__(self, mssv, ten, namSinh, tuoi, khoa, nganh, hocBong):
        self.mssv = mssv
        self.ten = ten
        self.namSinh = namSinh
        self.tuoi = tuoi
        self.khoa = khoa
        self.nganh = nganh
        self.hocBong = hocBong
    def tangHocBong (self, soTien):
        if soTien > 0:
            kq = self.hocBong + soTien
    def giamHocBong (self, soTien):
        if soTien > 0:
            kq = self.hocBong - soTien
    def display (self):
        print(f'mssv: {self.mssv}, ten: {self.ten}, namSinh: {self.namSinh}, khoa: {self.khoa}, nganh: {self.nganh}, hocBong: {self.hocBong}\n')