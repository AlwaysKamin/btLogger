import pymysql
import globalVars

class dbMod:
    def __init__(self):
        con = pymysql.connect(host=globalVars.hostname, user=globalVars.username, passwd=globalVars.password, db=globalVars.db, port=globalVars.port)
        self.cursor = con.cursor()

    def closeConnection(self):
        print("Closing Connection...")

    def showVersion(self):
        self.cursor.execute("SELECT VERSION()")
        return self.cursor.fetchone()


    # def create():



    # def add(newAddr, newName):


    # def display():