import sqlite3

def connect():
    conn=sqlite3.connect("garden.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS plant (id INTEGER PRIMARY KEY, type text, location INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS info (plant INTEGER, type text, date_planted text )")
    cur.execute("CREATE TABLE IF NOT EXISTS harvest (plant INTEGER, amount I NTEGER, measure text, date text)")
    conn.commit()
    conn.close()
    
connect()