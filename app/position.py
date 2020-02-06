import sqlite3
import os

class Position:
    tablename = 'positions'
    dbpath = '../data/trades.db'

    def __init__(self, **kwargs):
        self.positions_id = kwargs.get("position_id")
        self.account_id = kwargs.get("account_id")
        self.ticker = kwargs.get("ticker")
        self.num_shares = kwargs.get("num_shares")


    def save(self):
        if self.positions_id is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """INSERT INTO {} (account_id, ticker, num_shares)
                    VALUES (?,?,?);""".format(self.tablename)
            curs.execute(sql, (self.account_id, self.ticker, self.num_shares))

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """UPDATE {} SET username=?, password_hash=?, balance=?
                WHERE account_id=?;""".format(self.tablename)
            values = (self.account_id, self.ticker, self.num_shares)
            curs.execute(sql, values)

    def delete(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """DELETE FROM {} WHERE account_id =?;""".format(self.tablename)
            curs.execute(sql, self.account_id)

    @classmethod
    def select_all(cls, *args):
        """select all entries from our database based on account_id
        """
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} {args[0]};"""
            curs.execute(sql, args[1])
            # return curs.fetchall()
            rows = curs.fetchall()
            print(rows)
            # return [(**row) for row in rows]

    @classmethod
    def select_one(cls, account_id, ticker):
        """selects an entry from our database based on its primary key"""
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} WHERE account_id=?;"""
            curs.execute(sql, (account_id,))
            row =  curs.fetchone()
            return cls(**row)

    def __repr__(self):
        return f"Account: Account ID: {self.account_id}, Ticker: {self.ticker}, Lots: {self.num_shares}"
