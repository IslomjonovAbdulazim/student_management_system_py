import sqlite3
from utils.app_constants import AppConstants

class Student:
    def __init__(self, id, name, age, gender, class_id):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.class_id = class_id

    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}', age={self.age}, gender='{self.gender}', class_id={self.class_id})"

    @staticmethod
    def create_table():
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            CREATE TABLE IF NOT EXISTS {AppConstants.TABLE_STUDENTS} (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                gender TEXT,
                class_id INTEGER
            );
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            INSERT INTO {AppConstants.TABLE_STUDENTS} (id, name, age, gender, class_id)
            VALUES (?, ?, ?, ?, ?)
        """, (self.id, self.name, self.age, self.gender, self.class_id))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            UPDATE {AppConstants.TABLE_STUDENTS}
            SET name = ?, age = ?, gender = ?, class_id = ?
            WHERE id = ?
        """, (self.name, self.age, self.gender, self.class_id, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(student_id):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {AppConstants.TABLE_STUDENTS} WHERE id = ?", (student_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Student(*row)
        return None

    def delete(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"DELETE FROM {AppConstants.TABLE_STUDENTS} WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    def print_info(self):
        print(f"👨‍🎓 Student #{self.id}")
        print(f"📛 Name: {self.name}")
        print(f"🎂 Age: {self.age}")
        print(f"🚻 Gender: {self.gender}")
        print(f"🏫 Class ID: {self.class_id}")
