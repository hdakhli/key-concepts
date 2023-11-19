import logging
import sqlite3
from sqlite3 import OperationalError


class QuizDAO:
    def __init__(self):
        self.database = 'quiz.db'
        sql = '''CREATE TABLE QUIZ (question_id INT NOT NULL,
                                    user_name text NOT NULL,
                                    answer_id INT NOT NULL,
                                    PRIMARY KEY (question_id, user_name));'''
        try:
            with self._create_connection() as conn:
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
        except OperationalError as error:
            logging.error("Database error", error.args)

    def _create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database)
        except Exception as e:
            print(e)
        return conn

    def create_answer(self, question_id, user_name, answer_id):
        sql = ''' INSERT INTO QUIZ (question_id, user_name, answer_id) 
        VALUES(?,?,?) '''
        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, (question_id, user_name, answer_id))
            conn.commit()

    def count_answers_by_id(self, question_id: int):
        sql = ''' SELECT * FROM QUIZ WHERE question_id=?'''
        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, (question_id,))
            rows = cur.fetchall()
            print(f"rows: {rows}")
            return len(rows)

    def update_answer(self, question_id: int, user_name, answer_id):
        sql = ''' UPDATE QUIZ SET answer_id=? WHERE question_id=? AND user_name=?'''
        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, (answer_id, question_id, user_name))
            conn.commit()

    def get_all_answers(self):
        sql = ''' SELECT * FROM QUIZ '''
        with self._create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            return rows
