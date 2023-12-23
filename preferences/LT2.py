import pandas as pd
import seaborn as sns


df = pd.read_csv('..\data\dulieuxettuyendaihoc.csv', header = 0, delimiter = ',', encoding = 'UTF-8')
# print(df.head(5))

# #đổi tên cột 
# df.rename(columns = {'TOANLOGICPHANTICH':'LOGIC','GIAIQUYETVANDE':'UNGXU','DINHHUONGNGHENGHIEP':'HUONGNGHIEP'},inplace= True)
# print(df.columns)

# df=df[['T5','T6','GT','DT','KV','KT','NGONNGU','LOGIC','UNGXU','NGAYTHI','HUONGNGHIEP']]
# print(df.head(5))

# #? XÓa dòng rỗng
# df = df.dropna(how = 'all', inplace= True)

# # ?xóa dòng trùng
# df.drop_duplicates(inplace=True)

#! Dùng heat map để trực quan hóa dữ liệu thiếu
import matplotlib.pyplot as plt
# plt.figure(figsize = (10,6)) # đặt kích thước cho biểu đồ
# sns.heatmap(df.isna().transpose(), cmap='YlGnBu', cbar_kws={'label': 'Dữ liệu thiếu'})
# # cmap: màu sắc
# plt.savefig('missingdata.png', dpi = 100)
# plt.show()

#? Điền giá trị thiếu
# df['DT'].fillna('KINH',inplace=True)
#! Lưu ý với biến định tính ta có thể thay bằng giá trị yếu vị(mode)
# df['DT'].fillna(df['DT'].mode()[0],inplace=True)

#Điền thiêu giá trị phần NGONNGU bằng 0
# df['NGONNGU'].fillna(0,inplace=True)
# # Bằng phần tử trung bình
# df['LOGIC'].fillna(df['LOGIC'].mean(),inplace=True)
# #bằng trung vị
# df['UNGXU'].fillna(df['UNGXU'].median(),inplace=True)
# #!Lưu ý với biến định lượng thì ta nên thay bằng trung vị

# #? INTERPOLATE (NỘI SUY) dùng cho dữ liệu có tính tuần tự
# df['T6'].interpolate(method='linear', inplace=True)

#!--------------------------KỸ THUẬT FEATURE ENGINEERING
''' (thường dùng cho Machine Learning)
 Nếu địa chỉ là xử lí phân tích dữ liệu thì ta gọi là New Attribute '''
 
 # ?Tạo biến TBTOAN: Trung bình toán lớp 12
# df['TBTOAN']=(df['T5']+df['T6']/2)

# ?Tạo biến XEPLOAI: Đánh giá môn toán dựa trên df['TBTOAN']

# df.loc[df['TBTOAN'] < 5.0, 'XEPLOAI'] = 'FAIL'
# df.loc[(df['TBTOAN'] >= 5.0) & (df['TBTOAN'] < 7.0), 'XEPLOAI'] = 'FAIL'
# df.loc[(df['TBTOAN'] >= 7.0) & (df['TBTOAN'] < 9.0), 'XEPLOAI'] = 'GOOD'
# df.loc[df['TBTOAN'] >= 9.0, 'XEPLOAI'] = 'EXCEL'

# print(df[['TBTOAN','XEPLOAI']].head(5))


# ?Tạo biến số nhóm khối thi
# dict_map={'A1':'G1','C':'G3','D1':'G3','A':'G1','B':'G2'}

# df['NHOMKT']=df['KT'].map(dict_map)
# print(df.head(5))

# ?Tạo biến số điểm cộng: CONG
# def flus(x,y):
#         if(x=='G1'or x=='G2') and (y>=5.0):
#             return 1.0
#         else:
#             return 0.0
        
# df['CONG']=list(map(flus,df['NHOMKT'],df['TBTOAN']))
# print(df[['NHOMKT','TBTOAN','CONG']].head(5))

#!-----------------------------------TRỰC QUAN HÓA DỮ LIỆU
''' Để trực quan số liệu ta cần lưu ý
# Mục đích: Tổng hợp dữ liệu, biểu diễn dữ liệu bằng hinh anh, dễ hiểu, sinh động
# Kỹ năng: sự phối hợp giữa các loại biến ( định tính, định lượng)
# https://www.tapclicks.com/resources/blog/data-visualization-types/'''

