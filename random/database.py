import sqlite3
import datetime
class con:
    def connection(self):
        self.date = datetime.datetime.now()
        self.q = 'INSERT INTO IMGDATA(DATE, LINK, TITLE) VALUES(?, ?, ?)'
        self.connection_created = sqlite3.connect("nasabase.db")
    def create(self):
        self.cursor = self.connection_created.cursor()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS IMGDATA(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DATE TEXT NOT NULL,
            LINK TEXT NOT NULL UNIQUE,
            TITLE TEXT NOT NULL UNIQUE
            )
            '''
        )
    def input2(self, url, title):
            try:
                self.cursor.execute(self.q, (self.date, url, title))
                self.connection_created.commit()
                print("done")
            except sqlite3.IntegrityError as e:
                print("an error took place in inserting database(just ignore this nothing much): "+ str(e))
    def delete(self,id):
        self.cursor.execute('DELETE FROM IMGDATA WHERE ID == {0}'.format(id))
        print("done")
        self.connection_created.commit()

    def show(self):
        self.query = '''SELECT * FROM IMGDATA'''
        self.cursor.execute(self.query)
        self.con22 = self.cursor.fetchall()
        for i in self.con22:
            print(i)
obj = con()
obj.connection()
obj.create()