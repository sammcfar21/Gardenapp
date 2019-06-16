import sqlite3
from datetime import date, datetime

def selector():
	print("What information do you want to input? (plant, info, harvest, exit)")
	select = input()
	if select == 'plant':
		plant()
		continue
	elif select == 'info':
		info()
		continue
	elif select == 'harvest':
		harvest()
		continue
	elif select == 'exit':
		exit()
	
	selector()
	
def plant():
	print('Input Plant Type:')
	type = input()
	print ('Input Location:')
	loc = input()
    conn=sqlite3.connect("garden.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO plant VALUES (NULL,?,?)",(type,loc))
    conn.commit()
    conn.close()
 
 
def info():
	print('What plant is this? :')
	plant = input()
	print ('Is this a seedling or a seed? :')
	type = input()
	print ('What is the date? :')
	date = input()
    conn=sqlite3.connect("garden.db")
    cur = conn.cursr()
    cur.execute('INSERT INTO info VALUES (?,?,?)', (plant, type, date))
   
    
def harvest():
    conn=sqlite3.connect("garden.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS plant (id INTEGER PRIMARY KEY, type text, location integer)")
    conn.commit()
    conn.close()
    
    
