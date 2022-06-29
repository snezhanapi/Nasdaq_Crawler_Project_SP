import sys
from PyQt6 import QtWidgets as qtw
from lib.MainMenuFormPyQT import MainMenuWindow
from lib.stock_table import Table
from lib.db import DB

class MainWindow(MainMenuWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.show()

	def get_data(self):
		db = DB()
		stock_data = db.get_stock_data()

		header = ("stock_date", "close_last", "volume", "open_price", "high_price", "low_price", "stock_code")

		return {
			"header":header,
			"data":stock_data
		}

	def stock_select_button_clicked(self):
		# stock_data_table = self.import_crawler_data_to_db()
		# print(stock_data_table)

		### get data from DB, no need to crawl, if crawler have saved them in DB
		stock_data = self.get_data()
		self.list_of_stocks = self.stock_db.view_stocks()
		self.stock_select_combobox.setHidden(True)
		self.stock_select_button.setHidden(True)

		stock_table = Table(stock_data=stock_data)

		# embed table into main window:
		main_widget = qtw.QWidget(self)
		main_layout = qtw.QVBoxLayout()
		table_label = qtw.QLabel('This is stock data table')

		main_layout.addWidget(table_label)
		main_layout.addWidget(stock_table)
		main_widget.setLayout(main_layout)
		self.setCentralWidget(main_widget)


		# stock_table.createTable(stock_data_table)

		print("finished")

if __name__ == "__main__":
	app = qtw.QApplication(sys.argv)

	main = MainWindow()

	sys.exit(app.exec())