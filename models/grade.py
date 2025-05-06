import sqlite3

class Grade:
    def __init__(self, id, student_id, subject, score):
        self.id = id
        self.student_id = student_id
        self.subject = subject
        self.score = score  # float

    @staticmethod
    def create_table():
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject TEXT,
                score REAL
            );
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("INSERT INTO grades (id, student_id, subject, score) VALUES (?, ?, ?, ?)",
                  (self.id, self.student_id, self.subject, self.score))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("""
            UPDATE grades
            SET student_id = ?, subject = ?, score = ?
            WHERE id = ?
        """, (self.student_id, self.subject, self.score, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(grade_id):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM grades WHERE id = ?", (grade_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Grade(*row)
        return None

    def delete(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("DELETE FROM grades WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    def print_info(self):
        print(f"📊 Grade Record #{self.id}")
        print(f"👨‍🎓 Student ID: {self.student_id}")
        print(f"📚 Subject: {self.subject}")
        print(f"🏆 Score: {self.score}")
