import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лицензионное соглашение")
        self.setGeometry(100, 100, 400, 300)

        # Создаем центральный виджет и устанавливаем для него вертикальный макет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Кнопка для открытия лицензионного соглашения
        self.show_button = QPushButton("Показать лицензионное соглашение")
        self.show_button.clicked.connect(self.show_license_agreement)

        # Кнопка "Назад", которая ничего не делает
        self.back_button = QPushButton("Назад")
        self.back_button.clicked.connect(self.back_action)  # Привязываем действие, которое ничего не делает

        # Текстовое поле для отображения лицензионного соглашения
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # Делаем текстовое поле только для чтения

        # Добавляем кнопки и текстовое поле в макет
        self.layout.addWidget(self.show_button)
        self.layout.addWidget(self.back_button)
        self.layout.addWidget(self.text_edit)

    def show_license_agreement(self):
        # Чтение лицензионного соглашения из файла
        with open('license_agreement.txt', 'r', encoding='utf-8') as file:
            license_text = file.read()

        # Установите текст лицензионного соглашения в текстовое поле
        self.text_edit.setPlainText(license_text)

    def back_action(self):
        # Действие кнопки "Назад", которое ничего не делает
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
