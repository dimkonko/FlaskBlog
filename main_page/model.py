import MySQLdb as mdb

class MainModel(object):
    def conn(self):
        return mdb.connect(host="mysql.server", user="dimkonko",
                           passwd="dblog", db="dimkonko$BlogDb")

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
        #new_list = [list(i) for i in data_list]
        db.close()
        return data_list

    def _execute_sql(self, sql_string):
        db = self.conn()
        cursor = db.cursor()
        cursor.execute(sql_string)
        db.commit()
        db.close()