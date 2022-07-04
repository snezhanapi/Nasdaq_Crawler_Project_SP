import sys
from PyQt6 import QtWidgets as qtw
from lib.MainMenuFormPyQT import MainMenuWindow
from lib.stock_table import Table
from lib.db import DB


# from lib.stock_table_view import TableModel

class MainWindow(MainMenuWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show()

    def stock_select_button_clicked(self):
        # stock_data_table = self.import_crawler_data_to_db()
        data_base = DB()
        stock_data_table = data_base.get_stock_data("AAT")
        header = data_base.get_column_names()
        stock_data_dict = {
            "header": header,
            "data": stock_data_table
        }

        print(stock_data_dict)

        self.stock_select_combobox.setHidden(True)
        self.stock_select_button.setHidden(True)

        self.stock_table = Table(stock_data_dict)
        self.stock_table.show()
        main_widget = qtw.QWidget(self)
        main_layout = qtw.QVBoxLayout()

        main_layout.addWidget(self.stock_table)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # self.table = qtw.QTableView()
        # self.model = TableModel(stock_data_table)
        # self.table.setModel(self.model)
        # stock_table_layout = qtw.QVBoxLayout()
        # stock_table_layout.addWidget(self.stock_table)
        # container = qtw.QWidget(self)
        # container.setLayout(stock_table_layout)
        # self.setCentralWidget(container)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    main = MainWindow()

    # sys.exit(app.exec())
    app.exec()
    sys.exit(5)
