import mysql.connector

config = {
    'user': 'kamin',
    'password': 'MotO8905_8',
    'host': 'bluetoothlogger.cxfbr8mw9rdi.us-east-2.rds.amazonaws.com',
    'database': 'btLog',
    'raise_on_warnings': True,
    'use_pure': False,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT * FROM Room")

data = cursor.execute(query)
for(roomID, buildingName, buildingAddress) in cursor:
    print("{}, {}, {}".format(roomID, buildingName, buildingAddress))
cnx.close()