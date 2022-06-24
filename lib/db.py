import mysql.connector
#pip install configparser
from configparser import ConfigParser
from dateutil import parser
import datetime

class DB:
	def __init__(self):
		db_config = DB.read_db_config(filename='../config.ini', section='MYSQL')

		try:
			self.cnx = mysql.connector.connect(
				user=db_config['user'],
				password=db_config['password'],
				db=db_config['db'],
				host=db_config['host'],
				port=db_config['port']
			)
		except mysql.connector.Error as e:
			print(e)
			exit()

	def read_db_config(filename='../config.ini', section='MYSQL'):
		""" Read database configuration file and return a dictionary object
				:param filename: name of the configuration file
				:param section: section of database configuration
				:return: a dictionary of database parameters
		"""
		# create parser and read the configuration file
		parser = ConfigParser()
		parser.read(filename)


		db_config = {}

		if parser.has_section(section):
				items = parser.items(section)
				for item in items:
						db_config[item[0]] = item[1]
		else:
				raise Exception(f'{section} not found in the {filename} file')

		return db_config

	def view_stocks(self):
		c = self.cnx.cursor()
		q = f"""
					SELECT * FROM nasdaq.stock_list

				"""
		c.execute(q)
		result = c.fetchall()
		print(list(result))
		return list(result)
	def insert_stock(self):
		row = ['06/23/2022', '$83.9123', '17,903', '$83.9123', '$83.9123', '$83.9123']
		counter = 1
		stock_data_list = list()
		stock = "AAPL"
		for i in row:
			# print(i)
			if counter == 1:
				stock_date = parser.parse(i)
				i = stock_date.date().isoformat()
			elif counter == 3:
				i = int(i.replace(',', ''))
			else:
				i = float(i.replace('$', ''))
			counter += 1
			stock_data_list.append(i)

		stock_data_list.append(stock)
		cd = self.cnx.cursor()
		sql = "INSERT INTO nasdaq.stock_data (stock_date, close_last, volume, open_price, high_price, low_price, stock_code)" \
			  "VALUES (%s,%s,%s,%s,%s,%s,%s)"
		cd.execute(sql, tuple(stock_data_list))
		self.cnx.commit()
		cd.close()

if __name__ == '__main__':
	db = DB()
	db.insert_stock()