import threading
import queue
import time

order_queue=queue.Queue(maxsize=3)

def producer():
    for order in range(1,6):
        print(f"New order received:{order}")
        order_queue.put(order)
        print(f"Order {order} added to queue")
        time.sleep(0.5)
    order_queue.put(None)
def consumer():
    while True:
        order=order_queue.get()
        if order is None:
            print("No more orders to process.")
            break
        print(f"Processing order:{order}")
        time.sleep(1)
        print(f"Order {order} completed")
producer_thread=threading.Thread(target=producer)
consumer_thread=threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()
print("All orders processed!")