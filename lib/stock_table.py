from email import header
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class Table(qtw.QTableWidget):
	def __init__(self):
		super().__init__()


		#self.createTable()



	def createTable(self,data):
		rows = len(self.data['data'])
		cols = len(self.data['header'])

		# init table
		table = qtw.QTableWidget()
		table.setRowCount(rows)
		table.setColumnCount(cols)
		table.setHorizontalHeaderLabels(self.data['header'])
		# table.setMinimumHeight(rows*100)
		# table.setMinimumWidth(cols*300)

		# set data
		for i,row in enumerate(self.data['data']):
			for j,item in enumerate(row):
				table.setItem(i,j,qtw.QTableWidgetItem(item))

		table.resizeColumnsToContents()

		# streach table:
		# table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
		# table.verticalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)



		self.table = table
		self.table.show()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	window = Table()

	sys.exit(app.exec())