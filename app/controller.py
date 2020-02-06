from app.position import Position
from app.account import Account
from app.trade import Trade
from app import view
from bcrypt import checkpw
from app.util import get_price

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
                print(type(verified_account[0]))
                if password_verify:
                    while True:
                        account = Account(account_id = verified_account[0])
                        choice = view.main_menu()
                        if choice is None:
                            view.bad_input()
                        elif choice == '1':
                            print(account)
                            balance = Account.get_balance(str(account.account_id))
                            print(balance[1])
                        elif choice == '2':
                            pass
                        elif choice == '3':
                            trade = Trade(account_id = 1, volume = 100, price = 320, time = 1, market_value =1)
                            Trade.save(trade)
                        elif choice == '4':
                            pass
                        elif choice == '5':
                            pass
                        elif choice == '6':
                            pass
                        elif choice == '7':
                            ticker = view.lookup_ticker()
                            print(get_price(ticker))
                        elif choice == '8':
                            pass
                        else:
                            pass
        elif choice == "2":
            account_details = view.create_account()
            print(account_details)
            account = Account(username = account_details[0], password_hash = account_details[1], balance = account_details[2])
            Account.save(account)

def run():
    main_loop()