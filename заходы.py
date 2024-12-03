import sys
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
import os


# Функция для инициализации файла
def init_counter_file(filename='launch_count.txt'):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write('0')  # Начальное значение счетчика


# Функция для чтения количества запусков из файла
def read_launch_count(filename='launch_count.txt'):
    with open(filename, 'r') as file:
        count = int(file.read().strip())
    return count


# Функция для увеличения счетчика запусков
def increment_launch_count(filename='launch_count.txt'):
    count = read_launch_count(filename)
    count += 1
    with open(filename, 'w') as file:
        file.write(str(count))


# Главное окно приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        self.setGeometry(100, 100, 300, 200)

        self.pixmap = QPixmap('mini.jpg')
        self.image = QLabel(self)
        self.image.move(60, 40)
        self.image.resize(450, 350)
        self.image.setPixmap(self.pixmap)

        self.button = QPushButton("Показать счетчик запусков")
        self.button.clicked.connect(self.open_counter_window)
        self.button.resize(200, 50)
        self.button.move(100, 150)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.counter_window = None  # Хранение окна счетчика

        # Увеличиваем счетчик запусков
        increment_launch_count()

    def open_counter_window(self):
        count = read_launch_count()  # Получаем количество запусков
        if self.counter_window is None or not self.counter_window.isVisible():
            self.counter_window = CounterWindow(count)
            self.counter_window.show()


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
    init_counter_file()  # Инициализация файла перед запуском приложения
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
