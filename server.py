import socket       #Networking
import threading    #Multiple Clients
import sqlite3      #User Database
import hashlib      #Hashing library

#Initialize a user database with SQLite3.
def init_db():
    con = sqlite3.connect('chat.db')        #Creates (opens if already created) a user database file. 
    cur = con.cursor()                      #Creates a cursor to run SQL commands.
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (  
            username TEXT PRIMARY KEY, 
            password TEXT NOT NULL
        )
    ''')                                    #Creates table, username column (no two usernames can be
    )                                       #the same), password column (cannot be empty).
    con.commit()                            #Saves changes to the .db file.
    con.close()                             #Closes connection to database.

#Hash password function
def hash_password(password)
    return hashlib.sha256(password.encode()).hexdigest()    #Hashes password

#Register user function implementation.
def register_user(username, password):
    con = sqlite3.connect('chat.db')        #Opens .db file.
    cur = con.cursor()                      #Creates a cursor to run SQL commands.
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, hash_password(password)))    #Insert new user to database.
        con.commit()                        #Save changes to database.
        print("User", username, "registerred successfully!")
    except sqlite3.IntegrityError:          #Executes if username exists.
        print("Username", username, "already exists!")
    con.close                               #Close the .db connection.

#Verify user function implementation.
def validate_user(username, password):
    con = sqlite3.connect('chat.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchone()
    con.close()
    if user is None:
        print ("Username", username, "does not exist!")
        return False
    if user[1] != hash_password(password):
        print("Wrong password")
        return False
    return True
    
