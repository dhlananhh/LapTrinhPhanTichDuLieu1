import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import random
# import DuLieuTuyenSinhDaiHoc.ipynb as DLTSDH


menu_options = {
    1: 'Đọc File với các file trong thư mục dữ liệu. Ứng với mỗi file sinh viên thực hiện các câu sau. Hiển thị toàn bộ dữ liệu của file dữ liệu đã đọc',  
    2: 'Đọc file với chỉ định không có header, dòng header của chúng ta đã biến thành 1 bản ghi dữ liệu. Hiển thị toàn bộ dữ liệu của file dữ liệu đã đọc',
    3: 'Đọc File với các tuỳ chọn mặc định. Hiển thị 5 dòng dữ liệu đầu tiên',
    4: 'Đọc File với các tuỳ chọn mặc định. Hiển thị 5 dòng dữ liệu cuối cùng',
    5: 'Chuyển kiểu dữ liệu cho 1 cột nào đó',
    6: 'Xem chiều dài của DataFrame',
    7: 'Xem thông tin DataFrame',
    8: 'Xem kích thước của DataFrame',
    9: 'Hiển thị dữ liệu của cột thứ 3',
    10:	'Hiển thị dữ liệu của cột 1,2,3,5,6',
    11:	'Hiển thị 5 dòng dữ liệu đầu tiên gồm các cột 1,2,3,5,6',
    12:	'Hiển thị 5 dòng dữ liệu đầu tiên theo chỉ số',
    13:	'Hiển thị 5 dòng dữ liệu đầu tiên theo chỉ số gồm các cột 1,2,3,5,6',
    14:	'Loại bỏ các dòng trùng nhau',
    15:	'Loại bỏ các dòng trống có dữ liệu của 1 cột là trống',
    16:	'Loại bỏ các dòng của 1 cột có giá trị là không biết ("Unknown") ',
    17:	'Lấy dữ liệu của 1 cột theo dạng chuỗi',
    18:	'Lấy dữ liệu của 1 cột về một mảng',
    19:	'Lấy dữ liệu của 1 cột về một mảng',
    20:	'Lấy dữ liệu từ dòng số 4 đến dòng 9',
    21:	'Đọc dữ liệu từ dòng 4 đến dòng 9',
    22:	'Lấy thông tin tại dòng có chỉ số là 2',
    23:	'Lấy thông tin từ dòng 4 đến dòng 10 của một số cột',
    24:	'Lấy thông tin dòng 2 đến dòng 9, từ cột 4 đến cột 7',
    25:	'Lấy dữ liệu tại chỉ số (index) là 2',
    26:	'Lấy dữ liệu từ dòng đầu tiên đến dòng 9 dùng iloc',
    27:	'Lấy dữ liệu từ dòng đầu tiên đến dòng 9 gồm các cột 4 đến cột 7 dùng iloc ',
    28:	'Sắp xếp dữ liệu theo 1 cột tăng dần',
    29:	'Sắp xếp dữ liệu theo nhiều tiêu chí',
    30:	'Lọc dữ liệu theo 1 điều kiện',
    31:	'Lọc dữ liệu theo nhiều điều kiện',
    32:	'Lọc giá trị và gán điều kiện dùng loc ',
    33:	'Viết hàm trả về giá trị có nhiều điều kiện và áp dụng hàm gán trị trả về cho 1 cột ',
    34:	'Ánh xạ giá trị tới 1 cột',
    35:	'Lấy những dòng dữ liệu bằng 1 điều kiện nào đó',
    36:	'Hiển thị các bản ghi có cột kiểu số hơn 25',
    37:	'Sinh viên tự nghĩ ra các câu hỏi đọc dữ liệu theo các điều kiện và thực hiện lại các câu hòi đó. Yêu cầu sinh viên ghi lại và lệnh thực hiện các câu hòi đó.',
    38:	'Thực hiện 1 ví dụ để lấy giá trị của một cột trả về dưới dạng numpy array trong thư viện pandas python.',
    39:	'Sử dụng thư viện random để sinh ngẫu nhiên một list năm sinh và thêm vào DataFrame',
    40:	'Thêm 1 cột vào file dữ liệu',
    41:	'Thêm 1 cột vào dữ liệu theo tiêu chí nếu điều kiện thoả thì giá trị mặc định là True, ngược lại là False.',
    42:	'Tạo 1 cột mới có giá trị rỗng',
    43:	'Thêm 1 bản ghi trong DataFrame',
    44:	'Sửa giá trị của cột',
    45:	'Xóa cột trong DataFrame',
    46:	'Xóa bản ghi theo chỉ số',
    47:	'Sử dụng hàm describe() để thống kê dữ liệu',
    48:	'Xem thống kê trên từng cột',
    49:	'Vẽ đồ thị xem phân bổ giá trị của 1 trường trong dataframe',
    50:	'Tạo mới dataframe từ các python list',
    51:	'Sắp xếp dataframe',
    52:	'Nối 2 dataframe',
    53:	'Xáo trộn các bản ghi trong dataframe',
    54:	'Lưu dataframe về file csv',
    55:	'Tối ưu bộ nhớ khi dùng pandas',
    56:	'Tạo 1 file chương trình hiện các menu gồm các mục trên và mục cuối là thoát. Người dùng chọn chức năng nào trong menu thì chương trình sẽ thực hiện chức năng tương ứng',
    'Others': 'Kết thúc chương trình'
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


_currentDir = os.getcwd()

while (True):
    print('\n\n')
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input('Nhập tùy chọn: '))
    except:
        print('Nhập sai định dạng. Vui lòng nhập lại !')
        continue
    
    # 1. Nạp dữ liệu từ file. Hiển thị toàn bộ dữ liệu của DataFrame
    if userChoice == 1:
        _currentDir = os.getcwd()
        file = _currentDir + '/data/dulieuxettuyendaihoc.csv'
        df = pd.read_csv(file)
        print(df)
    
    # 2. Nạp dữ liệu từ file. Hiển thị toàn bộ dữ liệu của DataFrame
    elif userChoice == 2:
        file = _currentDir + '/data/dulieuxettuyendaihoc.csv'
        df = pd.read_csv(file)
        print(df)
    
    # 3. Nạp dữ liệu từ file. Hiển thị 5 dòng dữ liệu đầu tiên của DataFrame
    elif userChoice == 3:
        file = _currentDir + '/data/dulieuxettuyendaihoc.csv'
        df = pd.read_csv(file).head(5)
        print(df)
    
    # 4. Nạp dữ liệu từ file. Hiển thị 5 dòng dữ liệu cuối cùng của DataFrame
    elif userChoice == 4:
        file = _currentDir + '/data/dulieuxettuyendaihoc.csv'
        df = pd.read_csv(file).tail(5)
        print(df)
    
    # 5. Chuyển kiểu dữ liệu cho 1 cột nào đó
    elif userChoice == 5:
        # Sử dụng thư viện random để sinh ngẫu nhiên một list mã tỉnh và thêm vào DataFrame
        # Tạo 1 cột mới có tên là MATINH dùng để lưu trữ giá trị của mã tỉnh trong cả nước
        maTinh = [random.randint(1, 64) for x in range(len(df))]
        df['MATINH'] = maTinh
        # Kiểu dữ liệu ban đầu của cột MATINH sau khi tạo là int64
        # Chuyển đổi kiểu dữ liệu của cột MATINH
        # Chuyển từ int64 sang int32
        df['MATINH'] = df['MATINH'].astype('int32')
        # Kiểm tra kiểu dữ liệu của cột MATINH sau khi đổi kiểu dữ liệu
        print(df.info())
    
    # 6. Xem chiều dài của DataFrame
    elif userChoice == 6:
        print('Len:', len(df))
    
    # 7. Xem thông tin DataFrame
    elif userChoice == 7:
        print('Info: ', df.info())
    
    # 8. Xem kích thước của DataFrame
    elif userChoice == 8:
        print('Shape: ', df.shape)
    
    # 9. Hiển thị dữ liệu của cột thứ 3
    elif userChoice == 9:
        print(df[['T3']])
    
    # 10. Hiển thị dữ liệu của cột 1,2,3,5,6
    elif userChoice == 10:
        print(df[['T1', 'T2', 'T3', 'T5', 'T6']])
    
    # 11. Hiển thị 5 dòng dữ liệu đầu tiên gồm các cột 1,2,3,5,6 
    elif userChoice == 11:
        print(df[['T1', 'T2', 'T3', 'T5', 'T6']].head(5))
    
    # 12. Hiển thị 5 dòng dữ liệu đầu tiên theo chỉ số
    elif userChoice == 12:
        print(df[0:5])
    
    # 13. Hiển thị 5 dòng dữ liệu đầu tiên theo chỉ số gồm các cột 1,2,3,5,6 
    elif userChoice == 13:
        print(df[['T1', 'T2', 'T3', 'T5', 'T6']][:5])
    
    # 14. Loại bỏ các dòng trùng nhau
    elif userChoice == 14:
        df.drop_duplicates(inplace=True)
        print(df)
    
    # 15. Loại bỏ các dòng trống có dữ liệu của 1 cột là trống
    elif userChoice == 15:
        print(df["DT"].isna().sum())
    
    # 16. Loại bỏ các dòng của 1 cột có giá trị là không biết (“unknown”) 
    elif userChoice == 16:
        df["DT"].fillna('Unknown', inplace=True)
        print(df["DT"].isna().sum())
    
    # 17. Lấy dữ liệu của 1 cột theo dạng chuỗi
    elif userChoice == 17:
        print(df["MSSV"])
    
    # 18. Lấy dữ liệu của 1 cột về một mảng
    elif userChoice == 18:
        print(df[["MSSV"]].values)
    
    # 19. Lấy dữ liệu của 1 cột về một mảng
    elif userChoice == 19:
        print(df[["MSSV"]].values)
    
    # 20. Lấy dữ liệu từ dòng số 4 đến dòng 9
    elif userChoice == 20:
        print(df[4:10])
    
    # 21. Đọc dữ liệu từ dòng 4 đến dòng 9
    elif userChoice == 21:
        print(df.loc[4:10])
        print(df.iloc[4:10])
    
    # 22. Lấy thông tin tại dòng có chỉ số là 2
    elif userChoice == 22:
        print(df.loc[2])
    
    # 23. Lấy thông tin từ dòng 4 đến dòng 10 của một số cột
    elif userChoice == 23:
        print(df.loc[4:10, ['KT', 'NGAYTHI']])
    
    # 24. Lấy thông tin dòng 2 đến dòng 9, từ cột 4 đến cột 7
    elif userChoice == 24:
        print(df.iloc[2:9, 4:7])
    
    # 25. Lấy dữ liệu tại chỉ số (index) là 2
    elif userChoice == 25:
        print(df.iloc[2])
    
    # 26. Lấy dữ liệu từ dòng đầu tiên đến dòng 9 dùng iloc
    elif userChoice == 26:
        print(df.iloc[:10])
    
    # 27. Lấy dữ liệu từ dòng đầu tiên đến dòng 9 gồm các cột 4 đến cột 7 dùng iloc 
    elif userChoice == 27:
        print(df.iloc[2:9, 4:7])
    
    # 28. Sắp xếp dữ liệu theo 1 cột tăng dần
    elif userChoice == 28:
        print(df.sort_values(by='MSSV', ascending=True))
    
    # 29. Sắp xếp dữ liệu theo nhiều tiêu chí
    elif userChoice == 29:
        print(df.sort_values(by=['NGONNGU', 'TOANLOGICPHANTICH'], ascending=[True, False]))
    
    # 30. Lọc dữ liệu theo 1 điều kiện
    elif userChoice == 30:
        print(df[df['NGONNGU']>5])
        print(df.loc[df['NGONNGU']>5])
    
    # 31. Lọc dữ liệu theo nhiều điều kiện
    elif userChoice == 31:
        print(df[(df['NGONNGU']>5) & (df['TOANLOGICPHANTICH']<4)])
    
    # 32. Lọc giá trị và gán điều kiện dùng loc 
    elif userChoice == 32:
        # Thêm cột TBTOAN
        df['TBTOAN'] = (df['T5']+df['T6'])/2
        # Tạo biến XEPLOAI để đánh giá học lực của học sinh
            # Gán nhãn XEPLOAI là EXCELLENT cho các giá trị >= 9.0 của cột TBTOAN
            # Gán nhãn XEPLOAI là GOOD cho các giá trị < 9 và >= 7 của cột TBTOAN
            # Gán nhãn XEPLOAI là FAIR cho các giá trị < 7 và >= 5 của cột TBTOAN
            # Gán nhãn XEPLOAI là FAIL cho các giá trị < 5 của cột TBTOAN
        df.loc[df['TBTOAN']>=9.0, 'XEPLOAI'] = 'EXCELLENT'
        df.loc[(df['TBTOAN']>=7.0) & (df['TBTOAN']<9.0), 'XEPLOAI'] = 'GOOD'
        df.loc[(df['TBTOAN']>=5.0) & (df['TBTOAN']<7), 'XEPLOAI'] = 'FAIR'
        df.loc[df['TBTOAN']<5.0, 'XEPLOAI'] = 'FAIL'

        print(df[['TBTOAN', 'XEPLOAI']])
    
    # 33. Viết hàm trả về giá trị có nhiều điều kiện và áp dụng hàm gán trị trả về cho 1 cột
    elif userChoice == 33:
        def foo(x):
            if x < 5.0:
                return 'FAIL'
            elif x >= 5 and x < 7.0:
                return 'FAIR'
            elif x >= 7.0 and x < 9.0:
                return 'GOOD'
            else:
                return 'EXCELLENT'
        df['HOCLUC'] = df[['NGONNGU']].applymap(foo)
        print(df)
    
    # 34. Ánh xạ giá trị tới 1 cột
    elif userChoice == 34:
        dict_map1 = {'M': 'Nam', 'F': 'Nữ'}
        df['GT'] = df['GT'].map(dict_map1)
        print(df[['GT']])
    
    # 35. Lấy những dòng dữ liệu bằng 1 điều kiện nào đó
    elif userChoice == 35:
        print(df[['MSSV', 'KV']].loc[df['KT']=='D1'])
    
    # 36. Hiển thị các bản ghi có cột kiểu số hơn 25
    elif userChoice == 36:
        df['DIEMTHITOAN'] = df['T1'] + df['T2'] + df['T3'] + df['T4'] + df['T5'] + df['T6']
        df[df['DIEMTHITOAN']>25]
        print("Hiển thị 5 dòng đầu tiên")
        DiemThiToan = df[df['DIEMTHITOAN']>25]
        print(DiemThiToan[:5])
    
    # 37.	Sinh viên tự nghĩ ra các câu hỏi đọc dữ liệu theo các điều kiện và thực hiện lại các câu hòi đó. 
    # Yêu cầu sinh viên ghi lại và lệnh thực hiện các câu hòi đó.
    elif userChoice == 37:
        """
            Tạo biến nhóm khối thi: NHÓM KT THÕA MÃN
            A1: G1
            C : G3
            D1 : G3
            A : G1
            B: G2
        """
        dict_map = {
            'A1': 'G1',
            'C' : 'G3',
            'D1' : 'G3',
            'A' : 'G1',
            'B': 'G2'
        }
        df['NHOM_KT'] = df['KT'].map(dict_map)
    
        """
            Tạo biến điểm cộng: 
            Nếu khối thi thuộc nhóm G1, G2 và TBTOAN >=0.5 thì là 1.0
            Ngược lại thì là 6.0
        """

        def fplus(x,y):
            if (x == 'G1' or x =='G2') and (y >= 5.0):
                return 1.0
            else:
                return 0.0
        df['DIEMCONG'] = list(map(fplus,df['NHOM_KT'],df['TBTOAN']))
        
        print(df[['NHOM_KT']])
        print(df[['DIEMCONG']])
    
    # 38. Thực hiện 1 ví dụ để lấy giá trị của một cột trả về dưới dạng numpy array trong thư viện pandas python.
    elif userChoice == 38:
        print(df['MSSV'].values)
    
    # 39. Sử dụng thư viện random để sinh ngẫu nhiên một list năm sinh và thêm vào dataframe.
    elif userChoice == 39:
        namSinh = [random.randint(1985, 2005) for x in range(len(df))]
        df['NAMSINH'] = namSinh
        print(df['NAMSINH'])
    
    # 40. Thêm 1 cột vào file dữ liệu
    elif userChoice == 40:
        df['TONGDIEMTHI'] = df['DIEMTHITOAN'] + df['NGONNGU'] + df['TOANLOGICPHANTICH'] + df['GIAIQUYETVANDE']
        print(df[['TONGDIEMTHI']])
    
    # 41. Thêm 1 cột vào dữ liệu theo tiêu chí nếu điều kiện thoả thì giá trị mặc định là True, ngược lại là False.
    elif userChoice == 41:
        # Tạo 1 cột mới có tên là DiemUuTienTheoKV
        # Nếu giá trị trong cột KV là 2NT thì trả về True
        # Ngược lại trả về False
        df['DiemUuTienTheoKV'] = df['KV'] == '2NT'
    
    # 42. Tạo 1 cột mới có giá trị rỗng
    elif userChoice == 42:
        df['NGUYENVONG'] = None
        print(df['NGUYENVONG'])
    
    # 43. Thêm 1 bản ghi trong dataframe
    elif userChoice == 43:
        newRecord = {
            'MSSV': 'SV00101',
            'T1': 6.0,
            'T2': 7.0,
            'T3': 7.0,
            'T4': 8.0,
            'T5': 8.0,
            'T6': 9.0,
            'GT': 'Nữ',
            'DT': 'Unknown',
            'KV': '1',
            'NGONNGU': 9.0,
            'TOANLOGICPHANTICH': 7.0,
            'GIAIQUYETVANDE': 8.0,
            'KT': 'D',
            'NGAYTHI': '10/7/2021',
            'DINHHUONGNGHENGHIEP': 'Yes',
            'TBTOAN': 7.5,
            'XEPLOAI': 'EXCELLENT',
            'HOCLUC': 'EXCELLENT',
            'DIEMTHITOAN': 45,
            'NHOM_KT': 'G3',
            'DIEMCONG': 1.0,
            'NAMSINH': 2003,
            'TONGDIEMTHI': 69,
            'DiemUuTienTheoKV': 'False',
            'NGUYENVONG': 'None'
        }
        df.loc[len(df)] = newRecord
        print(df.tail(5))
    
    # 44. Sửa giá trị của cột
    elif userChoice == 44:
        # Sửa giá trị của cột NGUYENVONG
        df['NGUYENVONG'] = None
        df['NGUYENVONG'] = 'Đậu TN THPT và đậu ĐH'
        print(df)
    
    # 45. Xóa cột trong dataframe
    elif userChoice == 45:
        df = df.drop('NGUYENVONG', axis=1)
        print(df)
    
    # 46. Xóa bản ghi theo chỉ số
    elif userChoice == 46:
        df.drop([0,1])
        print(df)
    
    # 47. Sử dụng hàm describe() để thống kê dữ liệu
    elif userChoice == 47:
        df.describe()
        print(df)
    
    # 48. Xem thống kê trên từng cột
    elif userChoice == 48:
        df['NAMSINH'].value_counts()
        print(df)
    
    # 49. Vẽ đồ thị xem phân bổ giá trị của 1 trường trong dataframe
    elif userChoice == 49:
        df['NAMSINH'].value_counts().plot(kind='bar')
    
    # 50. Tạo mới dataframe từ các python list
    elif userChoice == 50:
        import pandas as pd
        students = {
            'maSV': [21087481, 21107481],
            'hoTen': ['Dương Hoàng Lan Anh', 'Dương Hoàng Phương Anh'],
            'namSinh': [2003, 2007],
            'truong': ['Đại học Công nghiệp TPHCM', 'Đại học Công nghệ Thông tin'],
            'khoa': ['Khoa Công nghệ Thông tin', 'Khoa Công nghệ Thông tin'],
            'nganh': ['Ngành Kỹ thuật phần mềm', 'Ngành Khoa học dữ liệu']
        }
        df1 = pd.DataFrame(students)
        print(df1)
    
    # 51. Sắp xếp DataFrame
    elif userChoice == 51:
        # Sắp xếp DataFrame df tăng dần theo cột TONGDIEMTHI
        print('Before sort: \n', df)
        df_sorted = df.sort_values('TONGDIEMTHI', ascending=True)
        print('After sort: \n', df_sorted)
    
    # 52. Nối 2 dataframe
    elif userChoice == 52:
        # Gộp 2 DataFrame
        import pandas as pd
        df_1 = pd.DataFrame({'name': ['Hiếu'], 'age': [18], 'gender': ['male']})
        df_2 = pd.DataFrame({'name': ['Nam', 'Mai', 'Hoa'], 'age': [15, 17, 19]})
        df_3 = pd.concat([df_1, df_2], ignore_index=True)
        print(df_3)
    
    # 53. Xáo trộn các bản ghi trong dataframe
    elif userChoice == 53:
        df_4 = pd.DataFrame({'name': ['Hiếu', 'Nam', 'Mai', 'Hoa'], 'age': [18, 15, 17, 19]})
        print('\nBefore shuffle\n', df)
        df_5 = df.sample(frac=1).reset_index(drop=True)
        print('\nAfter shuffle\n', df1)
    
    # 54. Lưu dataframe về file csv
    elif userChoice == 54:
        df.to_csv('../data/dulieuxettuyendaihoc_clean.csv')
    
    # 55. Tối ưu bộ nhớ khi dùng pandas
    elif userChoice == 55:
        import numpy as np # linear algebra
        import pandas as pd # data processing, csv file I/O (e.g. pd.read_csv)

        def reduce_mem_usage(df):
            """iterate through all the columns of a dataframe and modify the data type
                to reduce memory usage
            """

            start_mem = df.memory_usage().sum()/1024**2
            print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))
            for col in df.columns:
                col_type = df[col].dtype

                if col_type != object and col_type.name != 'category' and 'datetime' not in col_type.name:
                    c_min = df[col].min()
                    c_max = df[col].max()
                    if str(col_type)[:3] == 'int':
                        if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                            df[col] = df[col].asptype(np.int8)
                        elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                            df[col] = df[col].asptype(np.int16)
                        elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                            df[col] = df[col].asptype(np.int32)
                        elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                            df[col] = df[col].asptype(np.int64)
                    else:
                        if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                            df[col] = df[col].astype(np.float16)
                        elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                            df[col] = df[col].astype(np.float32)
                        else:
                            df[col] = df[col].astype(np.float64)
                elif 'datetime' not in col_type.name:
                    df[col] = df[col].astype('category')
                
                end_mem = df.memory_usage().sum() / 1024**2
                print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
                print('Decreased bt {:.1f}'.format(100 * (start_mem - end_mem)/ start_mem))

                return df

        print(reduce_mem_usage(df))
    
    else:
        print('Kết thúc chương trình. BYE !')
        break