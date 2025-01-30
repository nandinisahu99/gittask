# -*- coding: utf-8 -*-
"""crud.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13DkMH1ikpD2P0lm-kp_uVsIedwDmk0WY
"""

import sqlite3

conn=sqlite3.connect("mydb.db")
c = conn.cursor()

def create_table():
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)

def insert(name, age):
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Inserted Successfully")

def read():
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    for user in users:
      print(user)
    return users 

def update(name, age, id):
    c.execute("UPDATE users SET name=?, age=? WHERE id=?", (name, age, id))
    conn.commit()
    print("Updated Successfully")

def delete(id):
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    print("Deleted Successfully")

if __name__ == "__main__":
  create_table()
  insert("Nandini",24)
  insert("Shivani",23)
  insert("Aman",26)
  read()
  update("Shivani",22,2)
  delete(2)
  read()
  conn.close()

