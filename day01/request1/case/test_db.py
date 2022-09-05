import unittest

from request1.tools.read_db import ReadDB


class TestDB(unittest.TestCase):

    def test_get_one(self):
        sql = "select name from role where id=1"
        data = ReadDB().get_sql_one(sql)
        self.assertEqual('ROLE_SUPER_ADMIN', data[0])

    def test_update(self):
        sql = "insert into role(id,name) values (null, 'ROLE_N')"
        result = ReadDB().update_sql(sql)

if __name__ == '__main__':
    unittest.main()
