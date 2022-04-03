import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS DATASET(Image = BLOB NOT NULL)')


def add_data(Image):
	c.execute('INSERT INTO DATASET(Image))
	conn.commit()

def view_all_data():
	c.execute('SELECT * FROM DATASET22222222')
	data = c.fetchall()
	return data