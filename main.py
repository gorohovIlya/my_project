import sys
import sqlite3
import maps.resource
import pictures_for_ark.resource1
import pictures_for_ark.mapiconresource
from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from functools import partial

connection = sqlite3.connect('dinos_db.db')
cursor = connection.cursor()


class MyArkManual(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.theislandbtn.clicked.connect(self.open_map_window)
        # self.scorchedearthbtn.clicked.connect(self.open_map_window)
        # self.aberrationbtn.clicked.connect(self.open_map_window)
        # self.ragnarokbtn.clicked.connect(self.open_map_window)
        # self.extinctionbtn.clicked.connect(self.open_map_window)
        self.show()

    def hello_world(self):
        print('Hello world!')

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
            # self.theislandbtn.clicked.connect(self.open_map_window)
            # self.scorchedearthbtn.clicked.connect(self.open_map_window)
            # self.aberrationbtn.clicked.connect(self.open_map_window)
            # self.ragnarokbtn.clicked.connect(self.open_map_window)
            # self.extinctionbtn.clicked.connect(self.open_map_window)
            self.MapButtons.addLayout(frame)
            # print(btn.objectName())
            # print(btn.text())

    def open_map_window(self, btn_text):
        self.hide()
        # print(btn)
        # print(btn_text)
        Map(current_map=btn_text, parent=self)

        # if btn.objectName == 'theislandbtn':
        #     Map(self)
        #     print(btn.objectName())
        # elif btn.objectName == 'scorchedearthbtn':
        #     Map(self)
        #     print(btn.objectName())
        # elif btn.objectName == 'aberrationbtn':
        #     Map(self)
        #     print(btn.objectName())
        # elif btn.objectName == 'extinctionbtn':
        #     Map(self)
        #     print(btn.objectName())
        # elif btn.objectName == 'ragnarokbtn':
        #     Map(self)
        #     print(btn.objectName())


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
        # if self.btn.objectName == 'theislandbtn':
        #     print(self.btn.objectName)
        #     print(self.current_map)
            imgs = cursor.execute(f"""SELECT * FROM Map_regions WHERE map_name = '{self.current_map}'""").fetchall()
            # print(imgs)
            pixmap = QPixmap()
            for el in imgs:
                pixmap.loadFromData(el[2], "png")
                pixmap_resized = pixmap.scaled(751, 751, QtCore.Qt.KeepAspectRatio)
                self.label.setPixmap(pixmap_resized)
                regions = (el[0].split('\n'))
                for i in regions:
                    region_btn = QPushButton(i, self)
                    if region_btn.text() == 'Западное побережье':
                        region_btn.setGeometry(50, 380, 160, 25)
                    elif region_btn.text() == 'Остров Крэгга':
                        region_btn.setGeometry(90, 630, 160, 25)
                    elif region_btn.text() == 'Секвойный лес':
                        region_btn.setGeometry(250, 450, 160, 25)
                    elif region_btn.text() == 'Извилистые болота':
                        region_btn.setGeometry(320, 490, 160, 25)
                    elif region_btn.text() == 'Южные острова':
                        region_btn.setGeometry(360, 570, 160, 25)
                    elif region_btn.text() == 'Северные регионы':
                        region_btn.setGeometry(50, 90, 160, 25)
                    elif region_btn.text() == 'Мертвый остров':
                        region_btn.setGeometry(560, 90, 160, 25)
                    elif region_btn.text() == 'Восточное побережье':
                        region_btn.setGeometry(560, 380, 160, 25)
                    elif region_btn.text() == 'Южная гавань':
                        region_btn.setGeometry(560, 600, 160, 25)
                    elif region_btn.text() == 'Горы':
                        region_btn.setGeometry(90, 350, 160, 25)
                    elif region_btn.text() == 'Дюны':
                        region_btn.setGeometry(500, 130, 160, 25)
                    elif region_btn.text() == 'Оазис 1':
                        region_btn.setGeometry(180, 90, 160, 25)
                    elif region_btn.text() == 'Оазис 2':
                        region_btn.setGeometry(200, 540, 160, 25)
                    elif region_btn.text() == 'Оазис 3':
                        region_btn.setGeometry(500, 370, 160, 25)
                    elif region_btn.text() == 'Нижняя пустыня':
                        region_btn.setGeometry(500, 480, 160, 25)
                    elif region_btn.text() == 'Траншея драконов':
                        region_btn.setGeometry(50, 410, 160, 25)
                    elif region_btn.text() == 'Каньоны':
                        region_btn.setGeometry(350, 450, 160, 25)
                    elif region_btn.text() == 'Верхняя пустыня':
                        region_btn.setGeometry(270, 370, 160, 25)
                    elif region_btn.text() == 'Бесплодные земли':
                        region_btn.setGeometry(520, 400, 160, 25)
                print([i for i in el[0].split('\n')])
        except Exception as e:
            print(e)

    # def setImgsValue(self):
    #     self.imgs = cursor.execute("""SELECT Map_img FROM Map_regions""").fetchall()
    #     print(self.imgs)
        # elif self.btn.objectName == 'scorchedearthbtn':
        # rqst = cursor.execute("""SELECT Map_img FROM Map_regions WHERE map_name = 'Scorched Earth'""").fetchall()
        # pixmap = QPixmap()
        # pixmap.loadFromData(rqst[0][0], "png")
        #     pixmap_resized = pixmap.scaled(751, 751, QtCore.Qt.KeepAspectRatio)
        #     self.label.setPixmap(pixmap_resized)
        # # elif self.btn.objectName == 'aberrationbtn':
        #     rqst = cursor.execute("""SELECT Map_img FROM Map_regions WHERE map_name = 'Aberration'""").fetchall()
        #     pixmap = QPixmap()
        #     pixmap.loadFromData(rqst[0][0], "png")
        #     pixmap_resized = pixmap.scaled(751, 751, QtCore.Qt.KeepAspectRatio)
        #     self.label.setPixmap(pixmap_resized)
        # # elif self.btn.objectName == 'extinctionbtn':
        #     rqst = cursor.execute("""SELECT Map_img FROM Map_regions WHERE map_name = 'Extinction'""").fetchall()
        #     pixmap = QPixmap()
        #     pixmap.loadFromData(rqst[0][0], "png")
        #     pixmap_resized = pixmap.scaled(751, 751, QtCore.Qt.KeepAspectRatio)
        #     self.label.setPixmap(pixmap_resized)
        # # elif self.btn.objectName == 'ragnarokbtn':
        #     rqst = cursor.execute("""SELECT Map_img FROM Map_regions WHERE map_name = 'Ragnarok'""").fetchall()
        #     pixmap = QPixmap()
        #     pixmap.loadFromData(rqst[0][0], "png")
        #     pixmap_resized = pixmap.scaled(751, 751, QtCore.Qt.KeepAspectRatio)
        #     self.label.setPixmap(pixmap_resized)
        # # print(rqst)



#     def open_theisland_window(self):
#         self.hide()
#         TheIsland(self)
#
#     def open_scorched_window(self):
#         self.hide()
#         ScorchedEarth(self)
#
#     def open_aberration_window(self):
#         self.hide()
#         Aberration(self)
#
#     def open_ragnarok_window(self):
#         self.hide()
#         Ragnarok(self)
#
#     def open_extinction_window(self):
#         self.hide()
#         Extinction(self)
#
#
# class TheIsland(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.parent = parent
#         uic.loadUi('theisland.ui', self)
#         self.return_back.clicked.connect(self.to_back)
#         self.Swamp_Biome.clicked.connect(self.show_swamp_biome_window)
#         self.show()
#
#     def to_back(self):
#         self.parent.show()
#         self.close()
#
#     def show_swamp_biome_window(self):
#         SwampBiome(self)
#
#
# class ScorchedEarth(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.parent = parent
#         uic.loadUi('scorchedearth.ui', self)
#         self.return_back.clicked.connect(self.to_back)
#         self.show()
#
#     def to_back(self):
#         self.parent.show()
#         self.close()
#
#
# class Aberration(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.parent = parent
#         uic.loadUi('aberration.ui', self)
#         self.return_back.clicked.connect(self.to_back)
#         self.show()
#
#     def to_back(self):
#         self.parent.show()
#         self.close()
#
#
# class Ragnarok(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.parent = parent
#         uic.loadUi('ragnarok.ui', self)
#         self.return_back.clicked.connect(self.to_back)
#         self.show()
#
#     def to_back(self):
#         self.parent.show()
#         self.close()
#
#
# class Extinction(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.parent = parent
#         uic.loadUi('extinction.ui', self)
#         self.return_back.clicked.connect(self.to_back)
#         self.show()
#
#     def to_back(self):
#         self.parent.show()
#         self.close()
#
#
# class SwampBiome(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.parent = parent
#         uic.loadUi('SwampBiomeInfo.ui', self)
#         self.return_back.clicked.connect(self.to_back)
#         # self.Meganeura.clicked.connect(self.show_dino_info)
#
#         for self.btn in self.DinoGroup.buttons():
#             self.btn.clicked.connect(self.show_dino_info)
#
#         self.show()
#
#     def show_dino_info(self):
#         # if self.sender().text == 'Меганевра':
#         Dino(self)
#
#     def to_back(self):
#         self.close()
#
#
# class Dino(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.parent = parent
#         uic.loadUi('DinoInfo.ui', self)
#         self.return_back.clicked.connect(self.to_back)
#         self.show()
#
#     def to_back(self):
#         self.close()

# class AberrantDino(Dino):
#     def __init__(self,  name, temperament, basic_stats, radiation_damage):
#         super().__init__(self, name, temperament,)
#         self.radiation_damage = radiation_damage
    # super().get_name()
    # super().get_temperament()
    # super().get_basic_stats()

#     def get_radiation_damage(self):
#         return self.radiation_damage
#
#
# class Tameable(Dino):
#     def __init__(self, name, temperament, basic_stats, istameable, food_for_taming, food_type, harvesting_resources
#                  , rideable, mateable, saddle_required, saddle_info):
#         super().__init__(name, temperament, basic_stats)
#         self.istameable = istameable
#         self.food_for_taming = food_for_taming
#         self.food_type = food_type
#         self.harvesting_resources = harvesting_resources
#         self.rideable = rideable
#         self.mateable = mateable
#         self.saddle_required = saddle_required
#         self.saddle_info = saddle_info
#
#     def get_istameable(self):
#         return self.istameable
#
#     def get_food_for_taming(self):
#         return self.food_for_taming
#
#     def get_food_type(self):
#         return self.food_type
#
#     def get_harvesting_resources(self):
#         return self.harvesting_resources
#
#     def get_rideable(self):
#         return self.rideable
#
#     def get_mateable(self):
#         return self.mateable
#
#     def get_saddle_required(self):
#         if self.saddle_required:
#             return self.saddle_required
#         else:
#             return None
#
#     def get_saddle_info(self):
#         if self.saddle_info:
#             return self.saddle_info
#         else:
#             return None
#
#
# class Untameable(Dino):
#     def __init__(self, istameable, name, temperament, basic_stats):
#         super().__init__(name, temperament, basic_stats)
#         self.istameable = istameable
#     # super().get_name()
#     # super().get_temperament()
#     # super().get_basic_stats()
#
#     def get_istameable(self):
#         return self.istameable


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.except_hook = except_hook
    app = QApplication(sys.argv)
    ex = MyArkManual()
    ex.show()
    sys.exit(app.exec())


