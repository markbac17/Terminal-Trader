import sqlite3

class Account:
    dbpath = "../data/trader.db"
    tablename = "accounts"

    def __init__(self, **kwargs):
        self.account_id = kwargs.get("account_id")
        self.username = kwargs.get("username")
        self.password_hash = kwargs.get("password_hash")
        self.balance = kwargs.get("balance")

    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """INSERT INTO {} (username, password_hash, balance)
                    VALUES (?,?,?);""".format(self.tablename)
            curs.execute(sql, (self.username, self.password_hash, self.balance))

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """UPDATE {} SET username=?, password_hash=?, balance=?
                WHERE account_id=?;""".format(self.tablename)
            values = (self.username, self.password_hash, self.balance, self.account_id)
            curs.execute(sql, values)

    def delete(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """DELETE FROM {} WHERE account_id =?;""".format(self.tablename)
            curs.execute(sql, self.account_id)

    @classmethod
    def select_all(cls, complete=None):
        """select all entries from our database based on whether they are
        complete or not, or selects all if complete=None
        """
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            if complete is None:
                sql = f"""SELECT * FROM {cls.tablename};"""
                curs.execute(sql)
            else:
                # sql = f"""SELECT * FROM {cls.tablename} WHERE complete=?;"""
                # curs.execute(sql, (complete,))
            # return curs.fetchall()
            rows = curs.fetchall()
            print(rows)
            return [cls(**row) for row in rows]

    @classmethod
    def select_one(cls, account_id):
        """selects an entry from our database based on its primary key"""
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} WHERE account_id=?;"""
            curs.execute(sql, (pk,))
            row =  curs.fetchone()
            return cls(**row)

    def __repr__(self):
        return f"Account: Account ID: {self.user_id}, User name: {self.username}, Password hash: {self.description}, Balance: {self.balance}"