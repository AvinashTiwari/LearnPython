import openpyxl

wb = openpyxl.load_workbook('airline1.xlsx')
print(wb)
print(wb.sheetnames)
sheet = wb['Sheet1']
print(sheet)
active = wb.active
print(active)
print(active.title)
print(active['A1'])
print(active['A1'].value)

print(sheet['A1':'C5'])



for  row in sheet['A1':'C5']:
    for cell in row:
        print(cell.value)
    print('\n')