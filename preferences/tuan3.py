import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = "dulieuxettuyendaihoc.csv"

a = pd.read_csv(file_path,header=0, delimiter=",",encoding='utf-8')
df =a[['T5','T6','GT','DT' ,'KV','KT','NGONNGU','TOANLOGICPHANTICH','GIAIQUYETVANDE','NGAYTHI','DINHHUONGNGHENGHIEP']]

df.rename(columns={
    'TOANLOGICPHANTICH':'LOGIC',
    'GIAIQUYETVANDE':'UNGXU',
    'DINHHUONGNGHENGHIEP':'HUONGNGHIEP'
},inplace=True)
# Xóa các dòng dl rỗng
df.dropna(how='all',inplace=True)
# Xóa các dòng bị trùng 
df.drop_duplicates(inplace=True)

# Dung heatmap de truc quan hoa dl
# plt.figure(figsize=(10, 6))
# sns.heatmap(df.isna().transpose(), cmap='YlGnBu', cbar_kws={"label": 'Dữ liệu thiếu'})
# plt.title("Ma trận dữ liệu thiếu")
# plt.savefig("missingdata.png", dpi=100)
# plt.show()

# Điền giá trị thiếu 
df['DT'].fillna('KINH',inplace=True)
# Lưu ý : với biến định tính ta có thể thay đổi bảng giá trị yếu vị (mode)
#df['DT].fillna(df['DT].mode()[0], inplace=True)

# Điền thiếu giá trị NgonNgu bằng 0 (nếu có)
df['NGONNGU'].fillna(0, inplace=True)
# Điền thiếu giá trị phần logic bằng trung bình nếu có 
df['LOGIC'].fillna(df['LOGIC'].mean(),inplace=True)
# Điền thiếu giá trị phần ứng xử bằng trung vị nếu có 
df['UNGXU'].fillna(df['UNGXU'].median(),inplace=True)

df['TBTOAN'] = (df['T5']+df['T6'])/2

# Tạo biến xếp loại đánh giá
df.loc[df['TBTOAN']< 5.0,'XEPLOAI'] = 'FAIL'
df.loc[(df['TBTOAN']>=5.0)&(df['TBTOAN']<7.0),'XEPLOAI'] = 'FAIR'
df.loc[(df['TBTOAN']>=7.0)&(df['TBTOAN']<9.0),'XEPLOAI'] = 'GOOD'
df.loc[df['TBTOAN']>= 9.0,'XEPLOAI'] = 'EXCEL'

# Tạo biến nhóm khối thi : NHÓM KT THÕA MÃN 
# A1: G1
# C : G3
# D1 : G3
# A : G1
# B: G2
# ..
dict_map = {
    'A1': 'G1',
    'C' : 'G3',
    'D1' : 'G3',
    'A' : 'G1',
    'B': 'G2'
}
df['NHOMKT'] = df['KT'].map(dict_map)

# TẠO BIẾN ĐIỂM CÔNG
# Nếu khối thi thuộc nhóm G1, G2 và TBTOAN >=0.5 thì là 1.0
# Ngược lại thì là 6.0
def fplus(x,y):
    if (x == 'G1' or x =='G2') and (y >= 5.0):
        return 1.0
    else:
        return 0.0
    
df['DIEMCONG'] = list(map(fplus,df['NHOMKT'],df['TBTOAN']))

# ... Phan 4: Phan tich mo tá dinh luong
# Phán tich dinh luong lay trong tám là các bién dinh luong
# нис dich: Mó ta các tri thuc dang án chua ben trong dü liéu, thong qua لا nghia
# cac dai luring mó tá toan hoc/

#mean dễ bị tác động bởi các giá trị bất thường(abnormal)
#mean trung vị cho biết 50% số pt có giá trị > median  và 50% số pt .. median
#không bị tác động bởi abnormal value

#mode ( yếu vị ) cho biết đại đa số pt có gtri là bn 
# 1 1 2 5 1 2 --> mode = 1
#mode khôg bị tác động bởi abnormal

#phân vị : là các đại lượng chứa tập dữ liệu thành p phần có sl bằng nhau --> thường dùng tứ fan vị
#|2QR| = Q3-Q1


