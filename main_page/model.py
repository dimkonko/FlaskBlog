import sys
import MySQLdb as mdb

from custom_modules.ConfigLoader import ConfigLoader

class MainModel(object):
    def __init__(self):
        self.encoding = "utf-8"
        
        config = ConfigLoader(sys.path[0] + "/conf/db_conf.ini").load()
        self.host = config["host"]
        self.user = config["user"]
        self.passwd = config["passwd"]
        self.db = config["db"]

    def conn(self):
        return mdb.connect(host=self.host, user=self.user,
                           passwd=self.passwd, db=self.db)

    def add_post(self, post_form):
        sql = "INSERT INTO post(title, descr, link, date) " +\
              "VALUES('{0}', '{1}', '{2}', CURDATE());".format(
                    post_form["title"].encode(self.encoding),
                    post_form["descr"].encode(self.encoding),
                    post_form["link"].encode(self.encoding)
                    )
        db = self.conn()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
        return True

    def get_all(self):
        sql = "SELECT * FROM post"

        db = self.conn()
        cursor = db.cursor()
        cursor.execute(sql)
        data_list = cursor.fetchall()
        db.close()

        posts = list()
        for post in data_list:
            e_post = list()
            for item in post:
                if type(item) is str:
                    item = item.decode(self.encoding)
                e_post.append(item)
            posts.append(e_post)
        return posts
