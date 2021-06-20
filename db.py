import sqlite3


def dbConnection():
    conn = sqlite3.connect('test11.db')
    print("Opened database successfully")
    return conn

def createBaseTable(conn):
    conn.execute('''CREATE TABLE ZSCALER_VERSIONS
             (ID INT PRIMARY KEY     NOT NULL,
             VERSION TEXT NOT NULL,
             REMARKS TEXT);''')
    print("Table created successfully")

def getMaxVersion():

def recordNewVersion(conn, version):


def closeConnection(conn):
    conn.close()