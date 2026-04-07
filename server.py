import socket       #Networking
import threading    #Multiple Clients
import sqlite3      #User Database
import hashlib      #Hashing library


def init_database():
    con = sqlite3.connect('chat.db')                                   
    cur = con.cursor()                                                
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT NOT NULL)")                                                                                                                                  
    con.commit()                                                      
    con.close()                                                         


#Tracks connected clients as {username: client_socket}
clients = {} 


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()                


def register_user(username, password):
    con = sqlite3.connect('chat.db')                                   
    cur = con.cursor()                                                 
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, hash_password(password)))    
        con.commit()                                                    
        print("User", username, "registered successfully!")   
    except sqlite3.IntegrityError:    #PRIMARY KEY violation: username is taken.                                   
        print("Username", username, "already exists!")
    con.close()                                                           
    

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

  
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
    server.bind(('localhost', 9999))                                 
    server.listen(3)                                                  
    print("Server running on Port: 9999")
    while True:
        client_socket, address = server.accept()                     
        print("Connection from", address)
        #Each client gets own thread so they don't block each other
        thread = threading.Thread(target = handle_client, args = (client_socket,)) 
        thread.start()
