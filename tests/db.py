# coding: UTF-8


import MySQLdb as mysql


def db_connection(host, user, passwd, db):
    
    try:
        db = mysql.connect(host=host, user=user,
                        passwd=passwd, db=db)

        cursor = db.cursor()
        cursor.execute("SELECT * FROM user")
        #data = cursor.fetchall()

        return db

        db.close()
        #for row in data:
        #    return row[0], row[1], row[2]

    except mysql.OperationalError:
        raise mysql.OperationalError("O banco de dados não existe")