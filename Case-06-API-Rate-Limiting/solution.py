import time
from collections import deque

MAX_REQUESTS=5
TIME_WINDOW=10

requests=deque()

def allow_request(user):
    current_time=time.time()
    while requests and current_time-requests[0]>=TIME_WINDOW:
        requests.popleft()
    if len(requests)<MAX_REQUESTS:
        requests.append(current_time)
        print(f"{user}:Request allowed")
    else:
        print(f"{user}: Too many requests! Try again later.")
for i in range(7):
    allow_request("User 1")
