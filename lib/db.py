import mysql.connector
#pip install configparser
from configparser import ConfigParser

FILENAME = './config.ini'
class DB:
	def __init__(self):

		db_config = DB.read_db_config(filename=FILENAME, section='MYSQL')

		try:
			self.cnx = mysql.connector.connect(
				user=db_config['user'],
				password=db_config['password'],
				db=db_config['db'],
				host=db_config['host'],
				port=db_config['port']
			)
			self.db_config = db_config
		except mysql.connector.Error as e:
			print(e)
			exit()

	def read_db_config(filename=FILENAME, section='MYSQL'):
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
					SELECT stock_code FROM nasdaq.stock_list

				"""
		c.execute(q)
		result = c.fetchall()

		return list(result)

	def insert_stock(self,stock_data_list):

		cd = self.cnx.cursor()
		sql = "INSERT INTO nasdaq.stock_data (stock_date, close_last, volume, open_price, high_price, low_price, stock_code)" \
			  "VALUES (%s,%s,%s,%s,%s,%s,%s)"
		cd.execute(sql, tuple(stock_data_list))
		self.cnx.commit()
		cd.close()

	def get_stock_data(self,selected_stock):
		c = self.cnx.cursor()
		q = f"""
				select * from stock_data WHERE stock_code = %s;
			"""
		c.execute(q,(selected_stock,))
		result = c.fetchall()

		return list(result)

	def get_column_names(self):
		c = self.cnx.cursor()
		q = f"""
						DESCRIBE stock_data;
					"""
		c.execute(q)
		result = c.fetchall()
		column_names = [element[0] for element in result]
		return column_names

if __name__ == '__main__':
	db = DB()
	m = db.get_column_names()

	print(m)