import io
import sys
import sqlite3
from PyQt6 import uic
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel,
                             QPushButton, QLineEdit, QMessageBox, QInputDialog,
                             QScrollArea, QHBoxLayout, QTableWidget, QTableWidgetItem,
                             QFormLayout, QTextEdit, QMainWindow, QComboBox)
from PyQt6.QtGui import QPixmap

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>795</width>
    <height>834</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>30</y>
      <width>801</width>
      <height>121</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_28">
       <item>
        <widget class="QPushButton" name="pushButton_33">
         <property name="text">
          <string>Профиль</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_34">
         <property name="text">
          <string>История заказов</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_32">
         <property name="text">
          <string>Создать промокод</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_31">
         <property name="text">
          <string>PushButton</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>150</y>
      <width>241</width>
      <height>571</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_22">
       <item>
        <widget class="QPushButton" name="pushButton_25">
         <property name="text">
          <string>Чизбургер</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_21">
       <item>
        <widget class="QPushButton" name="pushButton_26">
         <property name="text">
          <string>Картошка фри</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_9">
       <item>
        <widget class="QPushButton" name="pushButton">
         <property name="text">
          <string>Напиток</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_8">
       <item>
        <widget class="QPushButton" name="pushButton_2">
         <property name="text">
          <string>Наггетсы</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_7">
       <item>
        <widget class="QPushButton" name="pushButton_3">
         <property name="text">
          <string>Салат Цезарь</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_6">
       <item>
        <widget class="QPushButton" name="pushButton_4">
         <property name="text">
          <string>Молочный коктель</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_5">
       <item>
        <widget class="QPushButton" name="pushButton_5">
         <property name="text">
          <string>Фишбургеры</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_3">
       <item>
        <widget class="QPushButton" name="pushButton_6">
         <property name="text">
          <string>Пирожок с лавой</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_4">
       <item>
        <widget class="QPushButton" name="pushButton_7">
         <property name="text">
          <string>Кофе</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_10">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>150</y>
      <width>151</width>
      <height>571</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_10">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_24"/>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_23"/>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_17"/>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_16"/>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_15"/>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_14"/>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_13"/>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_11"/>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_12"/>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_18">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>150</y>
      <width>271</width>
      <height>571</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_18">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_22">
       <item>
        <widget class="QPushButton" name="pushButton_28">
         <property name="text">
          <string>ⓘ Подробнее...</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_30">
         <property name="text">
          <string>В Корзину 🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_21">
       <item>
        <widget class="QPushButton" name="pushButton_27">
         <property name="text">
          <string>ⓘ Подробнее...</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_29">
         <property name="text">
          <string>В Корзину 🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_7">
       <item>
        <widget class="QPushButton" name="pushButton_9">
         <property name="text">
          <string>ⓘ Подробнее...</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_8">
         <property name="text">
          <string>В Корзину 🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_6">
       <item>
        <widget class="QPushButton" name="pushButton_11">
         <property name="text">
          <string>ⓘ Подробнее...</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_10">
         <property name="text">
          <string>В Корзину 🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_5">
       <item>
        <widget class="QPushButton" name="pushButton_13">
         <property name="text">
          <string>ⓘ Подробнее...</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_12">
         <property name="text">
          <string>В Корзину 🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_4">
       <item>
        <widget class="QPushButton" name="pushButton_15">
         <property name="text">
          <string>ⓘ Подробнее...</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_14">
         <property name="text">
          <string>В Корзину 🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_3">
       <item>
        <widget class="QPushButton" name="pushButton_19">
         <property name="text">
          <string>ⓘ Подробнее...</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_16">
         <property name="text">
          <string>В Корзину 🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_2">
       <item>
        <widget class="QPushButton" name="pushButton_20">
         <property name="text">
          <string>ⓘ Подробнее...</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_17">
         <property name="text">
          <string>В Корзину 🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QPushButton" name="pushButton_21">
         <property name="text">
          <string>ⓘ Подробнее...</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_18">
         <property name="text">
          <string>В Корзину 🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_8">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>720</y>
      <width>791</width>
      <height>71</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_8">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_11">
       <item>
        <widget class="QPushButton" name="pushButton_22">
         <property name="text">
          <string>⛔ Выйти из Аккаунта ⛔</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_10">
       <item>
        <widget class="QPushButton" name="pushButton_23">
         <property name="text">
          <string>🛒 Корзина🛒</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_9">
       <item>
        <widget class="QPushButton" name="pushButton_24">
         <property name="text">
          <string>⚙Настройки⚙</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>-1</x>
      <y>1</y>
      <width>791</width>
      <height>31</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_19">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_29"/>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_4">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>150</y>
      <width>101</width>
      <height>571</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_20">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_20">
       <item>
        <widget class="QLabel" name="label_9">
         <property name="text">
          <string>⩥ 180₽</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_19">
       <item>
        <widget class="QLabel" name="label_8">
         <property name="text">
          <string>⩥ 100₽</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_18">
       <item>
        <widget class="QLabel" name="label">
         <property name="text">
          <string>⩥ 50₽</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_17">
       <item>
        <widget class="QLabel" name="label_2">
         <property name="text">
          <string>⩥ 200₽</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_16">
       <item>
        <widget class="QLabel" name="label_3">
         <property name="text">
          <string>⩥ 250₽</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_15">
       <item>
        <widget class="QLabel" name="label_4">
         <property name="text">
          <string>⩥ 120₽</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_14">
       <item>
        <widget class="QLabel" name="label_5">
         <property name="text">
          <string>⩥ 160₽</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_13">
       <item>
        <widget class="QLabel" name="label_6">
         <property name="text">
          <string>⩥ 70₽</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_12">
       <item>
        <widget class="QLabel" name="label_7">
         <property name="text">
          <string>⩥ 90₽</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>795</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


