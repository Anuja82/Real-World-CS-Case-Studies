Case 02 -Race Condition

Domain:Operating systems

Problem: Demostrates what happens when two threads access and modify a shared bank account balance simultaneously.

Real-World Scenario: Two people attempt to withdraw money from the same bank account at the same time.

Concepts Covered:

** Multithreading
** Shared Resources
** Race Conditions
** Thread Synchronization
** Data Consistency

Implementation: Python (threading, time)

Expected Result: Both threads may read the same initial balance and overwrite each other's updates, producing an incorrect final balance.

Learning Outcome: Understand why synchronization is important when multiple threads access shared data.
