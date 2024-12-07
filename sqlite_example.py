import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QMessageBox, QTableWidget, \
    QTableWidgetItem, QHBoxLayout, QLabel, QScrollArea
from PyQt6.QtGui import QPixmap


def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT
        )
    ''')

    # Create orders table to store order history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            order_details TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Главное окно приложения
class MainWindow(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.setWindowTitle("Меню Макдональдса")

        # Элементы меню
        self.menu_items = [
            MenuItem("🍔Чизбургер🍔", 180),
            MenuItem("🍟Картошка фри🍟", 100),
            MenuItem("🥤Напиток🥤", 50),
            MenuItem("🥟Наггетсы🥟", 200),
            MenuItem("🥗Салат Цезарь🥗", 250),
            MenuItem("🥛Молочный коктейль🥛", 120),
            MenuItem("🍔Фишбургеры🍔", 160),
            MenuItem("🥮Пирожок с вишней🥮", 70),
            MenuItem("☕Кофе☕", 90)
        ]

        self.cart = []
        self.order_history = []
        self.user_id = user_id
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Создаем прокрутку
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()

        # Меню
        for item in self.menu_items:
            h_layout = QHBoxLayout()
            h_layout.addWidget(QLabel(f"{item.name} - {item.price} ₽"))
            button = QPushButton("+")
            button.clicked.connect(lambda checked, item=item: self.add_to_cart(item))
            h_layout.addWidget(button)
            scroll_layout.addLayout(h_layout)

        scroll_widget.setLayout(scroll_layout)
        scroll.setWidget(scroll_widget)

        layout.addWidget(scroll)

        # Кнопки корзины и истории заказов
        button_cart = QPushButton("Корзина")
        button_cart.clicked.connect(self.open_cart)
        layout.addWidget(button_cart)

        button_history = QPushButton("История заказов")
        button_history.clicked.connect(self.open_order_history)
        layout.addWidget(button_history)

        self.setLayout(layout)

    def add_to_cart(self, item):
        self.cart.append(item)
        QMessageBox.information(self, "Добавлено в корзину", f"{item.name} добавлено в корзину!")

    def open_cart(self):
        if not self.cart:
            QMessageBox.information(self, "Корзина пуста", "Ваша корзина пуста!")
            return
        self.cart_window = CartWindow(self.cart, self.order_history, self.user_id)
        self.cart_window.show()

    def open_order_history(self):
        self.history_window = OrderHistoryWindow(self.user_id)
        self.history_window.show()


class CartWindow(QWidget):
    def __init__(self, cart, order_history, user_id):
        super().__init__()
        self.setWindowTitle("Корзина")
        self.cart = cart
        self.order_history = order_history
        self.user_id = user_id
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.cart_table = QTableWidget()
        self.cart_table.setRowCount(len(self.cart))
        self.cart_table.setColumnCount(3)
        self.cart_table.setHorizontalHeaderLabels(["Наименование", "Цена (руб)", "Удалить"])

        for row, item in enumerate(self.cart):
            self.cart_table.setItem(row, 0, QTableWidgetItem(item.name))
            self.cart_table.setItem(row, 1, QTableWidgetItem(str(item.price)))
            remove_button = QPushButton("Убрать")
            remove_button.clicked.connect(lambda checked, row=row: self.remove_item(row))
            self.cart_table.setCellWidget(row, 2, remove_button)

        layout.addWidget(self.cart_table)

        # Кнопки заказа и возврата в меню
        order_button = QPushButton("Заказать")
        order_button.clicked.connect(self.open_order_dialog)
        layout.addWidget(order_button)

        back_button = QPushButton("Назад в меню")
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def remove_item(self, row):
        item_name = self.cart[row].name
        self.cart.pop(row)  # Удаляем товар из корзины
        QMessageBox.information(self, "Удалено из корзины", f"{item_name} убрано из корзины!")
        self.refresh_cart()

    def refresh_cart(self):
        self.cart_table.setRowCount(len(self.cart))
        for row, item in enumerate(self.cart):
            self.cart_table.setItem(row, 0, QTableWidgetItem(item.name))
            self.cart_table.setItem(row, 1, QTableWidgetItem(str(item.price)))
            remove_button = QPushButton("Убрать")
            remove_button.clicked.connect(lambda checked, row=row: self.remove_item(row))
            self.cart_table.setCellWidget(row, 2, remove_button)

    def open_order_dialog(self):
        if not self.cart:
            QMessageBox.information(self, "Корзина пуста", "Добавьте товары в корзину для оформления заказа.")
            return
        self.order_dialog = OrderDialog(self.cart, self.user_id)
        self.order_dialog.show()
        self.close()


class OrderDialog(QWidget):
    def __init__(self, cart, user_id):
        super().__init__()
        self.setWindowTitle("Введите данные карты")
        self.cart = cart
        self.user_id = user_id
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.card_number_input = QLineEdit()
        self.card_number_input.setPlaceholderText("Введите 16 цифр номера карты")
        layout.addWidget(self.card_number_input)

        pay_button = QPushButton("Оплатить")
        pay_button.clicked.connect(self.confirm_order)
        layout.addWidget(pay_button)

        self.setLayout(layout)

    def confirm_order(self):
        # Check card validity or promo code
        valid_promo_codes = ["DISCOUNT10", "FREESHIP", "WELCOME50", "NEWYEAR15", "пж100баллов", "NEWYEAR", "MACMENU", "1"]
        card_number = self.card_number_input.text()
        if len(card_number) == 16 and card_number.isdigit() or card_number in valid_promo_codes:
            # Save the order in the database
            order_details = ', '.join([item.name for item in self.cart])
            self.save_order(order_details)
            self.cart.clear()  # Empty the cart
            QMessageBox.information(self, "Заказ подтвержден", "Ваш заказ успешно оплачен!")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неправильный номер карты или промокод. Введите коректные данные.")

    def save_order(self, order_details):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Insert order into orders table
        cursor.execute('INSERT INTO orders (user_id, order_details, status) VALUES (?, ?, ?)',
                       (self.user_id, order_details, "Оплачен"))

        conn.commit()
        conn.close()


class OrderHistoryWindow(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.setWindowTitle("История заказов")
        self.user_id = user_id
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.history_table = QTableWidget()
        self.history_table.setRowCount(0)
        self.history_table.setColumnCount(2)
        self.history_table.setHorizontalHeaderLabels(["Заказ", "Статус"])

        # Fetch order history from the database
        self.load_order_history()

        layout.addWidget(self.history_table)

        back_button = QPushButton("Назад в меню")
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def load_order_history(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Fetch orders for the current user
        cursor.execute('SELECT order_details, status FROM orders WHERE user_id=?', (self.user_id,))
        orders = cursor.fetchall()

        conn.close()

        # Add each order to the table
        for order in orders:
            order_details, status = order
            row_position = self.history_table.rowCount()
            self.history_table.insertRow(row_position)
            self.history_table.setItem(row_position, 0, QTableWidgetItem(order_details))
            self.history_table.setItem(row_position, 1, QTableWidgetItem(status))
