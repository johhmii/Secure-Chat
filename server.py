import socket       #Networking
import threading    #Multiple Clients
import sqlite3      #User Database

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

#Register user function implementation.
def register_user(username, password):
    con = sqlite3.connect('chat.db')        #Opens .db file.
    cur = con.cursor()                      #Creates a cursor to run SQL commands.
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))    #Insert new user to database.
        con.commit()                        #Save changes to database.
        print("User", username, "registerred successfully!")
    except sqlite3.IntegrityError:          #Executes if username exists.
        print("Username", username, "already exists!")
    con.close                               #Close the .db connection.
