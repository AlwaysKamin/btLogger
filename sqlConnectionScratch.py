import pymysql

# config = {
#     'user': 'alwayskamin',
#     'password': 'Fay89058',
#     'host': 'db4free.net',
#     'database': 'btlogger',
#     'raise_on_warnings': True,
#     'use_pure': False,
# }

db = pymysql.connect(host='db4free.net', user='alwayskamin', passwd='Fay89058', db='btlogger', port=3307)
cursor = db.cursor()

query = ("SELECT * FROM Room")

data = cursor.execute(query)
for(roomID, buildingName, buildingAddress) in cursor:
    print("{}, {}, {}".format(roomID, buildingName, buildingAddress))
db.close()