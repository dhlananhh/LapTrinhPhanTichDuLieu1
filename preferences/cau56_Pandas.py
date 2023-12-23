import pandas as pd
import matplotlib.pyplot as plt
import random
menu_options = {
    1:'Đọc File với các file trong thư mục dữ liệu. Ứng với mỗi file sinh viên thực hiện các câu sau. Hiển thị toàn bộ dữ liệu của file dữ liệu đã đọc',
    2:'Đọc file với chỉ định không có header, dòng header của chúng ta đã biến thành 1 bản ghi dữ liệu. Hiển thị toàn bộ dữ liệu của file dữ liệu đã đọc',
    3:'Đọc File với các tuỳ chọn mặc định. Hiển thị 5 dòng dữ liệu đầu tiên',
    4:'Đọc File với các tuỳ chọn mặc định. Hiển thị 5 dòng dữ liệu cuối cùng',
    5:'Chuyển kiểu dữ liệu cho 1 cột nào đó',
    6:'Xem chiều dài của df, tương đương shape[0]',
    7:'Xem thông tin dataframe vừa đọc được',
    8:'Xem kích thước của dataframe',
    9:'Hiển thị dữ liệu của cột thứ 3',
    10:'Hiển thị dữ liệu của cột 1,2,3,5,6 ',
    11:'Hiển thị 5 dòng dữ liệu đầu tiên gồm các cột 1,2,3,5,6 ',
    12:'Hiển thị 5 dòng dữ liệu đầu tiên theo chỉ số',
    13:'Hiển thị 5 dòng dữ liệu đầu tiên theo chỉ số gồm các cột 1,2,3,5,6 ',
    14:'Loại bỏ các dòng trùng nhau',
    15:'Loại bỏ các dòng trống có dữ liệu của 1 cột là trống',
    16:'Loại bỏ các dòng của 1 cột có giá trị là không biết (“unknown”)',
    17:'Lấy dữ liệu của 1 cột theo dạng chuỗi',
    18:'Lấy dữ liệu của 1 cột về một mảng',
    19:'Lấy dữ liệu của 1 cột về một mảng',
    20:'Lấy dữ liệu từ dòng số 4 đến dòng 9',
    21:'Đọc dữ liệu từ dòng 4 đến dòng 9',
    22:'Lấy thông tin tại dòng có chỉ số là 2',
    23:'Lấy thông tin từ dòng 4 đến dòng 10 của một số cột',
    24:'Lấy thông tin dòng 2 đến dòng 9, từ cột 4 đến cột 7',
    25:'Lấy dữ liệu tại chỉ số (index) là 2',
    26:'Lấy dữ liệu từ dòng đầu tiên đến dòng 9 dùng iloc',
    27:'Lấy dữ liệu từ dòng đầu tiên đến dòng 9 gồm các cột 4 đến cột 7 dùng iloc ',
    28:'Sắp xếp dữ liệu theo 1 cột tăng dần',
    29:'Sắp xếp dữ liệu theo nhiều tiêu chí',
    30:'Lọc dữ liệu theo 1 điều kiện',
    31:'Lọc dữ liệu theo nhiều điều kiện',
    32:'Lọc giá trị và gán điều kiện dùng loc ',
    33:'Viết hàm trả về giá trị có nhiều điều kiện và áp dụng hàm gán trị trả về cho 1 cột ',
    34:'Ánh xạ giá trị tới 1 cột',
    35:'Lấy những dòng dữ liệu bằng 1 điều kiện nào đó',
    36:'Hiển thị các bản ghi có cột kiểu số hơn 25',
    37:'Sinh viên tự nghĩ ra các câu hỏi đọc dữ liệu theo các điều kiện và thực hiện lại các câu hòi đó. Yêu cầu sinh viên ghi lại và lệnh thực hiện các câu hòi đó.',
    38:'Thực hiện 1 ví dụ để lấy giá trị của một cột trả về dưới dạng numpy array trong thư viện pandas python.',
    39:'Sử dụng thư viện random để sinh ngẫu nhiên một list năm sinh và thêm vào dataframe.',
    40:'Thêm 1 cột vào file dữ liệu',
    41:'Thêm 1 cột vào dữ liệu theo tiêu chí nếu điều kiện thoả thì giá trị mặc định là True, ngược lại là False',
    42:'Tạo 1 cột mới có giá trị rỗng',
    43:'Thêm 1 bản ghi trong dataframe',
    44:'Sửa giá trị của cột',
    45:'Xóa cột trong dataframe',
    46:'Xóa bản ghi theo chỉ số',
    47:'Sử dụng hàm describe() để thống kê dữ liệu',
    48:'Xem thống kê trên từng cột',
    49:'Vẽ đồ thị xem phân bổ giá trị của 1 trường trong dataframe',
    50:'Tạo mới dataframe từ các python list',
    51:'Sắp xếp dataframe',
    52:'Nối 2 dataframe ',
    53:'Xáo trộn các bản ghi trong dataframe',
    54:'Lưu dataframe về file csv',
    55:'Tối ưu bộ nhớ khi dùng pandas'
}
def print_menu():
    for key in menu_options.keys():
        print(key,'--',menu_options[key])

