import sqlite3
from contacts import *

#creates the table in the db file
def createTable():
    #creates and connects to db file named contacts
    conn = sqlite3.connect('players.db')
    print ("Opened database successfully")

    #cursor allows to execute sql commands
    c = conn.cursor()
    #creates table users
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT not null,
                score INTEGER not null
                )""")
    print("Table created successfully")

    #check whether to insert records into db from contact list
    c.execute("SELECT * FROM users")
    entry = c.fetchone()

    if entry is None:
        print("No records found")
        for name, score in contactlist:
              insertContact(name, score)
        print("Records inserted...")
    else:
        print("Entry not found...")

#inserts new contacts (name and phone) into the db              
def insertContact(name, score):
    conn = sqlite3.connect('players.db')
    c = conn.cursor()
    sql =("""INSERT INTO users
            (name, score)
            VALUES(?,?)""")

    data = (name, score)
    # Try block to throw exception if fields are blank
    try:
        c.execute(sql, data)
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        print("Bad data")

#reads and retrieves all contacts/records from db
def readContacts():
    conn = sqlite3.connect('players.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    return c.fetchall()
    conn.close()
