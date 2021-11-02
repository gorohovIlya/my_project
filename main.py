import sys
import maps.resource
import pictures_for_ark.resource1
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QWidget


class MyArkManual(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start_window.ui', self)
        self.theislandbtn.clicked.connect(self.open_theisland_window)
        self.scorchedbtn.clicked.connect(self.open_scorched_window)
        self.aberbtn.clicked.connect(self.open_aberration_window)
        self.ragnarokbtn.clicked.connect(self.open_ragnarok_window)
        self.extinctionbtn.clicked.connect(self.open_extinction_window)

    def open_theisland_window(self):
        self.hide()
        TheIsland(self)

    def open_scorched_window(self):
        self.hide()
        ScorchedEarth(self)

    def open_aberration_window(self):
        self.hide()
        Aberration(self)

    def open_ragnarok_window(self):
        self.hide()
        Ragnarok(self)

    def open_extinction_window(self):
        self.hide()
        Extinction(self)


class TheIsland(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        uic.loadUi('theisland.ui', self)
        self.return_back.clicked.connect(self.to_back)
        self.Swamp_Biome.clicked.connect(self.show_swamp_biome_window)
        self.show()

    def to_back(self):
        self.parent.show()
        self.close()

    def show_swamp_biome_window(self):
        SwampBiome(self)


class ScorchedEarth(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        uic.loadUi('scorchedearth.ui', self)
        self.return_back.clicked.connect(self.to_back)
        self.show()

    def to_back(self):
        self.parent.show()
        self.close()


class Aberration(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        uic.loadUi('aberration.ui', self)
        self.return_back.clicked.connect(self.to_back)
        self.show()

    def to_back(self):
        self.parent.show()
        self.close()


class Ragnarok(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        uic.loadUi('ragnarok.ui', self)
        self.return_back.clicked.connect(self.to_back)
        self.show()

    def to_back(self):
        self.parent.show()
        self.close()


class Extinction(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        uic.loadUi('extinction.ui', self)
        self.return_back.clicked.connect(self.to_back)
        self.show()

    def to_back(self):
        self.parent.show()
        self.close()


class SwampBiome(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        uic.loadUi('SwampBiomeInfo.ui', self)
        self.return_back.clicked.connect(self.to_back)
        # self.Meganeura.clicked.connect(self.show_dino_info)

        for self.btn in self.DinoGroup.buttons():
            self.btn.clicked.connect(self.show_dino_info)

        self.show()

    def show_dino_info(self):
        # if self.sender().text == 'Меганевра':
        Dino(self)

    def to_back(self):
        self.close()


class Dino(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        uic.loadUi('DinoInfo.ui', self)
        self.return_back.clicked.connect(self.to_back)
        self.show()

    def to_back(self):
        self.close()

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


