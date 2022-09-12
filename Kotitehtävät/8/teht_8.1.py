import mysql.connector


def airport_search(gps_code):
    sql = "select name, municipality from airport where gps_code = '\"" + gps_code + "\"';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

ICAO_Code = input("Anna ICAO koodi: ").upper()
airport = airport_search(ICAO_Code)

if not airport:
    print("Et syöttänyt kunnollista ICAO-koodia!")

else:
    for i in airport:
        print(f"{i[0]}: {i[1]}")
