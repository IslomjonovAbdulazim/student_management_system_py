import sqlite3

class Attendance:
    def __init__(self, id, student_id, date, status):
        self.id = id
        self.student_id = student_id
        self.date = date  # format: "YYYY-MM-DD"
        self.status = status  # "Present" or "Absent"

    @staticmethod
    def create_table():
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                date TEXT,
                status TEXT
            );
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("INSERT INTO attendance (id, student_id, date, status) VALUES (?, ?, ?, ?)",
                  (self.id, self.student_id, self.date, self.status))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("""
            UPDATE attendance
            SET student_id = ?, date = ?, status = ?
            WHERE id = ?
        """, (self.student_id, self.date, self.status, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(attendance_id):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("SELECT * FROM attendance WHERE id = ?", (attendance_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Attendance(*row)
        return None

    def delete(self):
        conn = sqlite3.connect("school.db")
        c = conn.cursor()
        c.execute("DELETE FROM attendance WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    def print_info(self):
        print(f"📝 Attendance Record #{self.id}")
        print(f"👨‍🎓 Student ID: {self.student_id}")
        print(f"📅 Date: {self.date}")
        print(f"📌 Status: {self.status}")
