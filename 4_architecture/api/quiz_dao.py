import sqlite3


class AnswerDAO:
    def __init__(self):
        self.database = '/tmp/quiz.db'
        sql = '''CREATE TABLE QUIZ (id INTEGER PRIMARY KEY,
                                      question_id INT NOT NULL,
                                      user_name text NOT NULL,
                                      answer INT NOT NULL);'''
        with self.create_connection() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
            except Exception as error:
                print(error)

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database)
        except Exception as e:
            print(e)
        return conn

    def create_answer(self, question_id, user_name, answer):
        sql = ''' INSERT INTO QUIZ (question_id, user_name, answer) 
        VALUES(?,?,?) '''
        with self.create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, (question_id, user_name, answer))
            conn.commit()

    def count_answers_by_id(self, question_id: int):
        sql = ''' SELECT * FROM QUIZ WHERE question_id=?'''
        with self.create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, (question_id,))
            rows = cur.fetchall()
            return len(rows)
