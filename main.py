import DinoInfo
import region
import search_results
import test
import test_map
import sys
import sqlite3
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

connection = sqlite3.connect('dinos_db.db')
cursor = connection.cursor()

FLAGS = [['агрессивный', 'нейтральный', 'послушный'],
         ['хищник', 'падальщик', 'травоядный'],
         ['ездовое', 'неездовое'],
         ]


class MyArkManual(QMainWindow, test.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.exit.clicked.connect(self.exit_from_app)
        self.search_btn.clicked.connect(lambda: self.open_searcher_window(self.lineEdit.text()))

    def initUI(self):
        try:
            rqst = cursor.execute('SELECT * FROM Maps').fetchall()
            # uic.loadUi('test.ui', self)
            self.setupUi(self)
            for el in rqst:
                pixmap = QPixmap()
                pixmap.loadFromData(el[2], "png")
                pixmap_resized = pixmap.scaled(120, 120, QtCore.Qt.KeepAspectRatio)
                btn = QPushButton(el[1], self)
                btn.setObjectName(el[3])
                label = QLabel()
                label.setPixmap(pixmap_resized)
                frame = QVBoxLayout()
                frame.addWidget(label, alignment=Qt.AlignCenter)
                frame.addWidget(btn)
                if btn.text() == 'The Island':
                    btn.clicked.connect(lambda: self.open_map_window('The Island'))
                elif btn.text() == 'Scorched Earth':
                    btn.clicked.connect(lambda: self.open_map_window('Scorched Earth'))
                elif btn.text() == 'Aberration':
                    btn.clicked.connect(lambda: self.open_map_window('Aberration'))
                elif btn.text() == 'Extinction':
                    btn.clicked.connect(lambda: self.open_map_window('Extinction'))
                elif btn.text() == 'Ragnarok':
                    btn.clicked.connect(lambda: self.open_map_window('Ragnarok'))
                self.MapButtons.addLayout(frame)
        except Exception as e:
            print(e)

    def open_map_window(self, btn_text):
        self.hide()
        Map(current_map=btn_text, parent=self)

    def exit_from_app(self):
        self.close()

    def open_searcher_window(self, user_input):
        self.hide()
        DinoSearch(edittext=user_input, parent=self)


class DinoSearch(QMainWindow, search_results.Ui_MainWindow):
    def __init__(self, edittext, parent=None):
        super().__init__(parent)
        self.edittext = edittext
        self.parent = parent
        self.initUI()
        self.show()
        self.return_back.clicked.connect(self.previousWindow)

    def initUI(self):
        try:
            self.setupUi(self)
            rquest = 0
            animal_frames = []
            self.setupUi(self)
            pixmap = QPixmap()
            if self.edittext in FLAGS[0]:
                rquest = cursor.\
                    execute(f"""SELECT * FROM Creatures_info WHERE Temperament = '{self.edittext.lower()}'""").\
                    fetchall()
            elif self.edittext in FLAGS[1]:
                rquest = cursor\
                    .execute(f"""SELECT * FROM Creatures_info WHERE food_type = '{self.edittext.lower()}'""").fetchall()
            elif self.edittext.lower() in FLAGS[2][0]:
                rquest = cursor.execute(f"""SELECT * FROM Creatures_info WHERE rideable = 'Да'""").fetchall()
            elif self.edittext.lower() in FLAGS[2][1]:
                rquest = cursor.execute(f"""SELECT * FROM Creatures_info WHERE rideable = 'Нет'""").fetchall()
            elif self.edittext.lower() not in FLAGS[0] and self.edittext.lower() not in FLAGS[1] and\
                    self.edittext.lower() not in FLAGS[2] and len(self.edittext.lower()) > 0:
                rquest = cursor.execute(f"""SELECT * FROM Creatures_info WHERE Name = '{self.edittext}'""").fetchall()
            for el in rquest:
                pixmap.loadFromData(el[15], "png")
                pixmap_resized = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
                dino_btn = QPushButton(el[1], self)
                dino_btn.clicked.connect(lambda: self.open_dino_window(self.sender().text()))
                label = QLabel()
                label.setPixmap(pixmap_resized)
                frame = QVBoxLayout()
                frame.addWidget(label, alignment=Qt.AlignCenter)
                frame.addWidget(dino_btn)
                animal_frames.append(frame)
            for x in range(1):
                for y in range(3):
                    self.gridLayout.addLayout(animal_frames[y], x, y)
        except Exception as e:
            print(e)

    def open_dino_window(self, dino_btn_text):
        Dino(current_dino=dino_btn_text, parent=self)

    def previousWindow(self):
        self.close()
        self.parent.show()


class Map(QMainWindow, test_map.Ui_MainWindow):
    def __init__(self, current_map, parent=None):
        super().__init__(parent)
        self.current_map = current_map
        self.parent = parent
        self.initUI()
        self.show()
        self.return_back.clicked.connect(self.previousWindow)

    def initUI(self):
        try:
            self.setupUi(self)
            imgs = cursor.execute(f"""SELECT * FROM Map_regions WHERE map_name = '{self.current_map}'""").fetchall()
            pixmap = QPixmap()
            for el in imgs:
                pixmap.loadFromData(el[2], "png")
                pixmap_resized = pixmap.scaled(751, 751, QtCore.Qt.KeepAspectRatio)
                self.label.setPixmap(pixmap_resized)
                regions = el[0].split('\n')
                locations = el[3]
                locations = locations.split('\n')
                locations_improved = [elem.split(', ') for elem in locations]
                l2 = [list(map(int, x)) for x in locations_improved]
                for i in range(len(regions)):
                    region_btn = QPushButton(regions[i], self)
                    region_btn.setGeometry(l2[i][0], l2[i][1], l2[i][2], l2[i][3])
                    region_btn.clicked.connect(lambda: self.open_region_window(self.sender().text()))  # открываем окно
                    # региона, название которого соответствует тексту кнопки
        except Exception as e:
            print(e)

    def open_region_window(self, reg_btn_text):
        Region(current_region=reg_btn_text, parent=self)

    def previousWindow(self):
        self.close()
        self.parent.show()


class Region(QMainWindow, region.Ui_MainWindow):  # окно региона
    def __init__(self, current_region, parent=None):
        super().__init__(parent)
        self.current_region = current_region
        self.parent = parent
        self.initUI()
        self.show()
        self.return_back.clicked.connect(self.previousWindow)

    def initUI(self):
        try:
            animal_frames = []
            self.setupUi(self)
            creatures = cursor.\
                execute(f"""SELECT creatures FROM RegionsDinos WHERE region_name = '{self.current_region}'""").\
                fetchall()  # выбираем из таблицы в базе данных нужные значения
            animals = creatures[0][0].split(', ')
            pixmap = QPixmap()
            for dino in range(len(animals)):
                icon = cursor.execute(f"""SELECT dino_icon FROM Creatures_info WHERE Name = '{animals[dino]}'""").\
                    fetchall()
                pixmap.loadFromData(icon[0][0], "png")
                pixmap_resized = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
                dino_btn = QPushButton(animals[dino], self)
                dino_btn.clicked.connect(lambda: self.open_dino_window(self.sender().text()))
                label = QLabel()
                label.setPixmap(pixmap_resized)
                frame = QVBoxLayout()
                frame.addWidget(label, alignment=Qt.AlignCenter)
                frame.addWidget(dino_btn)
                animal_frames.append(frame)
            for x in range(3):
                for y in range(6):
                    self.gridLayout.addLayout(animal_frames[y], x, y)
            self.title.setText(self.current_region)
        except Exception as e:
            print(e)

    def previousWindow(self):
        self.close()
        self.parent.show()

    def open_dino_window(self, dino_btn_text):
        Dino(current_dino=dino_btn_text, parent=self)


class Dino(QMainWindow, DinoInfo.Ui_MainWindow):
    def __init__(self, current_dino, parent=None):
        super().__init__(parent)
        self.current_dino = current_dino
        self.parent = parent
        self.initUI()
        self.show()
        self.return_back.clicked.connect(self.previousWindow)

    def initUI(self):
        try:
            self.setupUi(self)
            request = cursor.execute(f"""SELECT * FROM Creatures_info WHERE Name = '{self.current_dino}'""").fetchall()
            pixmap = QPixmap()
            pixmap1 = QPixmap()
            for el in request:
                pixmap.loadFromData(el[13], "png")
                pixmap_resized = pixmap.scaled(329, 232, QtCore.Qt.KeepAspectRatio)
                pixmap1.loadFromData(el[14], "png")
                pixmap_resized1 = pixmap1.scaled(329, 232, QtCore.Qt.KeepAspectRatio)
                self.picture_1.setPixmap(pixmap_resized)
                self.picture_2.setPixmap(pixmap_resized1)
                self.title.setText(el[1])
                self.tameable.setText(el[4])
                self.temperament.setText(el[2])
                self.food_type.setText(el[6])
                self.rideable.setText(el[8])
                self.mateable.setText(el[9])
                self.saddle_required.setText(el[10])
                self.food_value.setText(el[5])
                self.harvests_value.setText(el[7])
                self.saddle_recipe_value.setText(el[11])
                self.basic_stats_value.setText(el[3])
        except Exception as e:
            print(e)

    def previousWindow(self):
        self.close()
        self.parent.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.except_hook = except_hook
    app = QApplication(sys.argv)
    ex = MyArkManual()
    ex.show()
    sys.exit(app.exec())
