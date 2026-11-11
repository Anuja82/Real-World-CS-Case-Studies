Case 08 - Retry Mechanism with Exponential Backoff

Overview
This project demonstrates how a Python application automatically retries failed requests using an exponential backoff strategy.

Real- World Scenario

A banking application sends a request  to a server to retrieve account information. Due to temporary network issues, the server may be unavailable. Instead of failing immediately, the application retries the request after  increasing waiting intervals.

Concepts Covered
** Retry Mechanism
** Exponential Backoff
** Exception Handling
** Network Failures
** Backend Reliability
** Time Delays

Technologies Used
** Python
** Time Module

How It Works
1. Sends a request to the server.
2. Detects temporary connection failures.
3. Waits before retrying
4. Doubles the waiting time after each failed attempt.
5. Stops when the request succeeds or the maximum number of retries is reached.

Expected Result
The simulated server fails twice and succeeds on the third attemp. The application waits 1 seconds and then 2 seconds before retrying.

Learning Outcome
Learned how exponential backoff improves application reliability when handling temporary network failures.

