#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('database.db')
print ("Database has opened successfully")

conn.execute("DROP TABLE IF EXISTS OBJAWY")
conn.execute("DROP TABLE IF EXISTS LEKI")
conn.execute("DROP TABLE IF EXISTS CHOROBY")
conn.execute("DROP TABLE IF EXISTS WNIOSKI")
conn.execute("DROP TABLE IF EXISTS WNIOSKI_LEKI_RELACJA")
conn.execute("DROP TABLE IF EXISTS CHOROBY_LEKI_RELACJA")
conn.execute("DROP TABLE IF EXISTS CHOROBY_OBJAWY_RELACJA")

conn.execute('''CREATE TABLE OBJAWY
	(ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NAZWA_OBJAWU	TEXT	NOT NULL);''')

print ("Table Objawy created successfully")

conn.execute('''CREATE TABLE LEKI
	(ID INTEGER PRIMARY KEY	AUTOINCREMENT,
	NAZWA_LEKU	TEXT	NOT NULL);''')

print ("Table Leki created successfully")

conn.execute('''CREATE TABLE CHOROBY
	(ID INTEGER PRIMARY KEY	AUTOINCREMENT,
	NAZWA_CHOROBY	TEXT	NOT NULL);''')

print ("Table Choroby created successfully")

conn.execute('''CREATE TABLE WNIOSKI
	(ID INTEGER PRIMARY KEY	AUTOINCREMENT,
	ID_CHOROBY	INT	NOT NULL);''')

print ("Table Wnioski created successfully")

conn.execute('''CREATE TABLE WNIOSKI_LEKI_RELACJA
	(ID INT PRIMARY KEY	NOT NULL,
	SKUTEK INT,
	ID_WNIOSKU INT,
	ID_LEKU INT,
	FOREIGN KEY(ID_WNIOSKU) REFERENCES WNIOSKI(ID),
	FOREIGN KEY(ID_LEKU) REFERENCES LEKI(ID));''')

print ("Table leki_wnioski_relacja created successfully")

conn.execute('''CREATE TABLE CHOROBY_LEKI_RELACJA
	(ID_CHOROBY INT,
	ID_LEKU INT,
	FOREIGN KEY(ID_CHOROBY) REFERENCES CHOROBY(ID),
	FOREIGN KEY(ID_LEKU) REFERENCES LEKI(ID));''')

print ("Table Choroby_leki_relacja created successfully")

conn.execute('''CREATE TABLE CHOROBY_OBJAWY_RELACJA
	(ID_CHOROBY INT,
	ID_OBJAWU INT,
	FOREIGN KEY(ID_CHOROBY) REFERENCES CHOROBY(ID),
	FOREIGN KEY(ID_OBJAWU) REFERENCES OBJAWY(ID));''')

print ("Table choroby_objawy_relacja created successfully")
