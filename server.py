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
    con.commit()                            #Saves changes to the .db file
    con.close()                             #Closes connection to database
    
