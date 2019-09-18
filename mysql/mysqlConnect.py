import pymysql


class MysqlConnection(object):
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = 3306

    def mysql_connection(self):
        # 链接数据库
        conn = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database,
                               port=self.port)
        return conn

    def select_all(self, conn, select_sql):
        cur = conn.cursor()
        cur.execute(select_sql)
        select_all = cur.fetchall()
        cur.close()
        return select_all

    def select_one(self, conn, select_sql):
        cur = conn.cursor()
        cur.execute(select_sql)
        select_one = cur.fetchone()
        cur.close
        return select_one

    def insert_one(self, conn, insert_sql):
        cur = conn.cursor()
        try:
            cur.execute(insert_sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        cur.close

    def insert_many(self,conn, insert_sql, data):
        cur = conn.cursor()
        try:
            cur.executemany(insert_sql,data)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        cur.close


if __name__ == '__main__':
    host = '10.0.10.5'
    username = 'tsf'
    password = '123456'
    database = 'tsftest'
    connect = MysqlConnection(host, username, password, database)
    conn = connect.mysql_connection()



