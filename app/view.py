def user_menu():
    print("Welcome to Terminal Trader.")
    print()
    print('User logon')
    print()
    print('1. Login')
    print('2. Create account')
    print('3. Exit')
    print()
    choice = input("Select option: ")
    return choice

def main_menu():
    print()
    print('1. View balance')
    print('2. Deposit')
    print('3. Buy')
    print('4. Sell')
    print('5. View positions')
    print('6. View trades')
    print('7. Lookup')
    print('8. Logout')
    print()
    choice = input('Enter choice: ')
    return choice

def trade_stock():
    print()
    ticker = input("enter stock ticker: ")
    quantity = input("Enter quantity: ")
    return ticker, int(quantity)

def display_balance(balance):
    print()
    print("Account balance is: ${}".format(balance))
    print()

def create_account():
    print()
    print('Create new account')
    print()
    username = input('Create user name: ')
    password = input('Create password: ')
    balance = input('Enter amount to deposit: ')
    return username, password, balance

def login():
    print()
    print('Logon screen')
    print()
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def deposit():
    print()
    print('Deposit funds')
    print()
    balance = input('Enter amount to deposit: ')
    return int(balance)

def lookup_ticker():
    print()
    print('Lookup ticker')
    print()
    ticker = input('Lookup ticker: ')
    return ticker


def goodbye():
    print()
    print("Thank you for usinng Terminal Trader")
    exit()


def bad_input():
    print()
    print("Bad input. Retry!")

def enter_to_continue():
    print('Press enter to continue. ')

def select_item():
    choice = ''
    return choice