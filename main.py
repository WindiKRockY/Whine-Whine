from PIL import Image,ImageFilter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from ui import Ui_MainWindow

import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.ui.file.clicked.connect(self.choose_folder)
        self.fikenames = None
        self.image = None
        
    def show_image_list(self):
        self.filenames = os.listdir(self.workdir)
        images = []
        for filename in self.filenames:
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                images.append(filename)
        self.ui.listfile_win.clear()
        self.ui.listfile_win.addItems(images)


    def choose_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.filenames = os.listdir(self.workdir)
            self.show_image_list()
        except:
            message= QMessageBox()
            message.setText("Eror404")
            message.exec_()
    #def show_picutre()

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()



#with Image.open("stay.jpg") as original:
# pic_gray = original.convert("L")
# pic_gray.save("bw_pic.jpg")
# pic_blured = original.filter(ImageFilter.BLUR)
# pic_up = original.transpose(Image.ROTATE_90) 
# pic_gray.show()
    