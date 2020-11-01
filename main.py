import requests
import time
import mysql.connector

db = mysql.connector.connect(
    host='185.224.137.6',
    user='u235303426_root',
    passwd='S@l4b4d4',
    db='u235303426_bitcoin'
)

while True:
    try:
        response = requests.get('https://indodax.com/api/ticker/btcidr')
        data = response.json()

        bthigh = data['ticker']['high']
        btlow = data['ticker']['low']
        btvolBtc = data['ticker']['vol_btc']
        btvolIdr = data['ticker']['vol_idr']
        btlast = data['ticker']['last']
        btbuy = data['ticker']['buy']
        btsell = data['ticker']['sell']

        cursor = db.cursor()
        sql = "INSERT INTO `datasethour`(`date`, `high`, `low`, `volbtc`, `volidr`, `last`, `buy`, `sell`)" \
              "VALUES (NOW(), %s, %s, %s, %s, %s, %s, %s)"
        val = (bthigh, btlow, btvolBtc, btvolIdr, btlast, btbuy, btsell)
        cursor.execute(sql, val)
        db.commit()

    except mysql.connector.Error as e:
        print(e)

    time.sleep(5)