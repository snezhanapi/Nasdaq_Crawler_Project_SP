from email import header
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class Table(qtw.QTableWidget):
	def __init__(self, stock_data):
		super().__init__()

		self.createTable(stock_data)
		#self.table.show()


	def createTable(self, data):
		rows = len(data['data'])
		cols = len(data['header'])

		# init table
		self.table = qtw.QTableWidget()
		self.table.setRowCount(rows)
		self.table.setColumnCount(cols)
		self.table.setHorizontalHeaderLabels(data['header'])
		# table.setMinimumHeight(rows*100)
		# table.setMinimumWidth(cols*300)

		# set data
		for i,row in enumerate(data['data']):
			for j,item in enumerate(row):
				self.table.setItem(i,j,qtw.QTableWidgetItem(item))

		self.table.resizeColumnsToContents()

		# streach table:
		# table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
		# table.verticalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)

		self.table.show()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	window = Table()

	sys.exit(app.exec())