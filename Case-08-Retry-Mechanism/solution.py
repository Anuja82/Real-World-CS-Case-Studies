import time
MAX_RETRIES=3
INITIAL_DELAY=1

def send_request():
    send_request.attempts+=1
    if send_request.attempts<3:
        raise ConnectionError("Server is temporarily unavailable")
    return "Request successful!"
send_request.attempts=0
def retry_request():
    delay=INITIAL_DELAY
    for attempt in range(1,MAX_RETRIES+1):
        try:
            print(f"Attempt {attempt}:Sending request...")
            result=send_request()
            print(result)
            return
        except ConnectionError as error:
            print(error)
            if attempt<MAX_RETRIES:
                print(f"Retrying after {delay} seconds...\n")
                time.sleep(delay)
                delay*=2
    print("Request failed after maximum retries.")
retry_request()