'''
Lưu trữ danh sách các hình chữ nhật từ file input.db
Lưu danh sách các hình chữ nhật xuống file output.db theo định dạng
    rong-dai-chuvi-dientich

Lưu ý: Trong các file mỗi hàng là thông tin một hình chữ nhật
'''

import Rectangle as rect

# Tải dữ liệu từ file input_rect.db vào listRectangle
fr = open('../python tuan 2/input_rect.db', mode='r', encoding='utf-8')
listRectangle = []
for line in fr:
    stripLine = line.strip('\n')
    ds = stripLine.split(',')
    cr = float(ds[0])
    cd = float(ds[1])
    hcn = rect.Rectangle(cr, cd)
    listRectangle.append(hcn)
fr.close()

# Ghi dữ liệu từ listRectangle xuống file output_rect.db
fw = open('../python tuan 2/output_rect.db', mode='w', encoding='utf-8')
for item in listRectangle:
    fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
fw.close()