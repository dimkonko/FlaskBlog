import sys
import MySQLdb as mdb

from custom_modules.ConfigLoader import ConfigLoader

class MainModel(object):
    def __init__(self):
        config = ConfigLoader(sys.path[0] + "/conf/db_conf.ini").load()
        self.host = config["host"]
        self.user = config["user"]
        self.passwd = config["passwd"]
        self.db = config["db"]

    def conn(self):
        return mdb.connect(host=self.host, user=self.user,
                           passwd=self.passwd, db=self.db)

    def add_post(self, post_form):
        for key, value in post_form.iteritems():
            value = value.encode('utf8')
        print post_form

        sql = "INSERT INTO post(title, descr, link, date) " +\
              "VALUES('{0}', '{1}', '{2}', CURDATE());".format(post_form["title"],
                post_form["descr"], post_form["link"])
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