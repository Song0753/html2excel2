
# HTML to excel
import os
from html2excel2 import ExcelParser

# table을 html로 만든 폴더 경로
folder_path = 'D:/SHY/KIST/1.Research/OER project/Table 추출/data/performance_table_html_2406'
file_list = os.listdir(folder_path)
print(file_list)
for file_name in file_list:
    try:
        input_file = 'D:/SHY/KIST/1.Research/OER project/Table 추출/data/performance_table_html_2406/'+str(file_name)
        output_file = 'D:/SHY/KIST/1.Research/OER project/Table 추출/data/merged_cell_parse_excel/'+str(file_name[:-5])+'.xlsx'
        parser = ExcelParser(input_file)
        parser.to_excel(output_file)
    except:
        print(f'error occurred in{input_file}')
