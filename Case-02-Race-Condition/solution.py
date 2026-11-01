import threading
import time

balance=1000

def withdraw(person, amount):
    global balance
    print(f"{person} checking balance...")
    if balance>=amount:
        current_balance=balance
        time.sleep(1)
        balance=current_balance-amount
        print(f"{person} withdrew Rs.{amount}")
    else:
        print(f"{person}:Insufficient balance")
t1=threading.Thread(target=withdraw, args=("Person A",700))
t2=threading.Thread(target=withdraw,args=("Person B", 700))
t1.start()
t2.start()
t1.join()
t2.join()
print("Final balance:", balance)