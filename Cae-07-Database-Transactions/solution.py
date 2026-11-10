import sqlite3
connection=sqlite3.connect("bank.db")
cursor=connection.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS accounts(account_id INTEGER PRIMARY KEY, name TEXT, balance REAL)""")
cursor.execute(""" INSERT OR IGNORE INTO accounts VALUES(1,'Account A',10000)""")
cursor.execute("""INSERT OR IGNORE INTO accounts VALUES(2,'Account B',3000)""")
connection.commit()
def show_balances():
    cursor.execute("SELECT * FROM accounts")
    for account in cursor.fetchall():
        print(account)
def transfer_money(amount):
    try:
        print("\nStrating transaction...")
        connection.execute("BEGIN")
        cursor.execute("""UPDATE accounts SET balance=balance-? WHERE account_id=1""", (amount,))
        # raise Exception("Simulated application error!")
        cursor.execute("""UPDATE accounts SET balance=balance+?WHERE account_id=2""",(amount,))
        connection.commit()
        print("Transfer successful!")
    except Exception as error:
        connection.rollback()
        print("Transaction failed:",error)
        print("Rollback completed!")
print("Before Transfer:")
show_balances()
transfer_money(5000)
print("\nAfter Transfer:")
show_balances()
connection.close()
