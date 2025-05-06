import sqlite3

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
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS students (
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
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("INSERT INTO students (id, name, age, gender, class_id) VALUES (?, ?, ?, ?, ?)",
                  (self.id, self.name, self.age, self.gender, self.class_id))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("""
            UPDATE students
            SET name = ?, age = ?, gender = ?, class_id = ?
            WHERE id = ?
        """, (self.name, self.age, self.gender, self.class_id, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(student_id):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Student(*row)
        return None

    def delete(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("DELETE FROM students WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    def print_info(self):
        print(f"👨‍🎓 Student #{self.id}")
        print(f"📛 Name: {self.name}")
        print(f"🎂 Age: {self.age}")
        print(f"🚻 Gender: {self.gender}")
        print(f"🏫 Class ID: {self.class_id}")

