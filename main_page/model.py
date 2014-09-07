import MySQLdb as mdb

from custom_modules.ConfigLoader import ConfigLoader

class MainModel(object):
    def __init__(self):
        config = ConfigLoader("conf/db_conf.ini").load()
        self.host = config["host"]
        self.user = config["user"]
        self.passwd = config["passwd"]
        self.db = config["db"]

    def conn(self):
        return mdb.connect(host=self.host, user=self.user,
                           passwd=self.passwd, db=self.db)

    def add_post(self, post_form):
        field_list = [val.encode('utf8') for k, val in post_form.iteritems()]
        print field_list

        sql = "INSERT INTO post(title, descr, link, date) " +\
              "VALUES('{0}', '{1}', '{2}', CURDATE());".format(field_list[0],
                field_list[1], field_list[2])
        self._execute_sql(sql)
        return True

    def get_all(self):
        db = self.conn()
        cursor = db.cursor()
        sql = "SELECT * FROM post"
        cursor.execute(sql)
        data_list = cursor.fetchall()
        db.close()
        return data_list

    def _execute_sql(self, sql_string):
        db = self.conn()
        cursor = db.cursor()
        cursor.execute(sql_string)
        db.commit()
        db.close()