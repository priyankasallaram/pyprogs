import sqlite3
import traceback


def dbConnection():
    try:
        conn = sqlite3.connect('ZscalerClient-versions.db')
        print("Opened database successfully")
        return conn
    except Exception:
        print("Error occured")

def createBaseTable(conn):
    try:
        conn.execute('''CREATE TABLE ZSCALER_VERSIONS
                (VERSION TEXT NOT NULL,
                TYPE TEXT NOT NULL,
                CATEGORY TEXT NOT NULL);''')
        print("Table created successfully")
    except Exception:
        print("Table already exists")

def checkVersion(conn,version,type):
    try:
        cur = conn.cursor()
        cur.execute("SELECT count(*) from ZSCALER_VERSIONS where VERSION = ? and TYPE = ?",(version,type,))
        return cur.fetchone()
    except Exception:
        print("Problem with checkVersion")
    

def recordNewVersion(conn, version, type, category):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO ZSCALER_VERSIONS(VERSION,TYPE,CATEGORY)values(?,?,?)",(version,type,category))
        conn.commit()
        return
    except Exception:
        print("Error Occured in recording new version")
        traceback.print_exc()

def closeConnection(conn):
    try:
        conn.close()
    except Exception:
        print("Error Occured in closing connection")