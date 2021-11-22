import sys

from PIL import Image, ImageDraw
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.initUI()

    def initUI(self):
        self.drawPushButton.clicked.connect(self.do_magic)
        self.cleanPushButton.clicked.connect(self.clear)

        self.clear()
        

    def clear(self):
        img = Image.open('main_image.png')
        dr = ImageDraw.Draw(img)
        dr.rectangle(((0, 0), img.size), (200, 200, 200))
        img.save('main_image.png')
        img.close()

        self.image = QPixmap('main_image.png')
        self.label.setPixmap(self.image) 
        

    def do_magic(self):
        x0 = randrange(100, 500)
        y0 = randrange(100, 500)
        r = randrange(10, 100)
        par = ((x0 - r, y0 - r), (x0 + r, y0 + r))

        color = (255, 204, 0)
        
        par = ((x0 - r, y0 - r), (x0 + r, y0 + r))
        
        img = Image.open('main_image.png')
        dr = ImageDraw.Draw(img)
        dr.ellipse(par, color, (70, 0, 0))
        img.save('main_image.png')
        img.close()

        self.image = QPixmap('main_image.png')
        self.label.setPixmap(self.image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
    ex.connection.close()
        
