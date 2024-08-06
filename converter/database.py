import sqlite3

class Database:
    def __init__(self, db_name='data.db') -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_user(self, username, password):
        self.cursor.execute("INSERT INTO users(username, password) VALUES (?,?)", (username, password))
        self.conn.commit()

    def get_password(self, username):
        query = f"SELECT password FROM users WHERE username = '{username}';"
        print("Executing:", query)
        queried_password = self.cursor.execute(query)
        return queried_password.fetchone()[0]


    def close(self):
        self.conn.close()
