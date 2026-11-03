import sqlite3
connection=sqlite3.connect(":memory:")
cursor=connection.cursor()

cursor.execute("""
CREATE TABLE users(username TEXT,
password TEXT )""")

cursor.execute("INSERT INTO users VALUES ('admin','admin123')")
username=input("Enter username:")
password=input("Enter password:")
query=("SELECT * FROM users WHERE username='" + username +"' AND password='"+password+"'")
print("SQL Query:", query)
cursor.execute(query)
result=cursor.fetchone()
if result:
    print("Login Successful!")
else:
    print("Invalid username or password.")
connection.close()
    