# Подключение к базе данных (создание, если не существует)
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Класс для меню
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Главное окно приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Меню Макдональдса")
        f = io.StringIO(template)
        uic.loadUi(f, self)

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
        self.initUI()

    def initUI(self):
        self.pushButton_22.clicked.connect(self.open_login)
        self.pushButton_24.clicked.connect(self.open_setting)

        # Меню
        buttons = [
            self.pushButton_30,
            self.pushButton_29,
            self.pushButton_8,
            self.pushButton_10,
            self.pushButton_12,
            self.pushButton_14,
            self.pushButton_16,
            self.pushButton_17,
            self.pushButton_18
        ]

        for button, item in zip(buttons, self.menu_items):
            button.clicked.connect(lambda checked, item=item: self.add_to_cart(item))

        # Кнопки корзины и истории заказов
        self.pushButton_23.clicked.connect(self.open_cart)
        self.pushButton_34.clicked.connect(self.open_order_history)
        self.pushButton_31.clicked.connect(self.open_open_open_open)


    def open_open_open_open(self):
        QMessageBox.information(self, "Нету", "Пока здесь ничего нет")

    def add_to_cart(self, item):
        self.cart.append(item)  # Добавляем товар в корзину
        QMessageBox.information(self, "Добавлено в корзину", f"{item.name} добавлено в корзину!")

    def open_login(self):
        self.close()
        self.login_window = Login()
        self.login_window.show()

    def open_cart(self):
        if not self.cart:
            QMessageBox.information(self, "Корзина пуста", "Ваша корзина пуста!")
            return
        self.cart_window = CartWindow(self.cart, self.order_history)
        self.cart_window.show()

    def open_setting(self):
        self.open_setting = Setting()
        self.open_setting.show()

    def open_order_history(self):
        if not self.order_history:
            QMessageBox.information(self, "История пуста", "У вас нет истории заказов!")
            return
        self.history_window = OrderHistoryWindow(self.order_history)
        self.history_window.show()


