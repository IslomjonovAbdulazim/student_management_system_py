import sqlite3

class Class:
    def __init__(self, id, name, teacher_id):
        self.id = id
        self.name = name
        self.teacher_id = teacher_id

    @staticmethod
    def create_table():
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY,
                name TEXT,
                teacher_id INTEGER
            );
        ''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("INSERT INTO classes (id, name, teacher_id) VALUES (?, ?, ?)",
                  (self.id, self.name, self.teacher_id))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute('''
            UPDATE classes
            SET name = ?, teacher_id = ?
            WHERE id = ?
        ''', (self.name, self.teacher_id, self.id))

    @staticmethod
    def get_by_id(class_id):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM classes WHERE id = ?", (class_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Class(*row)
        return None

    def delete(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("DELETE FROM classes WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    def print_info(self):
        print(f"🏫 Class #{self.id}")
        print(f"📘 Name: {self.name}")
        print(f"👨‍🏫 Teacher ID: {self.teacher_id}")













