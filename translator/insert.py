import sqlite3


def insert_user(username, user_id):
    conn = sqlite3.connect('tarjima.db')
    curr = conn.cursor()
    query = "INSERT INTO users (username, user_id) VALUES (?, ?)"
    curr.execute(query, (username, user_id))
    conn.commit()
    conn.close()


def select_user():
    conn = sqlite3.connect('tarjima.db')
    curr = conn.cursor()
    query = "SELECT user_id FROM users"
    result = curr.execute(query, ).fetchall()
    l = []
    for i in result:
        l.append(i[0])
    return l
