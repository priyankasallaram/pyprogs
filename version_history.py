from db import checkVersion, closeConnection, createBaseTable, dbConnection, recordNewVersion
import sqlite3

version_mac = "1.2.1.1"
version_win = "1.2.1.11"
conn = dbConnection()
createBaseTable(conn)
id = checkVersion(conn,version_mac,"mac")
print(id[0])
if id[0] == 0:
    recordNewVersion(conn,version_mac,"mac","Not Available")
else:
    print("Version is already available with us")
id = checkVersion(conn,version_win,"mac")
print(id[0])
if id[0] == 0:
    recordNewVersion(conn,version_win,"mac","Not Available")
else:
    print("Version is already available with us")
closeConnection(conn)

