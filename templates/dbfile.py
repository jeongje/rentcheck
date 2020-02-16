from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbrentcheck

doc = {
    'name': "test3",
    'phone': "010-0000-0000",
    'tenant_memo': "테스트",
}



db.tenats.drop()

