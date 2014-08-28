import MySQLdb as mdb

class MySQLAPI(object):
    def __init__(self):
        self.db = mdb.connect(host="mysql.server", user="dimkonko", passwd="dblog",
                         db="dimkonko$BlogDb")

    def add(self):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO post VALUES('', 'Some Title', NOW()," +
                      "'Some big good descr');")