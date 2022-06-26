from email import header
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class Table(qtw.QTableWidget):
	def __init__(self,stock_data):
		super().__init__()
		self.stock_data = stock_data
		self.createTable(stock_data)
		self.table.show()


	def createTable(self, data):
		rows = len(data['data'])
		cols = len(data['header'])

		# init table
		table = qtw.QTableWidget()
		table.setRowCount(rows)
		table.setColumnCount(cols)
		table.setHorizontalHeaderLabels(data['header'])
		# table.setMinimumHeight(rows*100)
		# table.setMinimumWidth(cols*300)

		# set data
		for i,row in enumerate(data['data']):
			for j,item in enumerate(row):
				table.setItem(i,j,qtw.QTableWidgetItem(item))

		table.resizeColumnsToContents()

		# streach table:
		# table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
		# table.verticalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)



		self.table = table




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	window = Table()

	sys.exit(app.exec())