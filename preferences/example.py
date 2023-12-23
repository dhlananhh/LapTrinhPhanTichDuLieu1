import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "../data/dulieuxettuyendaihoc.csv"

# Đọc dữ liệu từ file CSV và tạo DataFrame
df = pd.read_csv(file_path,header=0, delimiter=",",encoding='utf-8')

# In ra một số dòng đầu của DataFrame
# print(df.head(10))

# 10 dòng cuối
# print(df.tail(10))

# Đổi tên cột 
# df.rename(columns={
#     "TOANLOGICPHANTICH": "TOAN",
#     "GIAIQUYETVANDE": "KYNANG",
#     "DINHHUONGNGHENGHIEP": "HUONGNGHIEP"
# }, inplace=True)
# print(df.head(10))
# inplace=True, thay vì tạo ra một bản sao của dữ liệu đã thay đổi, pandas sẽ thay đổi dữ liệu trực tiếp trên đối tượng ban đầu. Điều này có nghĩa là DataFrame (hoặc Series) ban đầu sẽ bị thay đổi, và không cần phải gán kết quả trở lại một biến mới.

# Kiểu dl của từng cột được lưu trữ trong df
# print(df.dtypes)

# Cho biết kích cỡ df
# print(df.shape)

# cho biết cách đánh chỉ mục Index 
# print(df.index) 

# truy cập và làm việc với một cột cụ thể trong DataFrame
# print(df['T1']) 
# 0     7.2
# 1     5.4
# 2     5.6
# 3     6.6
# 4     6.0
#      ...
# 95    8.6
# 96    3.7
# 97    8.8
# 98    2.7
# 99    4.1
# Name: T1, Length: 100, dtype: float64

# phân biệt khác nhau giữa df['T1'] và df[['T1']]
    # khi bạn sử dụng df[['T1']], bạn nhận được một DataFrame có một cột 
    # df['T1'] sẽ trả về một Series(là một mảng một chiều của dữ liệu, không bao gồm tên cột và chỉ bao gồm dữ liệu của cột đó.)
# print(df[['T1']]) 
#      T1
# 0   7.2
# 1   5.4
# 2   5.6
# 3   6.6
# 4   6.0
# ..  ...
# 95  8.6
# 96  3.7
# 97  8.8
# 98  2.7
# 99  4.1
# [100 rows x 1 columns]

# Lấy dữ liệu theo cột 
newdf = df[['T5','T6','KV','KT']]
# print(newdf)

# Lấy tất cả các dòng dl có index từ 2 - 97
# Slicing
# newdf = df[['T5','T6','KV','KT']]
# subset= newdf[2:97]
# print(subset)

# lấy dòng dữ liệu có index92 
# lấy theo index là chuỗi 
# newdf = df[['T5','T6','KV','KT']]
# row_92 = newdf.loc[92]  
# print(row_92)
# T5    8.0
# T6    7.5
# KV      1
# KT      A
# Name: 92, dtype: object

# Phân biệt slicing và loc 
# slicing dựa trên chỉ mục số, còn loc dựa trên nhãn.

# Lấy các dòng index=5 đến 9 và cụ thể trên các cột T6 KT
# newdf = df[['T5','T6','KV','KT']]
# subset = newdf.loc[5:9, ['T6', 'KT']]
# print(subset)
#     T6  KT
# 5  7.8  D1
# 6  5.3   C
# 7  8.3  D1
# 8  7.7  D1
# 9  6.9  D1

# Lấy dữ liệu tại index = 5 , ...
# iloc : lấy theo index là số
# newdf = df[['T5','T6','KV','KT']]
# subset = newdf.iloc[5]
# lấy các dòng index từ 6 đến 8 
# subset = newdf.iloc[6:9] 
# lấy các dòng index từ 0 đến 4 
# subset = newdf.iloc[:5] 
# print(subset)
# T5    8.5
# T6    7.8
# KV      1
# KT     D1
# Name: 5, dtype: object
# loc sử dụng nhãn (tên) của dòng và cột.
# iloc sử dụng chỉ mục số của dòng và cột (chỉ mục bắt đầu từ 0).

# Sắp xếp dữ liệu
# newdf = df[['T5','T6','KV','KT']]
# subset = newdf.sort_values(by='T5',ascending=True)
# subset = newdf.sort_values(by=['T5','T6'],ascending=[True,False])
# print(subset)
# ascending=True, dữ liệu sẽ được sắp xếp theo thứ tự tăng dần, từ nhỏ đến lớn. Điều này có nghĩa rằng giá trị nhỏ nhất của cột 'T5' sẽ xuất hiện ở đầu danh sách,

# Lấy dữ liệu theo điều kiện 
# newdf = df[['T5','T6','KV','KT']]
# subset = newdf[newdf['T6']>=8]
# subset = newdf[(newdf['T5']>7)&(newdf['T6']>=8)]
# print(subset)

# Cột KT là C
# newdf = df[['T5','T6','KV','KT']]
# subset = newdf.loc[newdf['KT']=='C']
# print(subset)

# Nguyên lí ứng dụng các hàm tổng hợp trên các loại biến định tính và định lượng
# newdf = df[['T5','T6','KV','KT']]
# subset = newdf.aggregate({'T5':['min','max'],'T6':['mean','sum']})
# mean là giá trị trung bình 
# print(subset)
#        T5       T6
# min   3.0      NaN
# max   9.5      NaN
# mean  NaN    6.937
# sum   NaN  693.700

