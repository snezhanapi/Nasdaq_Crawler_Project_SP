import sys
from PyQt6 import QtWidgets as qtw
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
#from PyQt6 import QtCore as qtc
#from PyQt6 import QtGui as qtg
from PyQt6.QtGui import QPixmap, QIcon
class MainMenuWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Stock Prices')
		self.setWindowIcon(QIcon('nasdaq.png'))
		self.setGeometry(200,150,800,500)
		#self.pixmap = QPixmap(r".\stock-market.jpg")
		#self.resize(self.pixmap.width(), self.pixmap.height())


		self.label = QLabel(self)
		self.pixmap = QPixmap(".\stock-market.jpg")
		self.label.setPixmap(self.pixmap)
		self.label.resize(self.pixmap.width(),
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
		view_action = stock_menu.addAction('Stock  Data')
		# add separator
		#sales_menu.addSeparator()

	def add_toolbar(self):
		toolbar = self.addToolBar('File')

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)

	window = MainMenuWindow()

	sys.exit(app.exec())