import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from db import DB
import pandas as pd

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data


    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])

if __name__ == '__main__':
    class MainWindow(QtWidgets.QMainWindow):
         def __init__(self):
            super().__init__()

            self.table = QtWidgets.QTableView()
            selected_stock = ("SNES",)
            db = DB()
            stock_data = db.get_stock_data(selected_stock)

            header = ("stock_record", "currency", "stock_date", "close_last", "volume", "open_price", "high_price", "low_price", "stock_code")



            data = pd.DataFrame([stock_data], columns = [header])

           # for i, row in enumerate(data['data']):
            #    for j, item in enumerate(row):
            #        if isinstance(item, datetime.date):
            #            item = item.strftime('%Y-%m-%d')
            #        self.setItem(i, j, qtw.QTableWidgetItem(str(item)))

            print(data)
            self.model = TableModel(data['data'])
            self.table.setModel(self.model)

            self.setCentralWidget(self.table)


    app=QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()