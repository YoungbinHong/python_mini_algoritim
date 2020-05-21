# open txt file

f = open("./string_split.txt",'r')

my_string = ''

while True:
    line = f.readline()
    if not line: break
    my_string += line

f.close()

# processing

my_list1, my_list2 = list() , list()

my_list1 = my_string.split('\n')

for i in my_list1:
    my_list2.append(i.split(','))

# constant

ROW_LENGTH = len(my_list2)
COLUMN_LENGTH = len(my_list2[0])

# make excel file

from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

for column_index in range(COLUMN_LENGTH):
    for row_index in range(ROW_LENGTH):
        sheet.cell(row=row_index+1,column=column_index+1,value=my_list2[row_index][column_index])

wb.save('string_split.xlsx')
