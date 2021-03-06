import sys
from PyQt6 import QtWidgets as qtw
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QComboBox, QPushButton
#from PyQt6 import QtCore as qtc
#from PyQt6 import QtGui as qtg
from PyQt6.QtGui import QPixmap, QIcon
from lib.db import DB
from lib.crawler import Crawler_Nasdaq
from dateutil import parser
import datetime


class MainMenuWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Stock Prices')
		self.setWindowIcon(QIcon('nasdaq.png'))
		self.setGeometry(200,150,800,500)



		self.label_image = QLabel(self)
		self.pixmap = QPixmap(".\lib\stock-market.jpg")
		self.label_image.setPixmap(self.pixmap)
		self.label_image.resize(self.pixmap.width(),
						  self.pixmap.height())

		self.stock_db = DB()
		self.list_of_stocks = self.stock_db.view_stocks()


		self.add_menubar()
		self.add_statusbar("Welcome!")
		#self.add_toolbar()
		self.show()

	def add_statusbar(self,text):
		s = qtw.QStatusBar(self)
		self.setStatusBar(s)
		s.showMessage(text)

	def add_menubar(self):
		# get the menu bar
		menubar = self.menuBar()

		# add menu items
		stock_menu = menubar.addMenu('&Stock')
		help_menu = menubar.addMenu('He&lp')

		# add actions
		view_action = stock_menu.addAction('Stock Data')
		view_action.triggered.connect(self.stock_menu_clicked)
		# add separator
		#sales_menu.addSeparator()

	#def add_toolbar(self):
		#toolbar = self.addToolBar('File')

	def stock_menu_clicked(self):
		self.label_image.setHidden(True)
		#label = QLabel("StockName")
		#label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		#self.setCentralWidget(label)
		self.stock_list_box()
		#combobox.activated.connect(self.activated)

	def stock_list_box(self):

		self.stock_select_combobox = QComboBox()
		stock_list = list(list(zip(*(self.list_of_stocks)))[0])
		self.stock_select_combobox.addItems(stock_list)

		self.stock_select_layout = QVBoxLayout()
		self.stock_select_button = QPushButton("Select")

		self.stock_select_layout.addWidget(self.stock_select_combobox)
		self.stock_select_layout.addWidget(self.stock_select_button)
		container = qtw.QWidget()
		container.setLayout(self.stock_select_layout)
		self.setCentralWidget(container)
		self.stock_select_button.show()
		self.stock_select_button.clicked.connect(self.stock_select_button_clicked)




	def import_crawler_data_to_db(self):
		selected_stock = self.stock_select_combobox.currentText()
		print(selected_stock)
		base_stock_url = 'https://www.nasdaq.com/market-activity/stocks/' + selected_stock.lower() + '/historical'
		print(base_stock_url)
		self.stock_crawler = Crawler_Nasdaq(base_stock_url)
		crawler_data = self.stock_crawler.get_table_rows()
		print(crawler_data)
		self.stock_data_selected = list()
		for row in crawler_data:
			row_list = list(row.text.split(" "))

			counter = 1
			stock_data_list = list()
			for i in row_list:
				if counter == 1:
					stock_date = parser.parse(i)
					i = stock_date.date().isoformat()
				elif counter == 3:
					i = int(i.replace(',', ''))
				else:
					i = float(i.replace('$', ''))
				counter += 1
				stock_data_list.append(i)


			stock_data_list.append(selected_stock)

			print(stock_data_list)
			self.stock_db.insert_stock(stock_data_list)
			self.stock_data_selected.append(tuple(map(str,stock_data_list)))

		header = ("stock_date", "close_last", "volume", "open_price", "high_price", "low_price", "stock_code")

		stock_data = tuple(self.stock_data_selected)

		return {
			"header":header,
			"data":stock_data
		}


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	window = MainMenuWindow()

	sys.exit(app.exec())