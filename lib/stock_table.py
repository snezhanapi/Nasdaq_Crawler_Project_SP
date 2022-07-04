from email import header
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
import datetime

class Table(qtw.QTableWidget):
	def __init__(self, stock_data):
		super().__init__()
		print("table started")
		self.createTable(stock_data)
		#self.table.show()


	def createTable(self, data):
		print(f"Data in create table:{data}")
		rows = len(data['data'])
		cols = len(data['header'])

		# init table
		#self.table = qtw.QTableWidget()
		self.setRowCount(rows)
		self.setColumnCount(cols)
		self.setHorizontalHeaderLabels(data['header'])
		# table.setMinimumHeight(rows*100)
		# table.setMinimumWidth(cols*300)

		# set data
		for i,row in enumerate(data['data']):
			for j,item in enumerate(row):
				if isinstance(item, datetime.date):
					item = item.strftime('%Y-%m-%d')
				self.setItem(i, j, qtw.QTableWidgetItem(str(item)))

		self.resizeColumnsToContents()

		# streach table:
		# table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
		# table.verticalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)

		#self.table.show()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	window = Table()

	sys.exit(app.exec())