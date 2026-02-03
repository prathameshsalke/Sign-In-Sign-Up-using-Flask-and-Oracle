import oracledb

def get_connection():
    return oracledb.connect(
        user="system",
        password="Tejas@123",
        dsn="localhost/XEPDB1"
    )
