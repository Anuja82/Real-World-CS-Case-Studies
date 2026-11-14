Case 09 - File Handling and Concurrent Access

Overview
This project demonstrates how multiple threads can access and update a shared file safely
using Python file handling and thread synchronization.

Real-World Scenario
An online shopping application has an inventory file that stores product stock.
When two users try to update the inventory simultaneously, incorrect stock values may occur without proper synchronization.

Concepts Covered
** File Handling
** Multithreading
** Concurrent File Access
** Thread Synchronization
** File Locking
** Shared Resources
** Data Consistency

Technologies Used

** Python
** Threading Module
** Time Module

How it Works

1. Creates an inventory file with an initial stock of 100
2. Creates two threads representing two users.
3. Both users attempt to update the inventory.
4. Uses a thread lock to allow only one user to update the file at a time.
5. Reads the current stock and deducts the requested quantity.
6. Displays the final inventory.

Expected Result
Both users successfully update the inventory one after another. The final stock is 70 after deducting 10 and 20 units from the initial stock of 100.

Learning Outcome

Learned how thread synchronization and file locking prevent concurrent access problems and help maintain consistent inventory data.