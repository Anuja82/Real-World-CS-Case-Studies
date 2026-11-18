import uuid
balance=10000
processed_payments={}

def process_payment(idempotency_key,amount):
    global balance
    if idempotency_key in processed_payments:
        print("Duplicate request detected!")
        print("Returning previous transaction result.")
        return processed_payments[idempotency_key]
    if amount>balance:
        result={
            "status":"Failed",
            "message":"Insufficient balance"}
        processed_payments[idempotency_key]=result
        return result
    balance-=amount
    transaction={
        "transaction_id":str(uuid.uuid4()),
        "status":"Success",
        "amount":amount
    }
    processed_payments[idempotency_key]=transaction
    print("Payment processed successfully!")
    return transaction
print("First Request:")
result1=process_payment("PAY-001",2000)
print(result1)
print("\nSecond Request:")
result2=process_payment("PAY-001",2000)
print(result2)
print("\nFinal Account Balance:",balance)