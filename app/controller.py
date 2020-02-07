from app.position import Position
from app.account import Account
from app.trade import Trade
from app import view
from bcrypt import checkpw
from app.util import get_price
from datetime import datetime

def main_loop():
    while True:
        choice = view.user_menu()
        if choice is None:
            view.bad_input()
        
        elif choice == "3":
            view.goodbye()
            break

        elif choice == "1":
            login_input = view.login()
            verified_account = Account.login(login_input)
            if verified_account:
                db_password_hash = verified_account[2]
                password_verify = checkpw(login_input[1].encode(), db_password_hash)
                if password_verify:
                    account = Account(account_id = verified_account[0])
                    account.username = verified_account[1]
                    account.balance = int(verified_account[3])
                    
                    while True:
                        choice = view.main_menu()
                        
                        if choice is None:
                            view.bad_input()
                        
                        elif choice == '1':
                            view.display_balance(account.balance)

                        elif choice == '2':
                            account.balance += view.deposit()
                            print()
                            print(account)
                            print()
                            Account.update_balance(account)
                        
                        elif choice == '3':
                            buy_stock = view.trade_stock()
                            account.buy(buy_stock[0], buy_stock[1])
                        
                        elif choice == '4':
                            buy_stock = view.trade_stock()
                            position_exists = Position.select_one_where("WHERE account_id=? and ticker=?", (account.account_id,buy_stock[0]))
                            print(position_exists)
                            print(position_exists.num_shares)
                            if buy_stock[1] <= position_exists.num_shares:
                                account.sell(buy_stock[0], buy_stock[1])
                                mv = get_price(buy_stock[0]) * int(buy_stock[1])
                                account.balance += mv
                                account.update_balance()
                        
                        elif choice == '5':
                            positions = Account.get_positions(account)
                            print()
                            print(positions)
                            print()

                        elif choice == '6':
                            trade_history = Account.get_trades(account)
                            print()
                            print(trade_history)
                            print()
                        
                        elif choice == '7':
                            ticker = view.lookup_ticker()
                            print("Ticker: {} is currently: ${}".format(ticker, get_price(ticker)))
                        
                        elif choice == '8':
                            view.goodbye()
                        
                        else:
                            view.bad_input()

        elif choice == "2":
            account_details = view.create_account()
            account = Account(username = account_details[0], password_hash = account_details[1], balance = account_details[2])
            Account.save(account)

def run():
    main_loop()