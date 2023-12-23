'''
(*) Sinh viên tự thực hành
Viết chương trình menu
1- Đọc dữ liệu từ file input.db
2- Thêm mới hình chữ nhật
3- Hiển thị danh sách hình chữ nhật
4- Lưu danh sách hình chữ nhật xuống file demo4output.db
Others- Thoát
'''

import Rectangle as rect

menu_options = {
    1: 'Đọc dữ liệu từ file input_rect.db',
    2: 'Thêm mới hình chữ nhật',
    3: 'Hiển thị danh sách hình chữ nhật',
    4: 'Lưu danh sách hình chữ nhật xuống file output_rect.db',
    'Others': 'Thoát chương trình'
}

def print_menu():
    print('\n----------------------')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    print('------------------------')

# Khai báo biến lưu trữ các hình chữ nhật
dsHCN = []

while (True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input('Nhập tùy chọn: '))
    except:
        print('Nhập sai định dạng. Vui lòng nhập lại !')
        continue

    # Check what choice was entered and act accordingly
    if userChoice == 1:
        fr = open('../python tuan 2/input_rect.db', mode='r', encoding='utf-8')
        print('Đang đọc dữ liệu ...')
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            cr = float(ds[0])
            cd = float(ds[1])
            hcn = rect.Rectangle(cr, cd)
            dsHCN.append(hcn)
        fr.close()
        print('Đã đọc dữ liệu xong')
    elif userChoice == 2:
        cr = float(input('Nhập chiều rộng: '))
        cd = float(input('Nhập chiều dài: '))
        hcn = rect.Rectangle(cr, cd)
        dsHCN.append(hcn)
    elif userChoice == 3:
        for item in dsHCN:
            item.display()
    elif userChoice == 4:
        print('Đang ghi vào file output_rect.db')
        fw = open('../python tuan 2/output_rect.db', mode='r', encoding='utf-8')
        for item in dsHCN:
            fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
        fw.close()
        print('Đã ghi file xong')
    else:
        print('Kết thúc chương trình. BYE !')
        break