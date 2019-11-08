import openpyxl

wb = openpyxl.load_workbook('airline1.xlsx')
print(wb)
print(wb.get_sheet_names())
wb.close()

wb = openpyxl.load_workbook('airline1.xlsx')
