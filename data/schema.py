import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'trader.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        sql = """CREATE TABLE accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR,
            password_hash VARCHAR,
            balance FLOAT
        );"""
        cur.execute(sql)

        sql = """CREATE TABLE positions (
            position_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INT,
            ticker VARCHAR,
            num_shares INT,
            FOREIGN KEY (account_id) REFERENCES accounts(account_id)
        );"""
        cur.execute(sql)

        sql = """CREATE TABLE trades (
            trade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id VARCHAR,
            volume INT,
            price FLOAT,
            FOREIGN KEY (account_id) REFERENCES accounts(account_id)
        );"""
        cur.execute(sql)

if __name__ == "__main__":
    schema()