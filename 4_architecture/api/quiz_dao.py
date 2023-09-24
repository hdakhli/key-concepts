import sqlite3


class QuizDAO:
    def __init__(self):
        self.database = 'quiz.db'
        sql = '''CREATE TABLE QUIZ (id INTEGER PRIMARY KEY,
                                      question_id INT NOT NULL,
                                      user_name text NOT NULL,
                                      answer_id INT NOT NULL);'''
        with self.create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database)
        except Exception as e:
            print(e)
        return conn

    def create_answer(self, question_id, user_name, answer_id):
        sql = ''' INSERT INTO QUIZ (question_id, user_name, answer_id) 
        VALUES(?,?,?) '''
        with self.create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, (question_id, user_name, answer_id))
            conn.commit()

    def count_answers_by_id(self, question_id: int):
        sql = ''' SELECT * FROM QUIZ WHERE question_id=?'''
        with self.create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, (question_id,))
            rows = cur.fetchall()
            print(f"rows: {rows}")
            return len(rows)
