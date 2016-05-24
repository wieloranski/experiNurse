#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('db/database.db')
print ("Database has opened successfully")

#C-Create, R-Read, U-Update, D-Delete

#CREATE

def create_choroby(choroba):
    conn.execute('INSERT INTO CHOROBY (NAZWA_CHOROBY) VALUES (?)', [choroba]);
    conn.commit()

def create_leki(lek):
    conn.execute('INSERT INTO LEKI(NAZWA_LEKU) VALUES (?)', [lek]);
    conn.commit()

def create_objawy(objaw):
    conn.execute('INSERT INTO OBJAWY(NAZWA_OBJAWU) VALUES(?)', [objaw]);
    conn.commit()

def create_wnioski(choroba):
    conn.execute('INSERT INTO WNIOSKI(ID_CHOROBY) VALUES(?)', [choroba]);
    conn.commit()

def create_choroby_leki(id_choroby, id_leku):
    conn.execute('INSERT INTO CHOROBY_LEKI_RELACJA(ID_CHOROBY, ID_LEKU) VALUES(?,?)', [id_choroby, id_leku]);
    conn.commit()

def create_choroby_objawy(id_choroby, id_objawu):
    conn.execute('INSERT INTO CHOROBY_OBJAWY_RELACJA(ID_CHOROBY, ID_OBJAWU) VALUES(?,?)', [id_choroby, id_leku]);
    conn.commit()

def create_wnioski_leki(skutek, id_wniosku, id_leku):
    conn.execute('INSERT INTO WNIOSKI_LEKI_RELACJA(SKUTEK, ID_WNIOSKU, ID_LEKU) VALUES(?,?,?)', [skutek, id_wniosku, id_leku]);
    conn.commit()

#READ

def read_choroby_id(id):
    cursor = conn.execute('SELECT NAZWA_CHOROBY FROM CHOROBY WHERE ID=?', [id])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]

def read_choroby_nazwa(nazwa):
    cursor = conn.execute('SELECT ID FROM CHOROBY WHERE NAZWA_CHOROBY=?', [nazwa])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]

def read_choroby_leki_id_leku(id_leku):
    cursor = conn.execute('SELECT ID_CHOROBY FROM CHOROBY_LEKI_RELACJA WHERE ID_LEKU=?', [id_leku])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]

def read_choroby_leki_id_choroby(id_choroby):
    cursor = conn.execute('SELECT ID_LEKU FROM CHOROBY_LEKI_RELACJA WHERE ID_CHOROBY=?', [id_choroby])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]

def read_choroby_objawy_id_choroby(id_choroby):
    cursor = conn.execute('SELECT ID_OBJAWU FROM CHOROBY_OBJAWY_RELACJA WHERE ID_CHOROBY=?', [id_choroby])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]

def read_choroby_objawy_id_objawu(id_objawu):
    cursor = conn.execute('SELECT ID_CHOROBY FROM CHOROBY_OBJAWY_RELACJA WHERE ID_OBJAWU=?', [id_objawu])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]


def read_leki_id(id):
    cursor = conn.execute('SELECT NAZWA_LEKU FROM LEKI WHERE ID=?', [id])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]


def read_leki_nazwa_leku(nazwa_leku):
    cursor = conn.execute('SELECT ID FROM LEKI WHERE NAZWA_LEKU=?', [nazwa_leku])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]


def read_objawy_id(id):
    cursor = conn.execute('SELECT NAZWA_OBJAWU FROM OBJAWY WHERE ID=?', [id])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]


def read_objawy_nazwa_objawu(nazwa_objawu):
    cursor = conn.execute('SELECT ID FROM OBJAWY WHERE NAZWA_OBJAWU=?', [nazwa_objawu])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]

def read_wnioski_id(id):
    cursor = conn.execute('SELECT ID_CHOROBY FROM WNIOSKI WHERE ID=?', [id])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]

def read_wnioski_id_choroby(id_choroby):
    cursor = conn.execute('SELECT ID FROM WNIOSKI WHERE ID=?', [id_choroby])
    cur=[]
    for row in cursor:
        cur.append(row)
    return cur[0]

def read_choroby_objawy_objaw(objaw):
    cur1 = conn.execute('SELECT ID FROM OBJAWY WHERE NAZWA_OBJAWU=?', [objaw])
    cur11=[]
    for row in cur1:
        cur11.append(row)
    cur2 = conn.execute('SELECT ID_CHOROBY FROM CHOROBY_OBJAWY_RELACJA WHERE ID_OBJAWU=?', [cur11[0][0]])
    cur22=[]
    for row in cur2:
        cur22.append(row)
    cur33=[]
    index=0
    cur333=[]    
    for row in cur22:
        cur3 = conn.execute('SELECT NAZWA_CHOROBY FROM CHOROBY WHERE ID=?', [cur22[index][0]])
        for row1 in cur3:
            cur333.append(row1)           
        index = index+1
    ret = []
    index1=0
    for row in cur333:
        #ret.append(cur333[index1])
        #print(len(cur333))
        #index1=index1+1
        ret.append(row[index1])
    return ret


#UPDATE

def update_choroby_id(id, nazwa_choroby):
    conn.execute('UPDATE CHOROBY set NAZWA_CHOROBY = ? WHERE ID=?', [id])
    conn.commit()

def update_choroby_nazwa(nazwa_choroby, new_nazwa):
    conn.execute('UPDATE CHOROBY set NAZWA_CHOROBY=? WHERE NAZWA_CHOROBY=?', [new_nazwa, nazwa_choroby])
    conn.commit()

