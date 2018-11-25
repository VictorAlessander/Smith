from ..Abstracts.AbstractHandler import AbstractHandler
import sqlite3


@AbstractHandler.register
class HandlerPichauImpl(AbstractHandler):

    def __init__(self, db_name):
        super(HandlerPichauImpl, self).__init__()
        self.db_name = db_name

    def create_database(self):

        try:
            database = sqlite3.connect(self.db_name)

            cursor = database.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(200) NOT NULL,
                normal_price varchar(20) DEFAULT NULL,
                in_cash varchar(20) DEFAULT NULL,
                inserted_date DATE DEFAULT (datetime('now', 'localtime'))
            );
            """)

            database.close()
        except Exception as e:
            raise e

    def store_database(self, values):
        database = sqlite3.connect(self.db_name)

        cursor = database.cursor()
        cursor.execute("""
        INSERT INTO products (name, normal_price, in_cash)
        VALUES (?,?,?)
        """, (values[0], values[1], values[2])
        )

        database.commit()

        database.close()