class Setting(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        btn_open_versions = QPushButton('Версии')
        btn_open_versions.clicked.connect(self.open_versions)
        layout.addWidget(btn_open_versions)

        btn_open_setting1 = QPushButton('Рестораны')
        btn_open_setting1.clicked.connect(self.open_restaurant)
        layout.addWidget(btn_open_setting1)

        open_license_window = QPushButton('Открыть лицензионное соглашение')
        open_license_window.clicked.connect(self.open_license)
        layout.addWidget(open_license_window)

        btn = QPushButton('Назад')
        btn.clicked.connect(self.open_men)
        layout.addWidget(btn)

        self.setLayout(layout)

    def open_license(self):
        self.close()
        self.license_window = LicenseWindow()
        self.license_window.show()

    def open_men(self):
        self.close()
        self.menu_window = MainWindow()

    def open_versions(self):
        self.close()
        self.oppen_versions = Versions()
        self.oppen_versions.show()

    def open_restaurant(self):
        self.close()
        self.restaurant_window = Restaurant()
        self.restaurant_window.show()


class Versions(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        btn_open_setting1 = QPushButton('Бета 0.1')
        btn_open_setting1.clicked.connect(self.open_beta_0_1)
        layout.addWidget(btn_open_setting1)

        btn_open_setting1 = QPushButton('Патч 0.1.1')
        btn_open_setting1.clicked.connect(self.open_patch_0_1_1)
        layout.addWidget(btn_open_setting1)

        btn_open_setting1 = QPushButton('Обновление 0.2.0')
        btn_open_setting1.clicked.connect(self.open_versions_0_2)
        layout.addWidget(btn_open_setting1)

        btn_open_setting = QPushButton('Что будет добавлено в релизе 1.0')
        btn_open_setting.clicked.connect(self.open_relis_1_0)
        layout.addWidget(btn_open_setting)

        btn = QPushButton('Вернуться в окно настроек')
        btn.clicked.connect(self.open_setting)
        layout.addWidget(btn)

        self.setLayout(layout)

    def open_beta_0_1(self):
        self.close()
        self.obnov_window1 = Beta()
        self.obnov_window1.show()

    def open_patch_0_1_1(self):
        self.close()
        self.obnov_window2 = Patch_0_1_1()
        self.obnov_window2.show()

    def open_versions_0_2(self):
        self.close()
        self.obnov_window3 = Versions_0_2_0()
        self.obnov_window3.show()

    def open_relis_1_0(self):
        self.close()
        self.obnov_window = Obnov()
        self.obnov_window.show()

    def open_setting(self):
        self.close()
        self.open_setting = Setting()
        self.open_setting.show()


class Beta(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Устанавливаем параметры окна
        self.setGeometry(450, 175, 400, 400)
        self.setWindowTitle('Бетта 0.1.0.')

        # Создаем кнопку "Назад"
        self.btn = QPushButton('Вернуться в окно версий', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 365)
        self.btn.clicked.connect(self.open_versions)

        # Создаем метку заголовка
        self.label = QLabel(self)
        self.label.setText("Перечень реализованных функций, появившихся в версии «Бетта» 0.1.0.")
        self.label.move(100, 15)

        # Создаем текстовую область для отображения изменений
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setPlainText(self.get_text_content1())
        self.text_area.setGeometry(15, 40, 370, 320)  # Положение и размер текстовой области

    def get_text_content1(self):
        return (
            "Проект представляет собой приложение для онлайн-заказа еды, которое позволяет пользователю просматривать меню, добавлять товары в корзину, оформлять заказы и сохранять историю заказов. Идея проекта заключается в создании удобного и интуитивно понятного интерфейса для пользователей, которые хотят заказать еду с помощью мобильного устройства или компьютера, при этом имея возможность использовать различные дополнительные функции, такие как промокоды, история заказов и настройки аккаунта.\n\n"

            "Описание реализации:\n\n"

            "Основной функционал приложения включает в себя несколько ключевых компонентов. Для реализации этого функционала использовались различные классы и функции, каждая из которых отвечает за определенный аспект работы программы.\n\n"

            "Классы и их роль:\n\n"

            "Класс Product:\n"
            "Этот класс представляет собой отдельное блюдо в меню. Он хранит информацию о названии блюда, его цене и описании. Класс имеет конструктор, который принимает данные о блюде, а также метод для получения информации о блюде. Это позволяет организовать меню и управлять данными о каждом товаре.\n"
            "class Product:\n"
            "    def __init__(self, name, price, description):\n"
            "        self.name = name\n"
            "        self.price = price\n"
            "        self.description = description\n\n"
            "    def get_info(self):\n"
            "        return f'{self.name}: {self.description}, Price: {self.price}'\n\n"

            "Класс Cart:\n"
            "Этот класс управляет корзиной покупок, куда пользователи могут добавлять продукты. Он хранит список товаров, выбранных пользователем, и предоставляет методы для добавления товаров в корзину, удаления товаров и расчета общей стоимости. Также здесь реализована возможность применения скидок, если промокод является действительным.\n"
            "class Cart:\n"
            "    def __init__(self):\n"
            "        self.items = []\n"
            "        self.total_price = 0\n\n"
            "    def add_item(self, product):\n"
            "        self.items.append(product)\n"
            "        self.total_price += product.price\n\n"
            "    def remove_item(self, product):\n"
            "        self.items.remove(product)\n"
            "        self.total_price -= product.price\n\n"

            "Класс Order:\n"
            "Этот класс отвечает за оформление заказа. Он включает информацию о заказанных продуктах, общей стоимости, а также о состоянии заказа (например, 'в процессе', 'доставлен' и т. д.). Класс сохраняет заказ в базе данных после его оформления, чтобы пользователи могли видеть историю своих заказов.\n"
            "class Order:\n"
            "    def __init__(self, cart, user):\n"
            "        self.cart = cart\n"
            "        self.user = user\n"
            "        self.status = 'in progress'\n"
            "        self.total = cart.total_price\n\n"
            "    def save_order(self):\n"
            "        # Логика для сохранения заказа в базе данных\n"
            "        pass\n\n"

            "Класс User:\n"
            "Класс User представляет собой учетную запись пользователя. Он хранит информацию о пользователе, такую как имя, адрес электронной почты, пароль и историю заказов. Этот класс включает методы для регистрации, авторизации и сохранения информации о пользователе в базе данных.\n"
            "class User:\n"
            "    def __init__(self, username, password):\n"
            "        self.username = username\n"
            "        self.password = password\n"
            "        self.orders_history = []\n\n"
            "    def register(self):\n"
            "        # Логика регистрации пользователя\n"
            "        pass\n\n"
            "    def login(self):\n"
            "        # Логика авторизации пользователя\n"
            "        pass\n\n"

            "Класс Database:\n"
            "Класс, управляющий базой данных, используется для хранения информации о пользователях, заказах и других данных, таких как продукты и промокоды. Он реализует основные операции, такие как добавление и извлечение данных.\n"
            "class Database:\n"
            "    def __init__(self):\n"
            "        self.users = []\n"
            "        self.orders = []\n\n"
            "    def add_user(self, user):\n"
            "        self.users.append(user)\n\n"
            "    def add_order(self, order):\n"
            "        self.orders.append(order)\n\n"

            "Взаимодействие классов и функции:\n\n"

            "-Основной поток:\n"
            "Когда пользователь выбирает продукты и добавляет их в корзину, происходит взаимодействие с классом Cart, который управляет всеми товарами в корзине. После того как пользователь завершает выбор, он может применить промокод (если он есть), используя класс PromoCode. После этого создается заказ с помощью класса Order, который сохраняется в базе данных для последующего использования.\n\n"

            "-История заказов:\n"
            "Каждый заказ сохраняется в базе данных с помощью класса Database. Пользователь может просматривать свою историю заказов, благодаря методу orders_history в классе User.\n\n"

            "-База данных:\n"
            "Для хранения данных о пользователях, заказах, блюдах и промокодах используется класс Database. Этот класс реализует операции добавления, извлечения и обновления данных в базе данных.\n\n"

            "Заключение:\n\n"
            "Проект представляет собой полноценное приложение для онлайн-заказа еды с широким набором функций, включая корзину, историю заказов, промокоды и настройки пользователя. Классы, такие как Product, Cart, Order, User, PromoCode и Database, взаимодействуют друг с другом, создавая удобный и функциональный интерфейс для пользователей.\n\n"

            "Возможности для доработки и развития включают расширение функционала, например, добавление новых способов оплаты, улучшение интерфейса с использованием изображений и анимаций, а также интеграцию с другими сервисами для улучшения пользовательского опыта. В дальнейшем можно реализовать поддержку многопользовательских учетных записей, добавление отзывов о блюдах и внедрение системы лояльности для постоянных клиентов.\n"
        )

    def open_versions(self):
        self.close()
        self.oppen_versions = Versions()
        self.oppen_versions.show()


class Patch_0_1_1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Устанавливаем параметры окна
        self.setGeometry(450, 175, 400, 400)
        self.setWindowTitle('Патч 0.1.1')

        # Создаем кнопку "Назад"
        self.btn = QPushButton('Вернуться в окно версий', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 365)
        self.btn.clicked.connect(self.open_versions)

        # Создаем метку заголовка
        self.label = QLabel(self)
        self.label.setText("Перечень реализованных функций, появившихся в версии Патча 0.1.1.")
        self.label.move(5, 15)

        # Создаем текстовую область для отображения изменений
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setPlainText(self.get_text_content1())
        self.text_area.setGeometry(15, 40, 370, 320)  # Положение и размер текстовой области

    def get_text_content1(self):
        return (
            "В патче 0.1.1 была восстановлена функция «промокодов», которая позволяет оплачивать заказ.\n"

            "Для оплаты заказа необходимо выполнить следующие действия:\n"

            "            1.Добавить в корзину товар,который вы хотите приобрести.\n"

            "            2.Нажать кнопку «Заказать».\n"

            "            3.В открывшемся окне ввести промокод «MACMENU» в поле для ввода карты и нажать кнопку «Подтвердить».\n"

            "После выполнения этих действий ваш заказ будет оплачен.\n"
        )

    def open_versions(self):
        self.close()
        self.oppen_versions = Versions()
        self.oppen_versions.show()


class Versions_0_2_0(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Устанавливаем параметры окна
        self.setGeometry(450, 175, 400, 400)
        self.setWindowTitle('Версия  0.2.0.')

        # Создаем кнопку "Назад"
        self.btn = QPushButton('Вернуться в окно версий', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 365)
        self.btn.clicked.connect(self.open_versions)

        # Создаем метку заголовка
        self.label = QLabel(self)
        self.label.setText("Перечень реализованных функций, появившихся в версии 0.2.0.")
        self.label.move(5, 15)

        # Создаем текстовую область для отображения изменений
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setPlainText(self.get_text_content1())
        self.text_area.setGeometry(15, 40, 370, 320)  # Положение и размер текстовой области

    def get_text_content1(self):
        return (
            "В версии 0.2.0. были реализовано:\n"

            "1. Список адресов сети ресторанов Вкусно и точка.\n"

            "2. Лицензия приложения.\n"

            "3. Изменился интерфейс окна настройки.\n"

            "4. Фоны в окне меню и окне регистрации.\n"

            "5. Окно со списком обновлений.\n"
        )

    def open_versions(self):
        self.close()
        self.oppen_versions = Versions()
        self.oppen_versions.show()


class LicenseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лицензионное соглашение")
        self.setGeometry(450, 175, 400, 300)

        layout = QVBoxLayout()

        # Чтение лицензионного соглашения из файла
        with open('license_agreement.txt', 'r', encoding='utf-8') as file:
            license_text = file.read()

        # Текстовое поле для отображения лицензионного соглашения
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(license_text)
        self.text_edit.setReadOnly(True)  # Делаем текстовое поле только для чтения

        layout.addWidget(self.text_edit)
        self.setLayout(layout)


class Restaurant(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Поиск ресторанов в Санкт-Петербурге")
        self.setGeometry(450, 175, 300, 550)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.btn = QPushButton('Назад')
        self.btn.clicked.connect(self.open_setting)
        self.layout.addWidget(self.btn)

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
        self.conn = sqlite3.connect("restaurant.db")
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

    def open_setting(self):
        self.close()
        self.open_setting = Setting()
        self.open_setting.show()


class Obnov(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Устанавливаем параметры окна
        self.setGeometry(450, 175, 400, 400)
        self.setWindowTitle('Обновление 2.0')

        # Создаем кнопку "Назад"
        self.btn = QPushButton('Назад', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(165, 365)
        self.btn.clicked.connect(self.open_versions)

        # Создаем метку заголовка
        self.label = QLabel(self)
        self.label.setText("Список изменений или добавлений в обновлении 2.0")
        self.label.move(100, 15)

        # Создаем текстовую область для отображения изменений
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setPlainText(self.get_text_content())
        self.text_area.setGeometry(15, 40, 370, 320)  # Положение и размер текстовой области

    def get_text_content(self):
        return (
            "Обновление 2.0:\n\n"
            "1. Добавить галочку оставаться в аккаунте при выходе.\n"
            "2. Добавить промокоды для привлечения новых клиентов и поощрения существующих.\n"
            "3. Нарисовать новую иконку.\n"
            "4. Добавить возможность делать промокоды на определенное количество раз.\n"
            "5. Добавить реальное время и во сколько был создан заказ.\n"
            "6. Историю заказов сделать базой данных, плюс добавить время заказа.\n"
            "7. Сделать заставку.\n"
            "8. Сделать более сложное создание паролей для повышения безопасности аккаунтов пользователей.\n"
            "9. Сделать поддержку для оперативного решения возникающих вопросов и проблем.\n"
            "10. Добавить пасхалки для создания уникального пользовательского опыта и повышения лояльности.\n"
            "11. Возможность банить аккаунты для предотвращения мошенничества.\n"
            "12. Кнопка выхода из аккаунта для быстрого выхода из приложения.\n"
            "13. Кнопка «Подробнее» для предоставления дополнительной информации о товарах или услугах.\n"
            "14. Картинки для улучшения визуального восприятия и привлечения внимания пользователей.\n"
            "15. Цифр для подтверждения карты увеличить до 16 для повышения безопасности при вводе данных карты.\n"
            "16. Реклама для генерации дохода и продвижения продуктов.\n"
            "17. Приветствие пользователя для создания дружелюбной атмосферы.\n"
            "18. Сохранение любимых заказов для удобства пользователей.\n"
            "19. Кнопка настройки и смену языка для адаптации приложения.\n"
            "20. Поддержка клавиатуры: таб — корзина, на цифры — добавление товаров.\n"
            "21. Розыгрыши еды для привлечения новых пользователей.\n"
            "22. Мини-игры для развлечения пользователей.\n"
            "23. Увеличить меню.\n"
            "24. Полная переработка интерфейса, добавление новых функций.\n"
            "\n"
            "Дополнительные функции:\n"
            "25. Уведомления о готовности заказа, чтобы пользователи знали, когда их заказ будет готов.\n"
            "26. Персонализированные предложения по питанию на основе предпочтений и здоровья.\n"
            "27. Оплата через счет внутри приложения для современных способов оплаты.\n"
            "28. Пополнять счет внутри приложения .\n"
            "29. Карта лояльности с накопительными баллами за каждое действие.\n"
            "30. Онлайн-меню на нескольких языках для удобства пользователей.\n"
            "31. История заказов с фотографиями для визуального подтверждения.\n"
            "32. Рекомендации по блюдам с учетом времени суток.\n"
            "33. Онлайн-обучение по приготовлению блюд с рецептом.\n"
            "34. Обратная связь по качеству обслуживания для улучшения услуг.\n"
            "35. Персонализированные рекомендации по напиткам.\n"
            "36. Интеграция с фитнес-трекерами для достижения целей.\n"
            "37. Уведомления о скидках на определенные дни недели.\n"

            # Добавьте более подробно все изменения или дополнения, которые хотите отобразить.
        )

    def open_versions(self):
        self.close()
        self.oppen_versions = Versions()
        self.oppen_versions.show()


# Окно для корзины
class CartWindow(QWidget):
    def __init__(self, cart, order_history):
        super().__init__()
        self.setWindowTitle("Корзина")
        self.cart = cart
        self.order_history = order_history
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
        self.order_dialog = OrderDialog(self.cart, self.order_history)
        self.order_dialog.show()
        self.close()


# Окно для ввода данных карты
class OrderDialog(QWidget):
    def __init__(self, cart, order_history):
        super().__init__()
        self.setWindowTitle("Введите данные карты")
        self.cart = cart
        self.order_history = order_history
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
        # Проверка валидности номера карты и возможности оплаты
        valid_promo_codes = ["DISCOUNT10", "FREESHIP", "WELCOME50", "NEWYEAR25", "пж100баллов", "NEWYEAR", "MACMENU",
                             "1"]
        card_number = self.card_number_input.text()
        if len(card_number) == 16 and card_number.isdigit() or card_number in valid_promo_codes:
            self.order_history.append(self.cart.copy())  # Добавляем заказ в историю
            self.cart.clear()  # Обнуляем корзину
            QMessageBox.information(self, "Заказ подтвержден", "Ваш заказ успешно оплачен!")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неправильный номер карты или промокод. Введите коректные данные.")


# Окно истории заказов
class OrderHistoryWindow(QWidget):
    def __init__(self, order_history):
        super().__init__()
        self.setWindowTitle("История заказов")
        self.order_history = order_history
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.history_table = QTableWidget()
        self.history_table.setRowCount(len(self.order_history))
        self.history_table.setColumnCount(2)
        self.history_table.setHorizontalHeaderLabels(["Заказ", "Статус"])

        for row, order in enumerate(self.order_history):
            order_names = ', '.join([item.name for item in order])
            self.history_table.setItem(row, 0, QTableWidgetItem(order_names))
            self.history_table.setItem(row, 1, QTableWidgetItem("Оплачен"))

        layout.addWidget(self.history_table)

        back_button = QPushButton("Назад в меню")
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

        self.setLayout(layout)


# Главное окно с функциями регистрации и входа
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход в аккаунт")
        self.layout = QVBoxLayout()

        self.pixmap = QPixmap('icons8-знак-чередования-эмоджи-48.jpg')
        self.image = QLabel(self)
        self.image.move(10, 0)
        self.image.resize(270, 140)
        self.image.setPixmap(self.pixmap)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Введите имя пользователя")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.register_button = QPushButton("Регистрация")
        self.register_button.clicked.connect(self.open_registration)
        self.layout.addWidget(self.register_button)

        self.setLayout(self.layout)

    def login(self):

        username = self.username_input.text()
        password = self.password_input.text()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute('SELECT name FROM users WHERE username=? AND password=?', (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            name = result[0]
            QMessageBox.information(self, "Обновление 1.2", "В патче 1.2 было добавлено:\n "
                                                            "1.Фоны в окне меню и окне регистрации\n"
                                                            "2.База данных с магазинами\n"
                                                            "3.Лицензиооное соглашение\n"
                                                            "4.Создан файл requirements.txt\n"
                                                            "5.Это окно\n")

            self.close()
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль.")

    def open_registration(self):
        self.close()
        self.registration_window = Registration(self)
        self.registration_window.show()


# Окно регистрации
class Registration(QWidget):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        self.setWindowTitle("Регистрация")
        self.layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Введите имя пользователя")
        self.layout.addWidget(self.username_input)

        self.pixmap = QPixmap('icons8-знак-чередования-эмоджи-48.jpg')
        self.image = QLabel(self)
        self.image.move(10, 0)
        self.image.resize(270, 140)
        self.image.setPixmap(self.pixmap)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_input)

        self.register_button = QPushButton("Зарегистрироваться")
        self.register_button.clicked.connect(self.register)
        self.layout.addWidget(self.register_button)

        self.register_button = QPushButton("Войти")
        self.register_button.clicked.connect(self.open_login)
        self.layout.addWidget(self.register_button)

        self.setLayout(self.layout)

    def open_login(self):
        self.close()
        self.login_window = Login()
        self.login_window.show()

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Имя пользователя и пароль обязательны!")
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                           (username, password))
            conn.commit()
            QMessageBox.information(self, "Успех", "Учетная запись успешно создана!")
            self.close()

            self.login_window.show()  # Открываем окно входа
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Ошибка", "Это имя пользователя уже занято.")
        finally:
            conn.close()


if __name__ == "__main__":
    init_db()  # Инициализация базы данных
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec())  # Запуск приложения
