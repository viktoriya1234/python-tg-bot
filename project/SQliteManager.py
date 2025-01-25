import sqlite3

class SQLNote:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def __enter__(self):
        self.connect = sqlite3.connect(self.db_path)
        self.cursor = self.connect.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()


