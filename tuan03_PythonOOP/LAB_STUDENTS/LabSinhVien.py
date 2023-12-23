import matplotlib.pyplot as plt
import os
import SinhVien as sinhvien

menu_options = {
    1: 'Nạp dữ liệu từ file',
    2: 'Thêm sinh viên mới',
    3: 'Hiển thị danh sách sinh viên',
    4: 'Hiển thị thông tin chi tiết của một sinh viên khi biết mã sinh viên',
    5: 'Cập nhật thông tin sinh viên',
    6: 'Xóa sinh viên',
    7: 'Tăng mức tiền học bổng cho sinh viên',
    8: 'Giảm mức tiền học bổng cho sinh viên',
    9: 'Tính tổng số sinh viên trong trường',
    10: 'Tính tổng số tiền học bổng mà trường cần chi trả mỗi học kỳ cho sinh viên',
    11: 'Tính mức tiền học bổng trung bình của sinh viên',
    12: 'Tính độ tuổi trung bình của sinh viên',
    13: 'Tính độ tuổi lớn nhất của sinh viên',
    14: 'Sắp xếp danh sách sinh viên tăng dần theo mức tiền học bổng',
    15: 'Vẽ biểu đồ thể hiện sự tương quan mức tiền học bổng theo độ tuổi của sinh viên',
    16: 'Vẽ biểu đồ so sánh mức tiền học bổng trung bình của các nhóm tuổi: nhỏ hơn 24, từ 18 đến 22, hơn 24 trở lên',
    17: 'Vẽ biểu đồ thể hiện phần trăm mức tiền học bổng theo nhóm tuổi',
    18: 'Vẽ biểu đồ thể hiện phần trăm số sinh viên theo nhóm tuổi',
    19: 'Lưu danh sách sinh viên xuống file dbsv_output.db',
    'Others': 'Kết thúc chương trình'
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

# Khai báo biến lưu trữ các sinh viên
dsSinhVien = []

while (True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input('Nhập tùy chọn: '))
    except:
        print('Nhập sai định dạng. Vui lòng nhập lại !')
        continue
    
    # Nạp dữ liệu từ file
    if userChoice == 1:
        _currentDir = os.getcwd()
        fr = open(_currentDir + '/python tuan 3/LAB_STUDENTS/dbsv_input.db', mode='r', encoding='utf-8')
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            mssv = ds[0]
            ten = ds[1]
            namSinh = int(ds[2])
            tuoi = int(ds[3])
            khoa = ds[4]
            nganh = ds[5]
            hocBong = float(ds[6])
            sv = sinhvien.Student(mssv, ten, namSinh, khoa, nganh, hocBong)
            dsSinhVien.append(sv)
        fr.close()
    
    # Thêm sinh viên mới
    elif userChoice == 2:
        # nhập thông tin
        mssv = input("Nhập mssv: ")
        ten = input("Nhập tên: ")
        namSinh = int(input("Nhập năm sinh: "))
        khoa = input("Nhập khoa: ")
        nganh = input("Nhập ngành: ")
        hocBong = float(input("Nhập số tiền học bổng nhận được: "))
        # tạo và thêm vào cuối danh sách
        sv = sinhvien.Student(mssv, ten, namSinh, khoa, nganh, hocBong)
        dsSinhVien.append(sv)

    # Hiển thị danh sách sinh viên
    elif userChoice == 3:
        for item in dsSinhVien:
            item.display()
    
    # Hiển thị thông tin chi tiết của một sinh viên khi biết mã sinh viên
    elif userChoice == 4:
        # nhập mssv
        maSV = input("Nhập mssv: ")
        ktSV = 0
        for item in dsSinhVien:
            if item.mssv == maSV:
                item.display()
                ktSV = 1
        if ktSV == 0:
            print("Nothing here")

    # Cập nhật thông tin sinh viên
    elif userChoice == 5:
        # nhập mssv
        maSV = input("Nhập mssv: ")
        ktSV = 0
        for item in dsSinhVien:
            if item.mssv == maSV:
                item.display()
                ktSV = 1
        if ktSV == 0:
            print("Nothing here")
        else:
            mssv = input("Nhập mssv: ")
            ten = input("Nhập tên: ")
            namSinh = int(input("Nhập năm sinh: "))
            khoa = input("Nhập khoa: ")
            nganh = input("Nhập ngành: ")
            for item in dsSinhVien:
                if item.mssv == maSV:
                    item.mssv = maSV
                    item.ten = ten
                    item.namSinh = namSinh
                    item.khoa = khoa
                    item.nganh = nganh

# Xóa một sinh viên ra khỏi danh sách
    elif userChoice == 6:
        # nhập mssv
        maSV = input("Nhập mssv: ")
        ktSV = 0
        for item in dsSinhVien:
            if item.mssv == maSV:
                item.display()
                ktSV = 1
        if ktSV == 0:
            print("Nothing here")
        if ktSV == 1:
            for item in dsSinhVien:
                if item.mssv == maSV:
                    dsSinhVien.remove(item)

    # Tăng mức tiền học bổng cho sinh viên
    elif userChoice == 7:
        # nhập mssv
        maSV = input("Nhập mssv: ")
        ktSV = 0
        for item in dsSinhVien:
            if item.mssv == maSV:
                item.display()
                ktSV = 1
        if ktSV == 0:
            print("Nothing here")
        if ktSV == 1:
            hbMoi = float(input("Nhập số tiền học bổng mới nhận được: "))
            for item in dsSinhVien:
                if item.mssv == maSV:
                    item.hocBong += hbMoi

    # Giảm mức tiền học bổng cho sinh viên
    elif userChoice == 8:
        # nhập mssv
        maSV = input("Nhập mssv: ")
        ktSV = 0
        for item in dsSinhVien:
            if item.mssv == maSV:
                item.display()
                ktSV = 1
        if ktSV == 0:
            print("Nothing here")
        if ktSV == 1:
            hbMoi = float(input("Nhập số tiền học bổng mới nhận được: "))
            for item in dsSinhVien:
                if item.mssv == maSV:
                    item.hocBong += hbMoi

    # Tính tổng số sinh viên trong trường và xuất ra màn hình
    elif userChoice == 9:
        print('Tổng số sinh viên trong trường là: ', len(dsSinhVien))
    
    # Tính tổng số tiền học bổng mà trường cần chi trả mỗi học kỳ cho sinh viên 
    elif userChoice == 10:
        # tính tổng số tiền học bổng
        sumScholarship = 0.0
        for item in dsSinhVien:
            sumScholarship = sumScholarship + item.hocBong
        # Xuất ra màn hình kết quả
        print(f'Tổng số tiền học bổng mà trường học cần chi trả mỗi học kỳ cho sinh viên là: {sumScholarship:.2f}')
    
    # Tính số tiền học bổng trung bình của sinh viên (avgScholarship) và xuất ra màn hình
    elif userChoice == 11:
        # tổng số sinh viên
        sumStudents = len(dsSinhVien)
        # tính tổng số tiền học bổng
        for item in dsSinhVien:
            sumScholarships = sumScholarships + item.hocBong
        # tính số tiền học bổng trung bình
        avgScholarship = sumScholarships / sumStudents
        # Xuất ra màn hình kết quả
        print(f'Số tiền học bổng trung bình của sinh viên là: {avgScholarship:.2f}')
    
    # Tính độ tuổi trung bình của sinh viên (avgAge) và xuất ra màn hình
    elif userChoice == 12:
        # tổng số lượng sinh viên
        sumStudents = len(dsSinhVien)
        # tính tổng số tuổi của sinh viên
        sumAge = 0.0
        for item in dsSinhVien:
            sumAge = sumAge + item.tuoi
        # tính độ tuổi trung bình của sinh viên
        avgAge = sumAge / sumStudents
        # Xuất ra màn hình kết quả
        print(f'Độ tuổi trung bình của sinh viên là: {avgAge:.2f}')
    
    # Tính độ tuổi lớn nhất của sinh viên (maxAge) và hiển thị danh sách nhân viên có tuổi lớn nhất
    elif userChoice == 13:
        maxAge = dsSinhVien[0].age
        for item in dsSinhVien:
            if (maxAge < item.tuoi):
                maxAge = item.tuoi
        print(f'Độ tuổi lớn nhất của các sinh viên là: {maxAge}')
        
    # Sắp xếp danh sách sinh viên tăng dần theo mức tiền học bổng
    elif userChoice == 14:
        # tổng số lượng sinh viên
        sumStudents = len(dsSinhVien)
        for i in range(i+1, sumStudents):
            if (dsSinhVien[i].hocBong > dsSinhVien[i].hocBong):
                # hoán vị
                tmp = dsSinhVien[i]
                dsSinhVien[i] = dsSinhVien[j]
                dsSinhVien[j] = tmp
    
    # Vẽ biểu đồ thể hiện sự tương quan mức tiền học bổng theo độ tuổi của sinh viên
    elif userChoice == 15:
        arrTuoi = []
        arrHocBong = []
        for item in dsSinhVien:
            arrTuoi.append(item.tuoi)
            arrHocBong.append(item.hocBong)
        # Vẽ đồ thị
        plt.figure(figsize=(15,5))
        plt.title("Biểu đồ thể hiện sự tương quan mức tiền học bổng theo độ tuổi của sinh viên")
        plt.xlabel("Ox: độ tuổi")
        plt.ylabel("Oy: Mức tiền học bổng")
        plt.plot(arrTuoi, arrHocBong, "go")
        plt.show()

    # Vẽ biểu đồ so sánh mức tiền học bổng trung bình của các nhóm tuổi: nhỏ hơn 24, từ 18 đến 22, hơn 24 trở lên
    elif userChoice == 16:
        arrAgeGroup = ['nhỏ hơn 24', 'từ 18 đến 22', 'lớn hơn 24']
        arrAvgScholarship = [0.0, 0.0, 0.0]
        arrCount = [0.0, 0.0, 0.0]
        for item in dsSinhVien:
            if (item.tuoi < 24):
                arrAvgScholarship[0] += item.hocBong
                arrCount[0] += 1.0
            elif (item.tuoi >= 22 or item.tuoi <= 18):
                arrAvgScholarship[1] += item.hocBong
                arrCount[1] += 1.0
            else:
                arrAvgScholarship[2] += item.hocBong
                arrCount[2] += 1.0
        if (arrCount[0] > 0):
            arrAvgScholarship[0] = arrAvgScholarship[0] / arrCount[0]
        if (arrCount[1] > 0):
            arrAvgScholarship[1] = arrAvgScholarship[1] / arrCount[1]
        if (arrCount[2] > 0):
            arrAvgScholarship[2] = arrAvgScholarship[2] / arrCount[2]
        # Vẽ đồ thị
        plt.bar(arrAgeGroup, arrAvgScholarship, color="green")
        plt.title('Biểu đồ so sánh mức tiền học bổng trung bình của các nhóm tuổi')
        plt.xlabel('Ox: Độ tuổi')
        plt.ylabel('Oy: Mức tiền học bổng trung bình')
        plt.show()
        
    # Vẽ biểu đồ thể hiện phần trăm mức tiền học bổng theo nhóm tuổi
    elif userChoice == 17:
        arrAgeGroup = ['nhỏ hơn 24', 'từ 18 đến 22', 'lớn hơn 24']
        arrAvgScholarship = [0.0, 0.0, 0.0]
        noiBat = [0, 0.2, 0]
        sumStudents = len(dsSinhVien)
        for item in dsSinhVien:
            if (item.tuoi < 24):
                arrAvgScholarship[0] += item.hocBong
            elif (item.tuoi >= 22 or item.tuoi <= 18):
                arrAvgScholarship[1] += item.hocBong
            else:
                arrAvgScholarship[2] += item.hocBong
        if (arrAvgScholarship[0] > 0):
            arrAvgScholarship[0] = arrAvgScholarship[0] / sumStudents
        if (arrAvgScholarship[1] > 0):
            arrAvgScholarship[1] = arrAvgScholarship[1] / sumStudents
        if (arrAvgScholarship[2] > 0):
            arrAvgScholarship[2] = arrAvgScholarship[2] / sumStudents
        # Vẽ đồ thị
        plt.figure(figsize=(10, 5))
        plt.pie(arrAvgScholarship, labels=arrAgeGroup,
                explode=noiBat, shadow=True, startangle=45)
        plt.axis("equal")
        plt.legend(title='Độ tuổi', loc="upper right")
        plt.title('Tỷ lệ phần trăm mức tiền học bổng theo nhóm tuổi')
        plt.show()
    
    # Vẽ biểu đồ thể hiện phần trăm số sinh viên theo nhóm tuổi
    elif userChoice == 18:
        arrAgeGroup = ['nhỏ hơn 24', 'từ 18 đến 22', 'lớn hơn 24']
        arrCount = [0.0, 0.0, 0.0]
        noiBat = [0, 0.2, 0]
        sumStudents = len(dsSinhVien)
        for item in dsSinhVien:
            if (item.tuoi < 35):
                arrCount[0] += 1
            elif (item.tuoi >= 35 or item.tuoi <= 50):
                arrCount[1] += 1
            else:
                arrCount[2] += 1
        if (arrCount[0] > 0):
            arrCount[0] = arrCount[0] / sumStudents
        if (arrCount[1] > 0):
            arrCount[1] = arrCount[1] / sumStudents
        if (arrCount[2] > 0):
            arrCount[2] = arrCount[2] / sumStudents

        # vẽ biểu đồ
        plt.figure(figsize=(10, 5))
        plt.pie(arrCount, labels=arrAgeGroup,
                explode=noiBat, shadow=True, startangle=45)
        plt.axis("equal")
        plt.legend(title='Độ tuổi', loc="upper right")
        plt.title('Tỷ lệ phần trăm tổng số sinh viên theo nhóm tuổi')
        plt.show()
        
    # Lưu danh sách sinh viên xuống file dbsv_output.db
    # Biết rằng mỗi sinh viên là một dòng và các thông tin sinh viên được phân cách bởi dấu '-'
    elif userChoice == 19:
        fw = open(_currentDir + '/python tuan 3/LAB_STUDENTS/dbsv_output.db', mode='r', encoding='utf-8')
        for item in dsSinhVien:
            fw.write(f'{item.mssv}, {item.ten}, {item.namSinh}, {item.tuoi}, {item.khoa}, {item.nganh}, {item.hocBong:.0f}\n')
        fw.close()
        print('Lưu trữ dữ liệu thành công')
    
    else:
        print('Kết thúc chương trình. BYE !')
        break