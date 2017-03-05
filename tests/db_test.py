# coding: UTF-8

import unittest
import db


class TestMysql(unittest.TestCase):

    def setUp(self):
        self.connection = db.db_connection('localhost', 'vagr', 'administrador', 'smith')
        self.assertTrue(self.connection)

        self.cursor = self.connection.cursor()
        self.assertTrue(self.cursor)

    #def test_tablecontent(self):
    #    self.content = self.cursor.execute('SELECT * FROM products')
    #    self.assertTrue(self.content)

    def tearDown(self):
        self.connection.close()


if __name__ == '__main__':
    unittest.main()
