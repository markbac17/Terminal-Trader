import os
from app import Account, Position, Trade, run

DIR = os.path.dirname(__file__)
DBFILENAME = "ttrader.db"
DBPATH = os.path.join(DIR, 'data', DBFILENAME)

Account.dbpath = DBPATH
Position.dbpath = DBPATH
Trade.dbpath = DBPATH

run()