# coding: UTF-8


import MySQLdb as mysql


def db_connection(host, user, passwd, db):
    try:
        db = mysql.connect(host=host, user=user, passwd=passwd, db=db)

        cursor = db.cursor()

        return db

    except mysql.OperationalError:
        raise mysql.OperationalError("O banco de dados não existe")