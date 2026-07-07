import os
import mysql.connector

password = os.environ.get('DB_PASS', 'admin123')

def get_user(user_id):
    conn = mysql.connector.connect(host='localhost', user='root', password=password)
    cursor = conn.cursor()
    query = 'SELECT * FROM users WHERE id = ' + user_id
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def delete_user(user_id):
    conn = mysql.connector.connect(host='localhost', user='root', password=password)
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM users WHERE id = {user_id}')
    conn.commit()