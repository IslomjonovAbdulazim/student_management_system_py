import sqlite3
from utils.app_constants import AppConstants

class User:
    def __init__(self, username, password, role, linked_id, id=None):
        self.id = id
        self.username = username
        self.password = password
        self.role = role  # "student", "teacher", "admin"
        self.linked_id = linked_id

    def __str__(self):
        return f"User(id={self.id}, username='{self.username}', role='{self.role}', linked_id={self.linked_id})"

    @staticmethod
    def create_table():
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            CREATE TABLE IF NOT EXISTS {AppConstants.TABLE_USERS} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                role TEXT,
                linked_id INTEGER
            );
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            INSERT INTO {AppConstants.TABLE_USERS} (username, password, role, linked_id)
            VALUES (?, ?, ?, ?)
        """, (self.username, self.password, self.role, self.linked_id))
        self.id = c.lastrowid  # Capture auto-generated ID
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            UPDATE {AppConstants.TABLE_USERS}
            SET username = ?, password = ?, role = ?, linked_id = ?
            WHERE id = ?
        """, (self.username, self.password, self.role, self.linked_id, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(user_id):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {AppConstants.TABLE_USERS} WHERE id = ?", (user_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return User(row[1], row[2], row[3], row[4], row[0])  # Reordered for constructor
        return None

    def delete(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"DELETE FROM {AppConstants.TABLE_USERS} WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def login(username, password):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {AppConstants.TABLE_USERS} WHERE username = ? AND password = ?", (username, password))
        row = c.fetchone()
        conn.close()
        if row:
            return User(row[1], row[2], row[3], row[4], row[0])
        return None

    def print_info(self):
        print(f"🔐 User #{self.id}")
        print(f"👤 Username: {self.username}")
        print(f"🛡️ Role: {self.role}")
        print(f"🧷 Linked ID: {self.linked_id}")

    @staticmethod
    def get_all():
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {AppConstants.TABLE_USERS} ORDER BY username ASC")
        users = [User(row[1], row[2], row[3], row[4], row[0]) for row in c.fetchall()]
        conn.close()
        return users
