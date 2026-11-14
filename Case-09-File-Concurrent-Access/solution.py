import threading
import time

FILE_NAME="inventory.txt"

with open(FILE_NAME, "w") as file:
    file.write("Stock: 100\n")
file_lock=threading.Lock()
def update_inventory(user, quantity):
    print(f"{user} is waiting to update inventory...")
    with file_lock:
        print(f"{user} is updating inventory...")
        with open(FILE_NAME, "r") as file:
            stock=int(file.read().split(":")[1].strip())
        time.sleep(1)
        stock-=quantity
        with open(FILE_NAME, "w") as file:
            file.write(f"Stock: {stock}\n")
        print(f"{user} completed the update.")
user1=threading.Thread(target=update_inventory,args=("User 1",10))
user2=threading.Thread(target=update_inventory,args=("User 2",20))
user1.start()
user2.start()
user1.join()
user2.join()
with open(FILE_NAME,"r") as file:
    print("\nFinal Inventory:")
    print(file.read())