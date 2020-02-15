from flask import Flask, render_template, request
app = Flask(__name__)

from openpyxl import load_workbook

EXCEL_FIlE = 'C:\\Users\\82104\\Desktop\\rentcheck\\exfile\\ex.xlsx'

wb = load_workbook(EXCEL_FIlE, data_only=True)
ws1 = wb.worksheets[0]


all_values = []
for row in ws1.rows:
    row_value = []
    for cell in row:
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
