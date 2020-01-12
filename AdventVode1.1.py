import xlrd
import math

location = (r"C:\Users\christoffer\Desktop\ThisFolder\Bok.xlsx")

wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

list = []

for i in range(sheet.nrows):
    roundDownValue = math.floor(sheet.cell_value(i, 0))
    while roundDownValue >= 0:
        roundDownValue = math.floor(roundDownValue / 3 - 2)
        list.append(roundDownValue)
        for item in list:
            if item < 0:
                list.remove(item)

print('LIST:', list)
print('SUM:', sum(list))
