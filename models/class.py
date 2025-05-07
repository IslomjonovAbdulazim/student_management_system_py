import sqlite3
from utils.app_constants import AppConstants

class Class:
    def __init__(self, id, name, teacher_id):
        self.id = id
        self.name = name
        self.teacher_id = teacher_id

    @staticmethod
    def create_table():
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f'''
            CREATE TABLE IF NOT EXISTS {AppConstants.TABLE_CLASSES} (
                id INTEGER PRIMARY KEY,
                name TEXT,
                teacher_id INTEGER
            );
        ''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"INSERT INTO {AppConstants.TABLE_CLASSES} (id, name, teacher_id) VALUES (?, ?, ?)",
                  (self.id, self.name, self.teacher_id))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f'''
            UPDATE {AppConstants.TABLE_CLASSES}
            SET name = ?, teacher_id = ?
            WHERE id = ?
        ''', (self.name, self.teacher_id, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(class_id):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {AppConstants.TABLE_CLASSES} WHERE id = ?", (class_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Class(*row)
        return None

    def delete(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"DELETE FROM {AppConstants.TABLE_CLASSES} WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    def print_info(self):
        print(f"🏫 Class #{self.id}")
        print(f"📘 Name: {self.name}")
        print(f"👨‍🏫 Teacher ID: {self.teacher_id}")
