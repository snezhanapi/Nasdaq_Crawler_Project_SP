import sys
from PyQt6 import QtWidgets as qtw
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox
#from PyQt6 import QtCore as qtc
#from PyQt6 import QtGui as qtg
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class MainMenuWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Stock Prices')
		self.setWindowIcon(QIcon('nasdaq.png'))
		self.setGeometry(200,150,800,500)



		self.label_image = QLabel(self)
		self.pixmap = QPixmap(".\stock-market.jpg")
		self.label_image.setPixmap(self.pixmap)
		self.label_image.resize(self.pixmap.width(),
						  self.pixmap.height())


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
		stock_select_combobox = QComboBox()
		stock_select_combobox.addItem('AAPL')
		stock_select_layout = QVBoxLayout()
		stock_select_layout.addWidget(stock_select_combobox)

		container = qtw.QWidget()
		container.setLayout(stock_select_layout)

		self.setCentralWidget(container)

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)


	window = MainMenuWindow()

	sys.exit(app.exec())