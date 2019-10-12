#Daniel Kolodziej
#ITMD 413 Lab 8
#4/18/2018

import sqlite3
from contacts import *

#creates the table in the db file
def createTable():
    #creates and connects to db file named contacts
    conn = sqlite3.connect('contacts.db')
    print ("Opened database successfully")

    #cursor allows to execute sql commands
    c = conn.cursor()
    #creates table daniel
    c.execute("""CREATE TABLE IF NOT EXISTS daniel (
                id INTEGER PRIMARY KEY,
                name TEXT not null,
                phone INTEGER not null
                )""")
    print("Table created successfully")

    #check whether to insert records into db from contact list
    c.execute("SELECT * FROM daniel")
    entry = c.fetchone()

    if entry is None:
        print("No records found")
        for name, phone in contactlist:
              insertContact(name, phone)
        print("Records inserted...")
    else:
        print("Entry not found...")

#inserts new contacts (name and phone) into the db              
def insertContact(name, phone):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    sql =("""INSERT INTO daniel
            (name, phone)
            VALUES(?,?)""")

    data = (name, phone)
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
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM daniel")
    return c.fetchall()
    conn.close()

#uses id of record to delete chosen contact
def deleteContact(id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    data = str(id)
    sql = "DELETE FROM daniel WHERE ID = ?;"
    #use of tuples so must add in the comma -> ( ,)
    c.execute(sql , (data,))
    conn.commit()
    conn.close()
    print("deleted contact from DB")

#uses id of record to update the contact name and or phone
def updateContact(id, name, phone):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("""UPDATE daniel SET name = ? ,phone = ? WHERE id= ? """,
    (name,phone,id))
    conn.commit()
    conn.close()
    print("updated contact from DB")
