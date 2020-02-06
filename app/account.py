import sqlite3
from .util import get_price, hash_password, checkpw
from .position import Position
from .trade import Trade

class Account:

    tablename = "accounts"
    dbpath = ""

    def __init__(self, **kwargs):
        self.account_id = kwargs.get('account_id')
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.balance = kwargs.get('balance')

    def save(self):
        if self.account_id is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """INSERT INTO {} (username, password_hash, balance)
                    VALUES (?,?,?);""".format(self.tablename)
            curs.execute(sql, (self.username, hash_password(self.password_hash), self.balance))

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """UPDATE {} SET username=?, password_hash=?, balance=?
                WHERE account_id=?;""".format(self.tablename)
            values = (self.username, self.password_hash, self.balance)
            curs.execute(sql, values)

    @classmethod
    def login(cls, login_details):
        return cls.select_one_where("WHERE username=?", (login_details[0],))
        # return cls.select_one_where("WHERE username=? AND password_hash=?", (login_details[1],))

    def buy(self, ticker, quantity):
        """ make a purchase. checks if ticker exists and if sufficient funds
        exist for this user. create a new Trade and modify a Position as well
        as the user's balance. returns nothing
        """
        # check price of the ticker * quantity
        # check balance is >= than that price
        # create new Trade(**kwargs) and save to database
        # create OR update a position
        # modify our balance
        # save our User instance
        pass

    def sell(self, ticker, quantity):
        """ make a sale. checks if a stock exists in the user's positions and
        has sufficient shares. creates a new Trade and modifies the Position as
        well as adding to the user's balance. returns nothing
        """
        pass

    def get_balance(self):
        """returns a list of Position objects"""
        return Account.select_one_where("WHERE account_id=?", (self.account_id,))

    def get_positions(self):
        """returns a list of Position objects"""
        return Position.select_all("WHERE account_id=?", (self.account_id,))
        # return Position.select_all('',)

    def get_trades(self):
        """returns a list of Trade objects"""
        return Trade.select_all("WHERE account_id=?", (self.account_id,))

    def get_position_for(self, ticker):
        return Position.select_one("WHERE account_pk=? AND ticker=?", (self.account_id, ticker))

    @classmethod
    def select_one_where(cls, where_clause, values):
        """ selects an entry from our database based on its primary"""
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} {where_clause};"""
            print(sql,values)
            curs.execute(sql, (values))
            row = curs.fetchone()
            return row

    def __repr__(self):
        return f"Account ID: {self.account_id}, User name: {self.username},\
         Password hash: {self.password_hash}, Balance: {self.balance}"