import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=HASSOBINEMRE\\SQLEXPRESS;'  # Bilgisayarındaki server adı
        'DATABASE=TinyHouseDB;'
        'Trusted_Connection=yes;'           # Windows Authentication
    )
    return conn
