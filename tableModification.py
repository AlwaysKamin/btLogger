import MySQLdb as mDB


def create():
    # Connects with database, sets up a cursor as well
    con = mDB.connect(host='localhost', port=3306, user='root', passwd='MotO8905_8', db='employees')
    with con:
        cur = con.cursor()

    # Drops any previous table
    # TODO GIVE THE USER THE OPTION TO DROP TABLE OR ADD ON
    cur.execute("DROP TABLE IF EXISTS emp_log")

    # CREATES THE TABLE with the values Id, Device ID, and employee name
    cur.execute("CREATE TABLE emp_log (`Id` INT PRIMARY KEY AUTO_INCREMENT,`Device_ID` VARCHAR(25) NOT NULL , `emp_name` VARCHAR (25) NOT NULL, `ts` TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    # Closes the connection
    con.close()


def add(newAddr, newName):

    # Connects with database, sets up a cursor as well
    con = mDB.connect(host='localhost', port=3306, user='root', passwd='MotO8905_8', db='employees')
    with con:
        cur = con.cursor()

    # Adds each device into the table, and adds the time behind the scenes as well
    cur.execute("INSERT INTO emp_log(Device_ID, emp_name) VALUES ('%s', '%s')" % (newAddr, newName))

    # Saves changes
    con.commit()

    # Closes Connection
    con.close()


def display():

    # Connects with database, sets up a cursor as well
    con = mDB.connect(host='localhost', port=3306, user='root', passwd='MotO8905_8', db='employees')
    with con:
        cur = con.cursor()

    # Output data
    cur.execute("SELECT * FROM `emp_log`")
    rows = cur.fetchall()

    for row in rows:
        print row

    # Close Connection
    con.close()
