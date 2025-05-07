import sqlite3
from utils.app_constants import AppConstants

class Grade:
    def __init__(self, id, student_id, subject, score):
        self.id = id
        self.student_id = student_id
        self.subject = subject
        self.score = score  # float

    @staticmethod
    def create_table():
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            CREATE TABLE IF NOT EXISTS {AppConstants.TABLE_GRADES} (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject TEXT,
                score REAL
            );
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"INSERT INTO {AppConstants.TABLE_GRADES} (id, student_id, subject, score) VALUES (?, ?, ?, ?)",
                  (self.id, self.student_id, self.subject, self.score))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            UPDATE {AppConstants.TABLE_GRADES}
            SET student_id = ?, subject = ?, score = ?
            WHERE id = ?
        """, (self.student_id, self.subject, self.score, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(grade_id):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {AppConstants.TABLE_GRADES} WHERE id = ?", (grade_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Grade(*row)
        return None

    def delete(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"DELETE FROM {AppConstants.TABLE_GRADES} WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    def print_info(self):
        print(f"📊 Grade Record #{self.id}")
        print(f"👨‍🎓 Student ID: {self.student_id}")
        print(f"📚 Subject: {self.subject}")
        print(f"🏆 Score: {self.score}")
