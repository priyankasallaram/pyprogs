import sqlite3


def dbConnection():
    conn = sqlite3.connect('test111.db')
    print("Opened database successfully")
    return conn

def createBaseTable(conn):
    conn.execute('''CREATE TABLE ZSCALER_VERSIONS
             (ID INT PRIMARY KEY     NOT NULL,
             VERSION TEXT NOT NULL,
             REMARKS TEXT);''')
    print("Table created successfully")

def getMaxVersion():
    return 

def recordNewVersion(conn, id, version, remarks):
    sql = "INSERT INTO ZSCALER_VERSIONS(ID,VERSION,REMARKS)values(?,?,?)"
    cur = conn.cursor()
    cur.execute(sql,(id,version,remarks))
    conn.commit()
    return

def closeConnection(conn):
    conn.close()