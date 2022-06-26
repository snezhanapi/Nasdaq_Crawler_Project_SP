import sys
from PyQt6 import QtWidgets as qtw
from lib.MainMenuFormPyQT import MainMenuWindow
from lib.stock_table import Table

class MainWindow(MainMenuWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show()


    def stock_select_button_clicked(self):
        data = self.import_crawler_data_to_db()
        self.list_of_stocks = self.stock_db.view_stocks()
        self.stock_select_combobox.setHidden(True)
        self.stock_select_button.setHidden(True)
        print("worked")
        stock_table = Table()
        stock_table.create_table(data)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    main = MainWindow()

    sys.exit(app.exec())