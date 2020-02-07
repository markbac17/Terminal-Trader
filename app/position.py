import sqlite3
import os


class Position:
    tablename = 'positions'
    dbpath = ''

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

            sql = """
                    INSERT INTO {} (account_id, ticker, num_shares)
                    VALUES (?,?,?);
                 """.format(self.tablename)

            curs.execute(sql, (self.account_id, self.ticker, self.num_shares))

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()

            sql = """
                    UPDATE {} SET num_shares=?
                    WHERE account_id=?;
                 """.format(self.tablename)

            values = (self.num_shares)
            curs.execute(sql, values)

    def delete(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """
                    DELETE FROM {} WHERE account_id =?;
                 """.format(self.tablename)

            curs.execute(sql, self.account_id)

    @classmethod
    def select_all(cls, where_clause, values):
        """select all entries from our database based on account_id
        """
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} {where_clause}"""
            curs.execute(sql, values)
            # return curs.fetchall()
            rows = curs.fetchall()
            if rows is None:
                return "No data"
            else:
                return [cls(**row) for row in rows]

    @classmethod
    def select_one_where(cls, where_clause, values):
        """
            selects an entry from our database based on its primary key
        """

        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} {where_clause};"""
            curs.execute(sql, (values))
            row = curs.fetchone()
            if row is None:
                return "empty"
            else:
                return cls(**row)

    def __repr__(self):
        return "Account: Account ID: {}, Ticker: {}, Shares: {}" \
            .format(self.account_id, self.ticker, self.num_shares)
