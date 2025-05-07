import sqlite3
from utils.app_constants import AppConstants

class Attendance:
    def __init__(self, id, student_id, date, status):
        self.id = id
        self.student_id = student_id
        self.date = date  # format: "YYYY-MM-DD"
        self.status = status  # "Present" or "Absent"

    @staticmethod
    def create_table():
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            CREATE TABLE IF NOT EXISTS {AppConstants.TABLE_ATTENDANCE} (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                date TEXT,
                status TEXT
            );
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            INSERT INTO {AppConstants.TABLE_ATTENDANCE} (id, student_id, date, status)
            VALUES (?, ?, ?, ?)
        """, (self.id, self.student_id, self.date, self.status))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"""
            UPDATE {AppConstants.TABLE_ATTENDANCE}
            SET student_id = ?, date = ?, status = ?
            WHERE id = ?
        """, (self.student_id, self.date, self.status, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(attendance_id):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {AppConstants.TABLE_ATTENDANCE} WHERE id = ?", (attendance_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Attendance(*row)
        return None

    def delete(self):
        conn = sqlite3.connect(AppConstants.DB_NAME)
        c = conn.cursor()
        c.execute(f"DELETE FROM {AppConstants.TABLE_ATTENDANCE} WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    def print_info(self):
        print(f"📝 Attendance Record #{self.id}")
        print(f"👨‍🎓 Student ID: {self.student_id}")
        print(f"📅 Date: {self.date}")
        print(f"📌 Status: {self.status}")
