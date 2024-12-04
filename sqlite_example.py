import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QTableWidget, \
    QTableWidgetItem


class RestaurantFinder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Поиск ресторанов в Санкт-Петербурге")
        self.setGeometry(100, 100, 300, 400)  # Изменили размер окна

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.region_label = QLabel("Выберите район:")
        self.region_combo = QComboBox()
        self.region_combo.addItems([
            "Не выбран",
            "Адмиралтейский",
            "Василеостровский",
            "Выборгский",
            "Калининский",
            "Кировский",
            "Колпинский",
            "Красногвардейский",
            "Красносельский",
            "Кронштадтский",
            "Курортный",
            "Московский",
            "Невский",
            "Петроградский",
            "Приморский",
            "Пушкинский",
            "Фрунзенский",
            "Центральный"
        ])
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

        # Подключаемся к существующей базе данных
        self.conn = sqlite3.connect("restaurant.db")  # Замените на путь к вашей базе данных
        self.update_table()  # Начальный вызов обновления таблицы

    def update_table(self):
        region = self.region_combo.currentText()
        address = self.address_input.text()

        cursor = self.conn.cursor()

        # Подготовка запроса
        if region == "Не выбран":
            query = "SELECT address, region FROM restaurants WHERE address LIKE ?"
            cursor.execute(query, (f"%{address}%",))
        else:
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
