import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# from scipy import stats


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

df['NGONNGU'].skew()
# print(df[['NGONNGU','LOGIC','UNGXU']].skew())
# NGONNGU    0.333221
# LOGIC      0.472551
# UNGXU      0.607063

# print(df[['NGONNGU']].kurtosis())
# NGONNGU   -0.517004
# print(df[['NGONNGU','LOGIC','UNGXU']].kurtosis())
# NGONNGU   -0.517004
# LOGIC      1.372439
# UNGXU      0.442173

# sns.displot(data = df[['T5','T6']],kind='kde')
# plt.show()

# sns.boxplot(data=df['LOGIC'],orient="h")
# plt.show()

# sns.boxplot(data=df[['NGONNGU','LOGIC','UNGXU']],orient="h")
# plt.show()

# sns.boxplot(x='NGONNGU',y='KT',data=df,orient="h")
# plt.show()

# sns.boxplot(x='KT',y='NGONNGU',hue='GT',data=df)
# plt.show()

# stats.probplot(df['NGONNGU'],plot=sns.mpl.pyplot)
# plt.show()

# cov sắp xếp mức độ tác động 

# print(df[['T5','T6']].corr())

sns.lmplot(data=df,x='T5',y='T6',fit_reg=True)
plt.show()

