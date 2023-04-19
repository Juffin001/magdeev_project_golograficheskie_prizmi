from PyQt5.QtWidgets import (QWidget, QInputDialog, QApplication)
class Prizma_Size(QWidget):

    def __init__(self):
        super().__init__()
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Размер призмы', 'Введите размер меньшей стороны призмы (см)')
        if ok:
            self.hey = int(text) * 37.936267 #из сантиметров в пиксели

