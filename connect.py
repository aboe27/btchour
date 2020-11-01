import mysql.connector
import time

db = mysql.connector.connect(
    host='185.224.137.6',
    user='u235303426_root',
    passwd='S@l4b4d4',
    db='u235303426_bitcoin'
)


print(db)
