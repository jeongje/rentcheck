# https://openpyxl.readthedocs.io/en/stable/

from openpyxl import load_workbook

wb = load_workbook('C:\\Users\\82104\\Desktop\\rentcheck\\exfile\\ex.xlsx', data_only=True)
ws = wb['Sheet1']

print(wb.sheetnames[0])
print(ws['A1'].value)
print(ws.rows)

all_values = []
for row in ws.rows:
    row_value = []
    for cell in row:
        row_value.append(cell.value)
    all_values.append(row_value)

print(all_values)