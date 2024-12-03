import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel

# Функция для инициализации базы данных
def init_db():
    conn = sqlite3.connect('open.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS app_launches (
            id INTEGER PRIMARY KEY AUTOINCREMENT
        )
    ''')
    conn.commit()
    conn.close()

# Функция для добавления записи о запуске приложения
def add_launch_record():
    conn = sqlite3.connect('open.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO app_launches DEFAULT VALUES')
    conn.commit()
    cursor.execute('SELECT COUNT(*) FROM app_launches')
    count = cursor.fetchone()[0]
    conn.close()
    return count

# Главное окно приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("Показать счетчик запусков")
        self.button.clicked.connect(self.open_counter_window)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.counter_window = None  # Хранение окна счетчика
        self.has_recorded_launch = False  # Флаг для учета запуска

        # Запись первого запуска
        if not self.has_recorded_launch:
            add_launch_record()
            self.has_recorded_launch = True  # Устанавливаем флаг

    def open_counter_window(self):
        count = self.get_launch_count()  # Получаем количество запусков
        if self.counter_window is None or not self.counter_window.isVisible():
            self.counter_window = CounterWindow(count)
            self.counter_window.show()

    def get_launch_count(self):
        conn = sqlite3.connect('open.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM app_launches')
        count = cursor.fetchone()[0]
        conn.close()
        return count

# Окно со счетчиком запусков
class CounterWindow(QWidget):
    def __init__(self, count):
        super().__init__()
        self.setWindowTitle("Счетчик запусков")
        self.setGeometry(150, 150, 200, 100)

        self.label = QLabel(f"Запусков приложения: {count}")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