while(True):
    print_menu()
    try:
        usechoice = int(input('input choice:'))
    except:
        print('Invalid input, try again')
        continue
    if(usechoice == 2):
        df = pd.read_csv('BT_Tuan3\BH.csv')
        print(df)
    elif(usechoice == 3):
        df = pd.read_csv('BT_Tuan3\BH.csv').head(5)
        print(df)
    elif(usechoice == 4):
        df = pd.read_csv('BT_Tuan3\BH.csv').tail(5)
        print(df)
    elif(usechoice == 5):
        df['Purchase'] = df['Purchase'].astype('int32')
        print(df.info())
    elif(usechoice == 6):
        print('Len:', len(df))
    elif(usechoice == 7):
        print(df.info())
    elif(usechoice == 8):
        print('Shape:',df.shape)
    elif(usechoice == 9):
        print(df['Purchase'])
    elif(usechoice == 10):
        print(df[['User_ID','Purchase','Product_ID']])
    elif(usechoice == 11):
        print(df[['User_ID','Purchase','Product_ID']].head(5))
    elif(usechoice == 12):
        print(df[0:5])
    elif(usechoice == 13):
        print(df[['User_ID','Purchase','Product_ID']][:5])
    elif(usechoice == 14):
        df.drop_duplicates(inplace=True)
        print(df)
    elif(usechoice == 15):
        print(df['User_ID'].isna().sum())
    elif(usechoice == 16):
        df["Purchase"].fillna('Unknown',inplace=True)
        print(df['Purchase'].isna().sum())
    elif(usechoice == 17):
        print(df["Purchase"])
    elif(usechoice == 18):
        print(df["Purchase"].values)
    elif(usechoice == 19):
        print(df["Purchase"].values)
    elif(usechoice == 20):
        print(df[4:10])
    elif(usechoice == 21):
        print(df.loc[4:9])
        print(df.iloc[4:10])
    elif(usechoice == 22):
        print(df.loc[2])
    elif(usechoice == 23):
        print(df.loc[4:10,['User_ID','Product_ID']])
    elif(usechoice == 24):
        print(df.iloc[2:9,1:3])
    elif(usechoice == 25):
        print(df.iloc[2])
    elif(usechoice == 26):
        print(df.iloc[:10])
    elif(usechoice == 27):
        print(df.iloc[:10,1:3])
    elif(usechoice == 28):
        print(df.sort_values(by='Purchase', ascending=True))
    elif(usechoice == 29):
        print(df.sort_values(by=['Purchase','Product_ID'], ascending=[True,False]))
    elif(usechoice == 30):
        print(df[df['Purchase']>300])
        print(df.loc[df['Purchase']>300])
    elif(usechoice == 31):
        print(df[(df['Purchase']>300) & (df['User_ID']>1000)])
    elif(usechoice == 32):
        print( df.loc[df['Purchase']>100,'User_ID']>1000)
        print(df[['Purchase','User_ID']][:5])
    elif(usechoice == 33):
        def foo(x):
            if x<200:
                return 'BAD'
            elif x>=200 and x<500:
                return 'GOOD'
            else:
                return 'EXCELLENT'
        df['Worth'] = df[['Purchase']].applymap(foo)
        print(df)
    elif(usechoice == 34):
        dict_map ={100:'Qui_1',200:'Qui_2',300:'Qui_3',400:'Qui_4'}
        df['QTR_ID']=df['Purchase'].map(dict_map)
        print(df['QTR_ID'])
    elif(usechoice == 35):
        print(df[['User_ID','Worth']].loc[df['Purchase'] > 100])
    elif(usechoice == 36):
        df[df['Purchase']<250]
        a =df[df['Purchase']<250]
        print(a[:5])
    elif(usechoice == 37):
        dg = df[df['Worth'] == 'GOOD']
        print(dg)
    elif(usechoice == 38):
        print(df['Worth'].values)
    elif(usechoice == 39):
        df_len = len(df)
        namsx = [random.randrange(2020,2023,1) for i in range(df_len)]
        df['namsx'] = namsx
        print(df.tail(5))
    elif(usechoice == 40):
        df['Evaluate'] = df['Worth']
        print(df.head(5))
    elif(usechoice == 41):
        df['ToT'] = df['Worth'] == 'GOOD'
        print(df.head(5))
    elif(usechoice == 42):
        df['TONGTIEN'] = None
        print(df)
    elif(usechoice == 43):
        df.loc[15] = {'User_ID':'1003','Product_ID':'P5','Purchase':400,
              'Worth':'GOOD','QTR_ID':'Qui_4','namsx':2020,'Evaluate':'GOOD','ToT':True,'TONGTIEN':None}
        print(df)
    elif(usechoice == 44):
        df['QTR_ID'] = None
        print(df)
    elif(usechoice == 45):
        df = df.drop(['namsx'],axis=1)
        print(df)
    elif(usechoice == 46):
        df = df.drop([0,1])
        print(df)
    elif(usechoice == 47):
        print(df.describe())
    elif(usechoice == 48):
        print(df['Purchase'].value_counts())
    elif(usechoice == 49):
        a = df['Purchase'].value_counts().plot(kind='bar')
        print(a)
    elif(usechoice == 50):
        txts = ['chỗ này ăn cũng khá ngon','ngon, nhất định sẽ quay lại','thái độ phục vụ quá tệ']
        labels = [1,1,0]
        df1 = pd.DataFrame()
        df1['txt'] = txts
        df1['label'] = labels
        print(df1)
    elif(usechoice == 51):
        print('Trước khi sắp xếp')
        print(df)
        df = df.sort_values('Purchase', ascending=True)
        print('Sau khi sắp xếp')
        print(df)
    elif(usechoice == 52):
        df_1 = pd.DataFrame({'name':['Hiếu'], 'age':[18], 'gender':['male']})
        df_2 = pd.DataFrame({'name': ['Nam','Mai','Hoa'], 'age':[15,17,19]})
        df_1 = pd.concat([df_1,df_2], ignore_index=True)
        df_3 = df_1
        print(df_3)
    elif(usechoice == 53):
        df1 = pd.DataFrame({'name':['Hiếu','Nam','Mai','Hoa'], 'age':[18,15,17,19]})
        print('Before shuffle\n', df1)
        df1 = df1.sample(frac=1).reset_index(drop=True)
        print('After shuffle\n', df1)
    elif(usechoice == 54):
        df1.to_csv('KHACHHANG.csv')
    elif(usechoice == 55):
        import numpy as np
        def reduce_mem_usage(df):
            start_mem = df.memory_usage().sum() / 1024**2
            print('Memory usage og dataframe is {:.2f} MB'.format(start_mem))

            for col in df.columns:
                col_type = df[col].dtype

                if col_type != object and col_type.name != 'category' and 'datetime' not in col_type.name:
                    c_min = df[col].min()
                    c_max = df[col].max()
                    if str(col_type)[:3] == 'int':
                        if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                            df[col] = df[col].astype(np.int8)
                        elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                            df[col] = df[col].astype(np.int16)
                        elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                            df[col] = df[col].astype(np.int32)
                        elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                            df[col] = df[col].astype(np.int64)
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
            print('Decreased bt {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

            return df
        print(reduce_mem_usage(df))
    else:
        print('Bye Bye')
        break