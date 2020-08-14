from pymongo import MongoClient

client = MongoClient('mongodb://172.17.0.3:27017/') # with Docker inspect
mydb = client.mydb # get Database
data = {'title': 'mariaDB 보기', 'tags': ['디비 서비스']}
board_info = mydb.board.insert_one(data)
data = [ {"name": "Ram", "age": "26", "city": "Hyderabad"},{"name": "Rahim", "age": "27", "city": "Bangalore"}]

res = mydb.board.insert_many(data); print(res.inserted_ids)
board_info = mydb.board.find() # get Collection with find()
for info in board_info: # Cursor
    print(info)
client.close()