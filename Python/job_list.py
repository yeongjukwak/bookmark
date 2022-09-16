import os
import re


# 메뉴 및 파일 경로만 출력
def print_menu_filename(r_str):
    p = re.compile(r'(\./)(.*?)(\.py)')

    for i in p.finditer(r_str):
        f_path = i.group(0)
        m_name = f_path.split('/')[1]

        print("[menu]: " + m_name + ", [path]: " + f_path)


# 메소드만 출력
def print_method(r_str):
    p = re.compile(r'((\:\{)|\,)([\'\"])(.*?)(\()(.*?)(\)[\'\"])')
    tmp_list = "".join(r_str.split()).split('}{')

    for iterator_data in tmp_list:
        i_obj = p.finditer(iterator_data)

    for i in i_obj:
        print(i.group(0))


file_list = os.listdir('탐색할 디렉토리명')
d_list = []

for filename in file_list:

    file_path = '탐색할 디렉토리명' + filename
    with open(file_path, 'r') as f:
        read_str = f.read()

    # print_menu_filename(read_str)
    # print_method(read_str)

    t_list = "".join(read_str.split()).split('}{')
    for data in t_list:
        if data[0] != '{':
            data = '{' + data

        if data[-2] != '}' and data[-1] == '}':
            data += '}'

        d_list.append(eval(data))

with open('결과값 저장할 csv파일명', 'w') as f:
    for d_data in d_list:
        for key, val in d_data.items():
            v_list = list(val)
            menu = str(key).split('/')[1]

            for m_val in v_list:
                f.write(menu + '!' + key + '!' + m_val + '\n')
