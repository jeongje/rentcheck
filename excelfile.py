from flask import Flask, render_template, request
app = Flask(__name__)

from openpyxl import load_workbook

EXCEL_FIlE = 'C:\\Users\\82104\\Desktop\\rentcheck\\exfile\\ex.xlsx'

wb = load_workbook(EXCEL_FIlE, data_only=True)
ws1 = wb.worksheets[0]


# 모든 값을 행별로 포함하는 list
# 빈칸이 있는 string을 form으로 넘길 때 적용이 안돼 빈칸 제거
all_values = []
for row in ws1.rows:
    row_value = []
    for cell in row:
        print(type(cell.value))
        if isinstance(cell.value, str):
            row_value.append(cell.value.strip())
        else:
            row_value.append(cell.value)
    all_values.append(row_value)


@app.route('/')
def index():
    return render_template(
        'index.html',
        allValues = all_values,
    )

@app.route('/check', methods = ['POST'])
def check():
    if request.method == 'POST':
        name = request.form['name']
        name_values = []
        for row_values in all_values:
            if name in row_values:
                name_values.append(row_values)
        return render_template(
            'check.html',
            nameValues = name_values,
        )


app.run(port=5000, debug=True)
