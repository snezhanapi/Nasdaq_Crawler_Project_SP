import sys
from PyQt6 import QtWidgets as qtw
from lib.MainMenuFormPyQT import MainMenuWindow
from lib.stock_table import Table
#from lib.stock_table_view import TableModel

class MainWindow(MainMenuWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show()


    def stock_select_button_clicked(self):
        stock_data_table = self.import_crawler_data_to_db()
        print(stock_data_table)
        self.list_of_stocks = self.stock_db.view_stocks()
        self.stock_select_combobox.setHidden(True)
        self.stock_select_button.setHidden(True)
        self.stock_table = Table(stock_data_table)

        # self.table = qtw.QTableView()
        # self.model = TableModel(stock_data_table)
        # self.table.setModel(self.model)
        #stock_table_layout = qtw.QVBoxLayout()
        #stock_table_layout.addWidget(self.stock_table)
        #container = qtw.QWidget(self)
        #container.setLayout(stock_table_layout)
        #self.setCentralWidget(container)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    main = MainWindow()

    sys.exit(app.exec())