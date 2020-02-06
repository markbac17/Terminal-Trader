import sqlite3
import os

class Trade:
    tablename = "trades"
    dbpath = '../data/trader.db'

    def __init__(self, **kwargs):
        self.trade_id = kwargs.get("trade_id")
        self.account_id = kwargs.get("account_id")
        self.volume = kwargs.get("volume")
        self.price = kwargs.get("price")
        self.time = kwargs.get("time")
        self.market_value = kwargs.get("market_value")

    def save(self):
        if self.trade_id is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        print(self.dbpath)
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """INSERT INTO {} (account_id, volume, price, time, market_value)
                    VALUES (?,?,?,?,?);""".format(self.tablename)
            curs.execute(sql, (self.account_id, self.volume, self.price, self.time,self.market_value))

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """UPDATE {} SET account_id=?, volume=?, price=?, time=?, market_value=?
                WHERE account_id=?;""".format(self.tablename)
            values = (self.account_id, self.volume, self.price, self.time, self.market_value)
            curs.execute(sql, values)

    def delete(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """DELETE FROM {} WHERE account_id =?;""".format(self.tablename)
            curs.execute(sql, self.account_id)

    @classmethod
    def select_all(cls, *args):
        """select all entries from our database based on whether they are
        complete or not, or selects all if complete=None
        """
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} {args[0]};"""
                # sql = f"""SELECT * FROM {cls.tablename} WHERE complete=?;"""
            curs.execute(sql, args[1])
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
            curs.execute(sql, (account_id,))
            row =  curs.fetchone()
            return cls(**row)

    def __repr__(self):
        return f"Account: Account ID: {self.account_id}, Volume: {self.volume}, \
        Price: {self.price}, Time: {self.time}, Market value: {self.market_value}"


# trade = Trade(account_id = 1, volume = 100, price = 320, time = 1, market_value =1)
# Trade.save(trade)