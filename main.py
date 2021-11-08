import sys
import sqlite3
from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QTableWidgetItem, QLabel
from PyQt5.QtGui import QPixmap

connection = sqlite3.connect('dinos_db.db')
cursor = connection.cursor()


class MyArkManual(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        cursor = connection.cursor()
        rqst = cursor.execute('SELECT * FROM Maps').fetchall()
        uic.loadUi('test.ui', self)
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

    def open_map_window(self, btn_text):
        self.hide()
        Map(current_map=btn_text, parent=self)


class Map(QMainWindow):
    def __init__(self, current_map, parent=None):
        super().__init__(parent)
        self.current_map = current_map
        self.parent = parent
        self.initUI()
        self.show()

    def initUI(self):
        try:
            uic.loadUi('test_map.ui', self)
            imgs = cursor.execute(f"""SELECT * FROM Map_regions WHERE map_name = '{self.current_map}'""").fetchall()
            pixmap = QPixmap()
            for el in imgs:
                pixmap.loadFromData(el[2], "png")
                pixmap_resized = pixmap.scaled(751, 751, QtCore.Qt.KeepAspectRatio)
                self.label.setPixmap(pixmap_resized)
                regions = el[0].split('\n')
                print(regions)
                locations = el[3]
                locations = locations.split('\n')
                locations_improved = [elem.split(', ') for elem in locations]
                print(locations_improved)
                l2 = [list(map(int, x)) for x in locations_improved]
                print(l2)
                for i in range(len(regions)):
                    region_btn = QPushButton(regions[i], self)
                    region_btn.setGeometry(l2[i][0], l2[i][1], l2[i][2], l2[i][3])
                    region_btn.clicked.connect(lambda: self.open_region_window(self.sender().text()))  # открываем окно региона, название которого соответствует тексту кнопки
        except Exception as e:
            print(e)

    def open_region_window(self, reg_btn_text):
        sender = self.sender()
        print(sender.text())
        print(reg_btn_text)
        Region(current_region=reg_btn_text, parent=self)


class Region(QMainWindow):  # окно региона
    def __init__(self, current_region, parent=None):
        super().__init__(parent)
        self.current_region = current_region
        self.parent = parent
        self.initUI()
        self.show()

    def initUI(self):
        try:
            animal_frames = []
            uic.loadUi('region.ui', self)
            creatures = cursor.execute(f"""SELECT creatures FROM RegionsDinos WHERE region_name = '{self.current_region}'""").fetchall()  # выбираем из таблицы в базе данных нужные значения
            print(creatures)
            animals = creatures[0][0].split(', ')
            print(animals)

            for dino in range(len(animals)):
                icon = cursor.execute(f"""SELECT dino_icon FROM Creatures_info WHERE Name = '{animals[dino]}'""").fetchall()

                pixmap = QPixmap()
                pixmap.loadFromData(icon[0][0], "png")

                pixmap_resized = pixmap.scaled(120, 120, QtCore.Qt.KeepAspectRatio)
                dino_btn = QPushButton(animals[dino], self)
                label = QLabel()
                label.setPixmap(pixmap_resized)
                frame = QVBoxLayout()
                frame.addWidget(label, alignment=Qt.AlignCenter)
                frame.addWidget(dino_btn)
                animal_frames.append(frame)
            for x in range(1):
                for y in range(2):
                    self.gridLayout.addLayout(animal_frames[y], x, y)

        except Exception as e:
            print(e)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.except_hook = except_hook
    app = QApplication(sys.argv)
    ex = MyArkManual()
    ex.show()
    sys.exit(app.exec())


