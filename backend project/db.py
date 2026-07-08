import oracledb

connection = oracledb.connect(
    user="system",
    password="Oracle@123",
    dsn="localhost:1521/XEPDB1"
)

cursor = connection.cursor()


connection.commit()

cursor.close()
connection.close()