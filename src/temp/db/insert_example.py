#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('database.db')
print ("Database has opened successfully")


conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (1, 'Zamknięte złamanie ręki')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (2, 'Otwarte złamanie ręki')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (3, 'Nadciśnienie tętnicze')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (4, 'Cukrzyca typu 1')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (5, 'Cukrzyca typu 2')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (6, 'Zapalenie płuc')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (7, 'Wirusowe zapalenie płuc')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (8, 'Bakteryjne zapalenie płuc')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (9, 'Grypa')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (10, 'Alergia')");

conn.execute("INSERT INTO CHOROBY (ID,NAZWA_CHOROBY) \
      VALUES (11, 'Alergia pokarmowa')");


conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (1, 'Ból ręki')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (2, 'Opuchlizna ręki')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (3, 'Wygrubienie na ręce')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (4, 'Wystająca kość')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (5, 'Zwiększona pobudliwość nerwowa')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (6, 'Zaburzenia snu')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (7, 'Kołatanie serca')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (8, 'Zawroty głowy')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (9, 'Podwyższone ciśnienie krwi')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (10, 'Wzmożone pragnienie')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (11, 'Częste oddawanie moczu')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (12, 'Wzmożony apetyt')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (13, 'Osłabienie')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (14, 'Senność')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (15, 'Podwójne widzenie')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (16, 'Utrata wagi')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (17, 'Drażliwość')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (18, 'Apatia')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (19, 'Zmęczenie')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (20, 'Wolne gojenie się ran')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (21, 'Ból klatki piersiowej')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (22, 'Dreszcze')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (23, 'Płytki oddech')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (24, 'Wydzielina z płuc')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (25, 'Ból mięsni')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (26, 'Ból stawów')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (27, 'Suchy kaszel')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (28, 'Duszności')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (29, 'Poty')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (30, 'Ból brzucha')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (31, 'Wymioty')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (32, 'Ból głowy')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (33, 'Katar')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (34, 'Łzawienie')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (35, 'Wysypka')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (36, 'Nudności')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (37, 'Biegunka')");

conn.execute("INSERT INTO OBJAWY (ID, NAZWA_OBJAWU) \
        VALUES (38, 'Gorączka')");


conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(1,1)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(1,2)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(1,3)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(2,1)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(2,2)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(2,4)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(3,5)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(3,6)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(3,7)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(3,8)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(3,9)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(4,10)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(4,11)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(4,12)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(4,13)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(4,14)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(4,15)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(5,10)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(5,11)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(5,16)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(5,17)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(5,18)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(5,19)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(5,14)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(5,20)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(6,21)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(6,22)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(6,23)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(6,24)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(6,38)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(7,38)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(7,25)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(7,26)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(7,27)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(7,28)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(8,38)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(8,22)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(8,29)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(8,27)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(8,13)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(8,21)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(8,30)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(8,31)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(8,28)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(9,38)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(9,32)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(9,26)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(10,33)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(10,34)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(10,35)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(10,28)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(11,36)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(11,31)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(11,30)");

conn.execute("INSERT INTO CHOROBY_OBJAWY_RELACJA (ID_CHOROBY, ID_OBJAWU) \
        VALUES(11,37)");


conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(1,'Nastawienie złamania')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(2,'Środki przeciwbólowe')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(3,'Opatrunek z gipsu')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(4,'Operacja złamania')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(5,'Zszycie rany')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(6,'Odkażenie rany')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(7,'Leki na obniżenie ciśnienia')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(8,'Insulina')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(9,'Metformina')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(10,'Antybiotyk')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(11,'Leki przeciwgorączkowe')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(12,'Syrop na kaszel')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(13,'Rozgrzanie')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(14,'Wziewy')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(15,'Leki przeciwhistaminowe')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(16,'Lek przeciwleukotrienowy')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(17,'Glikokortykosteroidy')");

conn.execute("INSERT INTO LEKI (ID, NAZWA_LEKU) \
        VALUES(18,'Sterydy')");


conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(1,1)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(1,2)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(1,3)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(2,1)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(2,5)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(2,6)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(2,2)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(2,4)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(2,3)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(3,7)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(4,8)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(5,8)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(5,9)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(6,10)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(6,11)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(6,12)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(7,10)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(7,11)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(7,12)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(7,2)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(8,2)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(8,10)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(8,11)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(8,12)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(9,13)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(9,2)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(9,12)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(9,11)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(10,14)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(10,15)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(10,16)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(11,15)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(11,17)");

conn.execute("INSERT INTO CHOROBY_LEKI_RELACJA (ID_CHOROBY, ID_LEKU) \
        VALUES(11,18)");


conn.commit()
print ("Records created successfully")
conn.close()
