import pymysql


class ReadDB:

    conn = None

    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="960601",
                database="mybatis_plus",
                charset="utf8")
        return self.conn

    def get_cursor(self):
        return self.get_conn().cursor()

    def close_cursor(self, cursor):
        if cursor:
            cursor.close()

    def close_conn(self):
        if self.conn:
            self.get_conn().close()
            self.conn = None

    def get_sql_one(self, sql):
        cursor = None
        result = None
        try:
            cursor = self.get_cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            print('get_sql_one error: ', e)
        finally:
            self.close_cursor(cursor)
            self.close_conn()
            return result

    def get_sql_all(self, sql):
        cursor = None
        result = None
        try:
            cursor = self.get_cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            print('get_sql_all error: ', e)
        finally:
            self.close_cursor(cursor)
            self.close_conn()
            return result

    def update_sql(self, sql):
        cursor = None
        try:
            cursor = self.get_cursor()
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print('get_sql_all error: ', e)
        finally:
            self.close_cursor(cursor)
            self.close_conn()


# cursor = conn.cursor()
# sql = "select name from role where id=1"
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)
# cursor.close()
# conn.close()
