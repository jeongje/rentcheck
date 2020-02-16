from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbrentcheck

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

@app.route('/tenant')
def tenant():
    return render_template(
        'tenant.html',
    )


@app.route('/tenant/tenants', methods=['POST'])
def save_tenant():
    name_receive = request.form['name']
    phone_receive = request.form['phone']
    memo_receive = request.form['tenant_memo']

    doc = {
        'name': name_receive,
        'phone': phone_receive,
        'memo': memo_receive,
    }

    db.tenants.insert_one(doc)

    return jsonify({'result': 'success'})


@app.route('/tenant/tenants', methods=['GET'])
def view_tenants():
    tenants = list(db.tenants.find({},{'_id':0}))
    return jsonify({'result': 'success', 'tenants': tenants})
    # return render_template(
    #     'tenant.html'
    # )




@app.route('/contract')
def contract():
    return render_template(
        'contract.html',
    )

@app.route('/monthly')
def monthly():
    return render_template(
        'monthly.html',
    )



@app.route('/search', methods = ['POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']
        search_values = []
        for row_values in all_values:
            name_list = [] #이름으로만 검색되게 만들기
            name_list.append(row_values[2])
            if name in name_list: #name_list에 있는 name만 추가하기
                search_values.append(row_values)
        return render_template(
            'search.html',
            searchValues = search_values,
        )


app.run(port=5000, debug=True)
