import oracledb
def get_connection():
    connection= oracledb.connect(
    user="system",
    password="Oracle@123",
    dsn="localhost:1521/XE"
)
    return connection