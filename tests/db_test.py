# coding: UTF-8

import unittest
import db


class TestAdd(unittest.TestCase):

    def test_db(self):
        #t1 = db.db_connection('localhost', 'root', '', 'mysql')
        #self.assertTrue(t1)

        t2 = db.db_connection('localhost', 'root', '', 'mysql')
        cursor = t2.cursor()
        self.assertTrue(cursor.execute('SELECT * FROM user'))

if __name__ == '__main__':
    unittest.main()