# ? trực quan hóa học sinh theo giới tính
# sns.countplot(x='GT',data=df)
# plt.show()

# ?Làm tương tự cho DT,NHOMKT
# sns.countplot(x='DT',data=df)
# plt.show()

# sns.countplot(x='NHOMKT',data=df)
# plt.show()

#? so sánh số lượng học sinh đăng thí khối thi dựa theo giới tính
# sns.countplot(x='KT',hue='GT',data=df)
# plt.show()

#? sinh viên làm tương tự cho các nhóm biến định tính KV,KT 
#? Cho biết khối A khu vực nào đăng kí cao nhất
# sns.countplot(x='KT',hue='KV',data=df)
# plt.show()
'''tham số hue được sử dụng để tạo sự phân chia màu sắc (color grouping) trong biểu đồ cột dựa trên một biến phân loại khác'''

# #? So sánh điểm trung bình NGONNGU theo nhóm giới tính
# sns.barplot(x='GT',y='NGONNGU',data=df,errorbar= None)
# plt.show()
'''
- (Barplot) là một loại biểu đồ thống kê sử dụng các cột dọc để biểu diễn dữ liệu
- errorbar=None: Tham số này cho biết bạn không muốn hiển thị các thanh lỗi (error bars) trên biểu đồ. - Thanh lỗi thường được sử dụng để hiển thị sự biến động hoặc độ tin cậy của dữ liệu.
ci="sd": Hiển thị thanh lỗi dựa trên độ lệch chuẩn (standard deviation).
ci="sem": Hiển thị thanh lỗi dựa trên sai số tiêu chuẩn (standard error of the mean).
ci=None: Không hiển thị thanh lỗi.

'''


##? So sánh trung bình điểm Logic theo NHOMKT
# sns.barplot(x='NHOMKT',y='LOGIC',data=df,errorbar=None)
# plt.show()

##? so sánh trung bình ngôn ngữ theo nhóm giới tính dựa theo các khối thi
# sns.barplot(x='GT',y='NGONNGU',hue='KT',data=df,errorbar=None)
# plt.show()


''' 
- Nếu bạn muốn hiển thị điểm trung bình của biến A cho từng nhóm của biến B, bạn nên sử dụng barplot.
 - Nếu bạn muốn hiển thị số lượng các mục khác nhau trong mỗi nhóm của biến B, bạn nên sử dụng countplot.'''
 
#  ##?so sánh sai số trên NGONNGU theo nhóm GT theo phân loại khối thi
sns.barplot(x='GT',y='NGONNGU',hue='KT',data=df)
plt.show()

# Sử dụng hàm median để tính giá trị trung vị
# sns.barplot(x='GT', y='NGONNGU', hue='KT', data=df, estimator= 'median')
# # Hiển thị biểu đồ
# plt.show()

#? So sánh điểm cao nhất của NGONGU theo nhóm giới tính theo KT 
#! Lưu ý không để estimator thì mặc định là mean(trung binh)
# print(df.columns)
# sns.barplot(x='GT',y='NGONNGU',hue='KT',data=df,errorbar=None, estimator=max)
# plt.show()

#!Khi biến định dùng để làm nhóm tổng hợp
'''có nhiều hơn 2 giá trị hoặc có giá trị thiều của NGONNGU 
# # thì ta cần dùng hàm tổng hợp thông qua thư viên numpy'''
import numpy as np
# sns.barplot(x='KV',y='NGONNGU',hue='KT',data=df,errorbar=None, estimator=np.max)
# plt.show()

# #?Trực quan dữ liệu theo nhóm tỉ lệ phần trăm
# gb=df.groupby(['KT'])['KT'].aggregate(['count'])
# labels=gb.index #labels=['A','A1','B','C','D1']
# data=list(gb['count'])
# colors=sns.color_palette('pastel')
# plt.pie(data,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True)
# plt.show()

# #?Trung bình ngon ngu theo thời kì thi
# sns.lineplot(x='NGAYTHI',y='NGONNGU',data=df)
# plt.show()

# #?điểm ngon ngu lớn nhất
# sns.lineplot(x='NGAYTHI',y='NGONNGU',data=df,estimator=np.max)
# plt.show()

# #?điểm ngon ngu lớn nhất theo các năm trên từng nhón giới tính
# sns.lineplot(x='NGAYTHI',y='NGONNGU',hue='GT',data=df,estimator=np.max)
# plt.show()