import sqlite3

class User:
    def __init__(self, id, username, password, role, linked_id):
        self.id = id
        self.username = username
        self.password = password
        self.role = role  # "student", "teacher", "admin"
        self.linked_id = linked_id

    def __str__(self):
        return f"User(id={self.id}, username='{self.username}', role='{self.role}', linked_id={self.linked_id})"

    @staticmethod
    def create_table():
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                role TEXT,
                linked_id INTEGER
            );
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (id, username, password, role, linked_id) VALUES (?, ?, ?, ?, ?)",
                  (self.id, self.username, self.password, self.role, self.linked_id))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("""
            UPDATE users
            SET username = ?, password = ?, role = ?, linked_id = ?
            WHERE id = ?
        """, (self.username, self.password, self.role, self.linked_id, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(user_id):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return User(*row)
        return None

    def delete(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def login(username, password):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        row = c.fetchone()
        if row:
            return User(*row)
        return None

    def print_info(self):
        print(f"🔐 User #{self.id}")
        print(f"👤 Username: {self.username}")
        print(f"🛡️ Role: {self.role}")
        print(f"🧷 Linked ID: {self.linked_id}")


















