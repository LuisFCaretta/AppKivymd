#pylint:disable=C0103
#pylint:disable=W0201
#pylint:disable=R0901
#pylint:disable=C0115
#pylint:disable=C0116
#pylint:disable=W0311
import sqlite3
from datetime import date, datetime, timedelta

class DataBaseControle:
	def __init__(self):
		self.conn = sqlite3.connect('dbcontrole.db')
		
		self.cursor = self.conn.cursor()
		self.cursor.execute(
						"CREATE TABLE IF NOT EXISTS controle(id INTEGER PRIMARY KEY, Nome TEXT, Valor FLOAT, Data_vencimento DATE, Categoria TEXT, Status TEXT);"
		)
		self.conn.commit()
		
		
		
	def fetch_all(self):
		self.cursor.execute("SELECT * FROM controle;")
		row = self.cursor.fetchall()
		return row
	
	def filter_categoria(self,Categoria):
	    self.cursor.execute("SELECT * FROM controle WHERE Categoria = ?;", (Categoria,))
	    row = self.cursor.fetchall()
	    return row
	    
	def filter_periodo(self,data_inicio, data_final):
	    self.cursor.execute('SELECT * FROM controle WHERE Data_vencimento BETWEEN ? AND ?;', (data_inicio, data_final,))
	    row = self.cursor.fetchall()
	    return row
	    
	def filter_month(self, data_inicio, data_final):
	    self.cursor.execute('SELECT * FROM controle WHERE Data_vencimento BETWEEN ? AND ?;', (data_inicio, data_final,))
	    row = self.cursor.fetchall()
	    return row
	    
	def filter_all(self, Categoria, data_inicio, data_final):
		self.cursor.execute("SELECT * FROM controle WHERE Categoria = ? AND Data_vencimento BETWEEN ? AND ?;", (Categoria, data_inicio, data_final,))
		row = self.cursor.fetchall()
		return row
	

	def get_record_by_id(self, id):
	       self.cursor.execute(
	       		"SELECT * FROM controle WHERE id=?;", (id,)
	       		)
	       row = self.cursor.fetchone()
	       return row
	       
	       
	def insert(self, conta, valor, data, categoria, status):
		self.cursor.execute(
				"INSERT INTO controle(id, Nome, Valor, Data_vencimento, Categoria, Status) VALUES (NULL, ?, ?, ?, ?, ?);", (conta, valor, data, categoria, status)
				)
		self.conn.commit()
		
	def delete(self, id):
	       self.cursor.execute(
	       		"DELETE FROM controle where id=?;", (id,)
	       		)
	       self.conn.commit()
	       
	def update(self, Nome, Valor, Data_vencimento, Categoria, Status, id):
		self.cursor.execute(
				"UPDATE controle SET Nome=?, Valor=?, Data_vencimento=?, Categoria=?, Status=? WHERE id=?", (Nome, Valor, Data_vencimento, Categoria, Status, id)
				)
		self.conn.commit()
		
	def update_status(self, id):
		self.cursor.execute(
				"UPDATE controle SET Status='Pago' WHERE id=?", (id,)
				)
		self.conn.commit()
		
	def __del__(self):
		
		self.conn.close()
		
		
		
DataBaseControle()