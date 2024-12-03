import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QTableWidget, \
    QTableWidgetItem


class RestaurantFinderCSV(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Поиск ресторанов в Санкт-Петербурге")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.region_label = QLabel("Выберите район:")
        self.region_combo = QComboBox()
        self.region_combo.addItems(["Центральный", "Московский", "Петроградский", "Невский", "Приморский"])
        self.layout.addWidget(self.region_label)
        self.layout.addWidget(self.region_combo)

        self.address_label = QLabel("Введите адрес:")
        self.address_input = QLineEdit()
        self.layout.addWidget(self.address_label)
        self.layout.addWidget(self.address_input)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Адрес", "Район"])
        self.layout.addWidget(self.table)

        self.address_input.textChanged.connect(self.update_table)
        self.region_combo.currentIndexChanged.connect(self.update_table)

        # Читаем данные из CSV
        self.load_data()

    def load_data(self):
        self.restaurants = []
        with open('restaurants.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропустить заголовок
            for row in reader:
                if len(row) == 2:
                    self.restaurants.append(row)
        self.update_table()

    def update_table(self):
        region = self.region_combo.currentText()
        address = self.address_input.text().lower()

        filtered_results = [
            (addr, reg) for addr, reg in self.restaurants
            if reg == region and address in addr.lower()
        ]

        self.table.setRowCount(len(filtered_results))

        for row_idx, (address, region) in enumerate(filtered_results):
            self.table.setItem(row_idx, 0, QTableWidgetItem(address))
            self.table.setItem(row_idx, 1, QTableWidgetItem(region))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RestaurantFinderCSV()
    main_window.show()
    sys.exit(app.exec())
