import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QTableWidget, \
    QTableWidgetItem


class RestaurantFinder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Поиск ресторанов в Санкт-Петербурге")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Создаем элементы интерфейса
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

        # Подключаемся к базе данных
        self.conn = sqlite3.connect("restaurants.db")
        self.create_table()

        # Инициализируем таблицу
        self.update_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS restaurants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                address TEXT NOT NULL,
                region TEXT NOT NULL
            )
        ''')
        self.conn.commit()
        self.insert_sample_data()

    def insert_sample_data(self):
        cursor = self.conn.cursor()
        sample_data = [
            ("Улица Пушкина, 1", "Центральный"),
            ("Проспект Невский, 10", "Центральный"),
            ("Улица Ленина, 5", "Московский"),
            ("Набережная реки Фонтанки, 9", "Петроградский"),
            ("Цветочная улица, 22", "Приморский"),
        ]
        cursor.executemany('INSERT INTO restaurants (address, region) VALUES (?, ?)', sample_data)
        self.conn.commit()

    def update_table(self):
        region = self.region_combo.currentText()
        address = self.address_input.text()

        cursor = self.conn.cursor()
        query = "SELECT address, region FROM restaurants WHERE region = ? AND address LIKE ?"
        cursor.execute(query, (region, f"%{address}%"))

        results = cursor.fetchall()
        self.table.setRowCount(len(results))

        for row_idx, (address, region) in enumerate(results):
            self.table.setItem(row_idx, 0, QTableWidgetItem(address))
            self.table.setItem(row_idx, 1, QTableWidgetItem(region))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RestaurantFinder()
    main_window.show()
    sys.exit(app.exec())
