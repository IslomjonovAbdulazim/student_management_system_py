import sqlite3

class Teacher:
    def __init__(self, id, name, subject):
        self.id = id
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Teacher(id={self.id}, name='{self.name}', subject='{self.subject}')"

    @staticmethod
    def create_table():
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                subject TEXT
            );
        ''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("INSERT INTO teachers (id, name, subject) VALUES (?, ?, ?)",
                  (self.id, self.name, self.subject))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute('''
            UPDATE teachers
            SET name = ?, subject = ?
            WHERE id = ?
        ''', (self.name, self.subject, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(teacher_id):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM teachers WHERE id = ?", (teacher_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Teacher(*row)
        return None

    def delete(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("DELETE FROM teachers WHERE id = ?", (self.id, ))
        conn.commit()
        conn.close()

    def print_info(self):
        print(f"👨‍🏫 Teacher #{self.id}")
        print(f"📛 Name: {self.name}")
        print(f"📚 Subject: {self.subject}")

    @staticmethod
    def get_all():
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM teachers ORDER BY name ASC")
        teachers = [Teacher(*row) for row in c.fetchall()]
        conn.close()
        return teachers

    @staticmethod
    def get_by_subject(subject):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM teachers WHERE subject = ?", (subject,))
        teachers = [Teacher(*row) for row in c.fetchall()]
        conn.close()
        return teachers

    @staticmethod
    def search_by_subject(query):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM teachers WHERE subject LIKE ?", (f"%{query}%", ))
        teachers = [Teacher(*row) for row in c.fetchall()]
        conn.close()
        return teachers

    


























