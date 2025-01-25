import mysql.connector

def get_database_connection():
    db_config = {
        'user': 'your_user',
        'password': 'your_password',
        'host': 'localhost',
        'database': 'your_database',
    }
    return mysql.connector.connect(**db_config)
