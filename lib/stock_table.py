from email import header
import sys
import datetime
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from lib.db import DB


class Table(qtw.QTableWidget):
	def __init__(self, stock_data):
		super().__init__()

		self.createTable(stock_data)
		# self.table.show()


	def createTable(self, data):
		rows = len(data['data'])
		cols = len(data['header'])

		# init table
		# self.table = qtw.QTableWidget()
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
				self.setItem(i,j,qtw.QTableWidgetItem(str(item)))

		# self.table.resizeColumnsToContents()

		# strech table (QHeaderView.Stretch in pyqt6 : QHeaderView.ResizeMode.Stretch):
		self.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)
		self.verticalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)



if __name__ == '__main__':
	db = DB()
	stock_data = db.get_stock_data()

	header = ("stock_date", "close_last", "volume", "open_price", "high_price", "low_price", "stock_code")

	data = {
		"header":header,
		"data":stock_data
	}
	app = qtw.QApplication(sys.argv)
	window = Table(data)

	sys.exit(app.exec())