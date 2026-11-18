CASE 10 - Idempotency in Payment Systems

Overview
This project demonstrates how an online payment system prevents duplicate transactions using idempotency keys in Python.

Real-World Scenario

A customer clicks the Pay Now button, and the payment is successfully processed. However, due to a network issue, the application sends
the same payment request again. Without duplicate request handling, the customer could be charged twice.

Concepts Covered
**Idempotency
**Duplicate Request Detection
**Payment Processing
**Transaction Management
**UUID Generation
**Python Dictionaries
**Backend REliability

Technologies Used
** Python
** UUID Module

How it Works
1. Receives a payment request with an idempotency key.
2. Checks whether the key has already been processed
3. Processes the payment if the key is new.
4. Stores the transaction result using the idempotency key.
5. Returns the previous result if the same request is received again.
6. Displays the final account balance.

Excepted Result
The first payment request is processed successfully. When the same request is received again with the same
idempotency key, the previous transaction result is returned without deducting the amount again.

Learning Outcome
Learned how idempotency keys help prevent duplicate payments and improve the reliability of backend payment systems.