# Buai 1: Mo ta bién dinh luong
df['NGONNGU'].describe()
# - G1A1 thich y nghia cac đại lung (them variance)
# count    100.000000
# mean       3.740000
# std        1.424408
# min        1.000000
# 25%        2.500000 Q1
# 50%        3.625000 Q2
# 75%        4.750000 Q3
# max        7.000000

 #max min mean median mode quantile(0.25)
print(f'{df["NGONNGU"].min()} \n {df["NGONNGU"].max()} \n')
print(f'{df["NGONNGU"].mean()} \n {df["NGONNGU"].median()} \n')
print(f'{df["NGONNGU"].mode()} \n')
print(f'{df["NGONNGU"].quantile(0.25)} \n')


# .... range cao ->> biến động cao, là 1 gtri yếu 
# range = max - min  
df['NGONNGU'].max() - df['NGONNGU'].min() 

df['NGONNGU'].quantile(0.75) - df['NGONNGU'].quantile(0.25) 

# độ lêch trung bình 
np.mean(np.abs(df['NGONNGU'] - np.mean(df['NGONNGU'])))
# 1.1600000000000001

# Phương sai 
df['NGONNGU'].var() 
# 2.0289393939393943
#phương sai càng cao, độ biến rộng càng cao

# Độ lệch chuẩn
df['NGONNGU'].std()
# std= căn var 
# 1.424408436488423

# phương pháp để so sánh mức độ biến động của hai hay nhiều biến số 
#Hãy so sánh mức độ ổn định của t5 và t6
print(df[['T5','T6']].mean())
print(df[['T5','T6']].std())
# T5    6.717
# T6    6.937
# dtype: float64
# T5    1.478059
# T6    1.363200
# dtype: float64
#Lưu ý: cần đảm bảo T5 và T6 cùng hệ quy chiếu (độ đo đơn vị so sánh )
# và trung bình t5 t6 sấp sỉ nhau 

# cofficiant of vaniance CV = sdt/mean
#Hãy so sánh mức độ biến động của loic và ngôn ngữ 
df[['LOGIC','NGONNGU']].std()/df[['LOGIC','NGONNGU']].mean()
# LOGIC      0.249131
# NGONNGU    0.38085

# print(df[['NGONNGU','LOGIC','UNGXU']].describe())

#Hướng dẫn tính nhanh CV
cv=df[['NGONNGU','LOGIC','UNGXU']].std()/df[['NGONNGU','LOGIC','UNGXU']].mean()
print(list(cv))
# [0.3808578707188297, 0.2491311130540305, 0.2135664058628459]
#Hãy tính khoảng range cho T5 và  T6

#Đánh giá xem giới tính nào thi tốt hơn 
print(df.groupby('GT')['NGONNGU'].describe())
#     count      mean       std   min     25%   50%  75%  max
# GT
# F    48.0  3.854167  1.348594  1.25  3.1875  3.75  5.0  7.0
# M    52.0  3.634615  1.496288  1.00  2.4375  3.50  4.5  7.0

# df[['T5','T6']].max() - df[['T5','T6']].min()
#Hãy tính độ lệch IQR cho T5 VÀ T6
#Hãy tính độ lệch trung bình cho T5 và T6 
# Tạo một bảng pivot để tính điểm trung bình theo môn thi và giới tính

#Historam là biểu đồ phân phối xác xuất của biến định lượng 
#Mục đích: cho biết xác xuất xảy ra của biến có trong khoảng giá trị dữ liệu nào nhiều nhất 
df['NGONNGU'].hist()
plt.show()

#Hướng dẫn về bins trong historam
#Lưu ý: Khi số lượng bins khác nhau sẽ dẫn đến hình dáng của histogram khác nhau 
df['NGONNGU'].hist(bins=14)
plt.show()

#DISPLOT 
sns.displot(df, x='NGONNGU', kind='kde')
plt.show()

sns.displot(data = df[['NGONNGU','LOGIC','UNGXU']], kind='kde')
plt.show()

sns.displot(df, x='NGONNGU',hue='GT', kind='kde')
plt.show()

# sns.displot(df, x='NGONNGU',hue='GT',kind='kde')
# plt.show()

# print(df.head(10))