# Nguyên tắc gom nhóm
# newdf = df[['T5','T6','KV','KT']]
# subset = newdf.groupby(['KV'])['KV'].agg(['count'])
# subset = newdf.groupby(['KV'])['T5'].agg(['count','min','std','max','sum'])
# print(subset)
#      count
# KV
# 1       60
# 2       19
# 2NT     21
#      count  min       std  max    sum
# KV
# 1       60  3.0  1.501053  9.3  390.9
# 2       19  3.2  1.574189  8.9  128.9
# 2NT     21  5.3  1.237066  9.5  151.9
# std: Độ lệch chuẩn trong mỗi nhóm.

# newdf = df[['T5','T6','KV','KT']]
# subset = newdf.groupby(['KV','KT'])[['T5','T6']].agg(['min','max'])
# print(subset)
#          T5        T6     
#         min  max  min  max
# KV  KT
# 1   A   4.7  9.3  4.0  8.9
#     A1  7.4  7.8  6.4  7.1
#     B   3.5  8.4  5.2  9.0
#     C   3.0  7.9  3.7  6.8
#     D1  3.4  9.3  4.9  8.3
# 2   A   3.2  8.9  3.7  8.9
#     C   3.4  5.4  4.1  5.3
#     D1  5.8  8.5  6.0  8.3
# 2NT A   5.8  8.7  5.7  9.4
#     A1  6.7  9.5  6.6  9.5
#     B   7.8  7.8  6.9  6.9
#     C   5.3  9.0  5.1  8.5
#     D1  7.4  7.4  5.9  5.9

# Tạo một bảng tổng hợp (pivot table) từ DataFrame 
# newdf = df[['T5','T6','KV','KT']]
# pivot_table_result = pd.pivot_table(newdf,values=['T5','T6'],
#                columns='KV', aggfunc=['min','mean','max'])
# pivot_table_result = pd.pivot_table(newdf,values=['T5','T6'],
#                columns=['KV','KT'], aggfunc=['min','mean','max'])
# print(pivot_table_result)
#     min                mean                      max
# KV    1    2  2NT         1         2       2NT    1    2  2NT
# T5  3.0  3.2  5.3  6.515000  6.784211  7.233333  9.3  8.9  9.5
# T6  3.7  3.7  5.1  6.743333  7.105263  7.338095  9.0  8.9  9.5
#     min                                                         ...  max
# KV    1                        2            2NT                 ...    1                   2            2NT
# KT    A   A1    B    C   D1    A    C   D1    A   A1    B    C  ...   A1    B    C   D1    A    C   D1    A   A1    B    C   D1
# T5  4.7  7.4  3.5  3.0  3.4  3.2  3.4  5.8  5.8  6.7  7.8  5.3  ...  7.8  8.4  7.9  9.3  8.9  5.4  8.5  8.7  9.5  7.8  9.0  7.4
# T6  4.0  6.4  5.2  3.7  4.9  3.7  4.1  6.0  5.7  6.6  6.9  5.1  ...  7.1  9.0  6.8  8.3  8.9  5.3  8.3  9.4  9.5  6.9  8.5  5.9
# columns='KV': Đây là cột mà bạn muốn sử dụng để phân chia dữ liệu. Trong trường hợp này, sử dụng cột 'KV' để phân chia.
# aggfunc=['min', 'mean', 'max']: Đây là danh sách các hàm tổng hợp  muốn áp dụng lên dữ liệu. Trong trường hợp này,  muốn tính giá trị tối thiểu (min), giá trị trung bình (mean) và giá trị tối đa (max) cho các cột 'T5' và 'T6'.


# Đổi tên cột 
df.rename(columns={
    "TOANLOGICPHANTICH": "LOGIC",
    "GIAIQUYETVANDE": "UNGXU",
    "DINHHUONGNGHENGHIEP": "HUONGNGHIEP"
}, inplace=True)
# print(df.head(10))
# df.dropna(how='all',inplace=True)

# df.drop_duplicates(inplace=True)



# plt.figure(figsize=(10, 6))
# sns.heatmap(df.isna().transpose(), cmap='YlGnBu', cbar_kws={"label": 'Dữ liệu thiếu'})
# plt.title("Ma trận dữ liệu thiếu")
# plt.savefig("missingdata.png", dpi=100)
# plt.show()

# df['DT'].fillna('KINH', inplace=True)

# df['NGONNGU'].fillna(8, inplace=True)

# df['LOGIC'].fillna(df['LOGIC'].mean(), inplace=True)

# df['UNGXU'].fillna(df['UNGXU'].median(), inplace=True)
# Điền giá trị 'KINH' vào các ô trống trong cột 'DT'
df['DT'].fillna('KINH', inplace=True)

df['NGONNGU'].fillna(8, inplace=True)

mean_logic = df['LOGIC'].mean()
df['LOGIC'].fillna(mean_logic, inplace=True)

median_ungxu = df['UNGXU'].median()
df['UNGXU'].fillna(median_ungxu, inplace=True)


df['TBTOAN'] = (df['T5']+df['T6'])/2
df.loc[df['TBTOAN']<5.0,'XEPLOAI'] = 'FAIL'
df.loc[(df['TBTOAN']>=5.0)&(df['TBTOAN']<7.0),'XEPLOAI']='FAIR'
df.loc[(df['TBTOAN']>=7.0)&(df['TBTOAN']<9.0),'XEPLOAI']='GOOD'
df.loc[df['TBTOAN']>9.0,'XEPLOAI'] = 'EXCEL'
print(df.head(10))





