def update_choroby_leki_id_choroby_choroby(id_choroby, new_choroba):
    conn.execute('UPDATE CHOROBY_LEKI_RELACJA set ID_CHOROBY=? WHERE ID_CHOROBY=?', [new_choroba, id_choroby])
    conn.commit()

def update_choroby_leki_id_leku_choroby(id_leku, new_choroba):
    conn.execute('UPDATE CHOROBY_LEKI_RELACJA set ID_CHOROBY=? WHERE ID_LEKU=?', [new_choroba, id_leku])
    conn.commit()

def update_choroby_leki_id_choroby_leki(id_choroby, new_leki):
    conn.execute('UPDATE CHOROBY_LEKI_RELACJA set ID_LEKU=? WHERE ID_CHOROBY=?', [new_leki, id_choroby])
    conn.commit()

def update_choroby_leki_id_leku_leki(id_leku, new_leki):
    conn.execute('UPDATE CHOROBY_LEKI_RELACJA set ID_LEKU=? WHERE ID_LEKU=?', [new_leki, id_leku])
    conn.commit()


def update_choroby_objawy_id_choroby_choroby(id_choroby, new_choroba):
    conn.execute('UPDATE CHOROBY_OBJAWY_RELACJA set ID_CHOROBY=? WHERE ID_CHOROBY=?', [new_choroba, id_choroby])
    conn.commit()

def update_choroby_objawy_id_objawu_choroby(id_objawu, new_choroba):
    conn.execute('UPDATE CHOROBY_OBJAWY_RELACJA set ID_CHOROBY=? WHERE ID_OBJAWU=?', [new_choroba, id_objawu])
    conn.commit()

def update_choroby_objawy_id_choroby_objawy(id_choroby, new_objawy):
    conn.execute('UPDATE CHOROBY_OBJAWY_RELACJA set ID_LEKU=? WHERE ID_CHOROBY=?', [new_objawy, id_choroby])
    conn.commit()

def update_choroby_objawy_id_objawu_objawy(id_objawu, new_objawy):
    conn.execute('UPDATE CHOROBY_OBJAWY_RELACJA set ID_LEKU=? WHERE ID_OBJAWU=?', [new_objawy, id_objawu])
    conn.commit()

def  update_leki_id(id, nazwa_leku):
    conn.execute('UPDATE LEKI set NAZWA_LEKU=? WHERE ID=?', [nazwa_leku, id])
    conn.commit()

def update_leki_nazwa(nazwa_leku, new_nazwa):
    conn.execute('UPDATE LEKI set NAZWA_LEKU=? WHERE NAZWA_LEKU=?', [new_nazwa, nazwa_leku])
    conn.commit()

def update_objawy_id(id, nazwa_objawu):
    conn.execute('UPDATE OBJAWY set NAZWA_OBJAWU=? WHERE ID=?', [nazwa_objawu, id])
    conn.commit()

def update_objawy_nazwa(nazwa_objawu, new_nazwa):
    conn.execute('UPDATE OBJAWY set NAZWA_OBJAWU=? WHERE NAZWA_OBJAWU=?', [new_nazwa, nazwa_objawu])
    conn.commit()

def update_objawy_id(id, nazwa_objawu):
    conn.execute('UPDATE OBJAWY set NAZWA_OBJAWU=? WHERE ID=?', [nazwa_objawu, id])
    conn.commit()

def update_wnioski_id(id, id_choroby):
    conn.execute('UPDATE WNIOSKI SET ID_CHOROBY=? WHERE ID=?', [id_choroby, id])
    conn.commit()


#def update_wnioski_leki


#DELETE

def delete_choroby_id(id):
    conn.execute('DELETE FROM CHOROBY WHERE ID=?', [id])
    conn.commit()

def delete_choroby_nazwa(nazwa_choroby):
    conn.execute('DELETE FROM CHOROBY WHERE NAZWA_CHOROBY=?', [nazwa_choroby])
    conn.commit()

def delete_choroby_leki(id_choroby, id_leku):
    conn.execute('DELETE FROM CHOROBY_LEKI_RELACJA WHERE ID_CHOROBY=? AND ID_LEKU=?', [id_choroby, id_leku])
    conn.commit()

def delete_choroby_objawy(id_choroby, id_objawu):
    conn.execute('DELETE FROM CHOROBY_OBJAWY_RELACJA WHERE ID_CHOROBY=? AND ID_OBJAWU=?', [id_choroby, id_objawu])
    conn.commit()

def delete_leki_id(id):
    conn.execute('DELETE FROM LEKI WHERE ID=?', [id])
    conn.commit()

def delete_leki_nazwa(nazwa_leku):
    conn.execute('DELETE FROM LEKI WHERE NAZWA_LEKU=?', [nazwa_leku])
    conn.commit()

def delete_objawy_id(id):
    conn.execute('DELETE FROM OBJAWY WHERE ID=?', [id])
    conn.commit()

def delete_objawy_nazwa(nazwa_objawu):
    conn.execute('DELETE FROM OBJAWY WHERE NAZWA_OBJAWU=?', [nazwa_objawu])
    conn.commit()

def delete_wnioski_id(id):
    conn.execute('DELETE FROM WNIOSKI WHERE ID=?', [id])
    conn.commit()

def delete_wnioski_leki_id(id):
    conn.execute('DELETE FROM WNIOSKI_LEKI_RELACJA WHERE ID=?', [id])
    conn.commit()


#conn.close()
