from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter, ImageOps
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow

import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.workdir = None  
        self.filenames = None
        self.image = None

        self.ui.file.clicked.connect(self.choose_folder)
        self.ui.b_w.clicked.connect(self.bw_button)
        self.ui.left.clicked.connect(self.left_button)
        self.ui.right.clicked.connect(self.right_button)
        self.ui.mirror.clicked.connect(self.mirror_button)
        self.ui.sharpness.clicked.connect(self.blur_button)
        self.ui.listpictures.currentRowChanged.connect(self.show_choosen_image)

    def choose_folder(self):
        """вибір папки"""
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_list_image()
        except:
            error = QMessageBox()
            error.setText("Error")
            error.exec_()

    def show_list_image(self):
        """завантажуємо список картинок"""
        self.filenames = os.listdir(self.workdir)
        images = []
        for filename in self.filenames:
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                images.append(filename)
        self.ui.listpictures.clear()
        self.ui.listpictures.addItems(images)

    def load_image (self, imagename):
        """завантажуємо 1 картинку"""
        self.image_name = imagename
        self.image_path = os.path.join(self.workdir, self.image_name)
        self.image = Image.open(self.image_path)

    def show_picture(self):
        """відображуємо картинку"""
        self.ui.pictures.hide()
        h = self.ui.pictures.height()
        w = self.ui.pictures.width()
        
        pixmap_image = QPixmap(self.image_path)
        pixmap_image = pixmap_image.scaled(w, h, Qt.KeepAspectRatio)
        self.ui.pictures.setPixmap(pixmap_image)
        self.ui.pictures.show()

    def show_choosen_image(self):
        """показати вибране зображення """
        if  self.ui.listpictures.currentRow() >= 0:
            self.image_name = self.ui.listpictures.currentItem().text()
            self.load_image(self.image_name)
            self.show_picture()

    def save_image(self):
        path = os.path.join(self.workdir, "edited")
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        self.new_path = os.path.join(path, self.image_name)
        self.newimage.save(self.new_path)
        self.image_path = self.new_path


    def bw_button(self):
        self.newimage = self.image.convert('L')
        self.save_image()
        self.show_picture()       

    def left_button(self):
        self.newimage = self.image.rotate(90)
        self.save_image()
        self.show_picture() 

    def right_button(self):
        self.newimage = self.image.rotate(-90)
        self.save_image()
        self.show_picture() 

    def mirror_button(self):
        self.newimage = ImageOps.mirror(self.image)
        self.save_image()
        self.show_picture() 

    def blur_button(self):
        self.newimage = self.image.filter(ImageFilter.BoxBlur(4))
        self.save_image()
        self.show_picture() 


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()




# python -m PyQt5.uic.pyuic -x untitled.ui -o ui.py

# with Image.open('beer.jpg') as original:
#     pic_gray= original.convert("L")
#     pic_gray.save("black.jpg")
#     pic_gray.show() 