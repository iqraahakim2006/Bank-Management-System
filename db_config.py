import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="bank_system"
    )