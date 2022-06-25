import sys
from PyQt6 import QtWidgets as qtw
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QComboBox, QPushButton
#from PyQt6 import QtCore as qtc
#from PyQt6 import QtGui as qtg
from PyQt6.QtGui import QPixmap, QIcon
from lib.db import DB

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

		self.stock = DB()
		self.list_of_stocks = self.stock.view_stocks()

		self.show()
		self.add_menubar()
		self.add_statusbar("Welcome!")
		self.add_toolbar()


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

	def add_toolbar(self):
		toolbar = self.addToolBar('File')

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

		stock_select_layout = QVBoxLayout()
		stock_select_button = QPushButton("Select")

		stock_select_layout.addWidget(self.stock_select_combobox)
		stock_select_layout.addWidget(stock_select_button)
		container = qtw.QWidget()
		container.setLayout(stock_select_layout)
		self.setCentralWidget(container)
		stock_select_button.show()
		stock_select_button.clicked.connect(self.stock_select_button_clicked)


	def stock_select_button_clicked(self):

		self.selected_stock = self.stock_select_combobox.currentText()
		print(self.selected_stock)


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)
	window = MainMenuWindow()

	sys.exit(app.exec())