from db import closeConnection, createBaseTable, dbConnection
import sqlite3

conn = dbConnection()
createBaseTable(conn)
closeConnection(conn)

