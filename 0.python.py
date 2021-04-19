#!/usr/bin/env python
# coding: utf-8

# # Abstractions

# When a project gets big you need to start creating abstractions. It's important to not do it too early (that's a very common mistake), but as the project grows you will see some patterns appear very often.
# 
# Sometimes it's good to take those patterns and create an abstraction around them. The objective of that abstraction is hidding complexity.

# In[1]:


class Car:
    def __init__(self, wheels, power, color="red"):
        self.wheels = wheels
        self.power = power
        self.color = color
        self.position = (0, 0)

    def description(self, word):

        return f"""
The car is {self.color}
It has {self.wheels} wheels
Power: {self.power}

A random word for you:
{word}
""".strip()

    def move(self, distance):

        old_x = self.position[0]
        old_y = self.position[1]

        self.position = (old_x + distance, old_y + distance)

        print(f"I'm now at {self.posicion}")

        return True


# In[3]:


porsche = Car(wheels=5, power=150)


# In[6]:


print(porsche.description("hellos strivers"))


# ## TO DO:
# 
# We are going to do some operations with a database. Those operations will be quite standardized, so maybe we can abstract them away. Now it's your job to do it.

# Make things idempotent whenever possible.

# In[9]:


import datetime as dt


# In[12]:


import sqlite3

# CREATE TABLE IF NOT EXISTS users (..., ..., ...)  -- <-- complete this

DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS logs (time TEXT, key TEXT, value TEXT)
CREATE TABLE IF NOT EXISTS users (..., ..., ...)  -- <-- complete this
""".strip()


class DB:
    def __init__(self, dbname):
        self.dbname = dbname

        self.conn = sqlite3.connect(self.dbname)

        with self.conn as cursor:
            cursor.execute(DB_SCHEMA)

    def insert_log(self, key, value):
        now = dt.datetime.utcnow().isoformat()

        with self.conn as cursor:
            cursor.execute(
                "INSERT INTO logs VALUES (:time, :key, :value)",
                {"time": now, "key": key, "value": value},
            )

    def create_user(self, email, user_id, key):
        # TODO
        # insert a new user

        # return the new user created
        pass

    def validate_key(self, key):
        # TODO
        # check the user_id OR key OR both that is associated with the key

        # return the user_id / email
        pass


# In[13]:


db = DB(dbname="test.db")


# In[14]:


db.insert_log("hello", "world")

