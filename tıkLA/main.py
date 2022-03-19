from arayuz import Ui_MainWindow
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
import random




class Window(QMainWindow):

    basarili_Tiklama = 0
    DURATION_INT = 60

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #menü
        self.ui.buton_oyna.clicked.connect(self.oyna)
        self.ui.buton_ayarlar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.buton_emek.clicked.connect(self.emek)
        self.ui.buton_cikis.clicked.connect(self.close)
        ###
        self.ui.buton_emek_den_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        ###
        self.ui.buton_ayar_dan_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        ###
        self.ui.buton_tikla.clicked.connect(self.tikla)
        ###

    

        #oyun
    def nokta(self,bas,son):
        nokta = random.randint(bas,son)
        return nokta
    
    def isinla(self,x,y):
        #print(x,y) butonun koordinatları

        if x + 50 > 1280:
            x = 1230
        
        if y + 50 > 720:
            y = 670
        
        if x >= 0 and x<200 and y>= 0 and y<30:
            x = 200
            y = 30
        
        if x>=1080 and x<1280 and y>=0 and y<30:
            x=1030
            y=30
        #print(x,y) butonun yeni koordinatları. Ekran dışına çıkmaması veya "label" ların altında oluşmaması için ayarlamalar yapıldı.

        self.ui.buton_tikla.setGeometry(x,y,50,50)

    def tikla(self):
        self.basarili_Tiklama +=1
        self.ui.tiklanma_sayisi.setText("Tıklanma Sayısı : {}".format(self.basarili_Tiklama))
        x = self.nokta(0,1280)
        y = self.nokta(0,720)
        self.isinla(x,y)
        ###

        #zaman
    def timer_start(self):
        self.time_left_int = self.DURATION_INT
        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)
        self.update_gui()

    def timer_timeout(self):
        self.time_left_int -= 1
        if self.time_left_int == 0:
            self.ui.buton_tikla.setText('Oyun Bitti')
            self.ui.buton_tikla.setGeometry(540,310,200,50)
            self.ui.buton_tikla.clicked.connect(self.close)
            self.my_qtimer.stop()
        self.update_gui()

    def update_gui(self):
        self.ui.zaman_etiket.setText('Kalan Zaman : {}'.format(str(self.time_left_int)))

        ###
    def oyna(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.time_left_int = self.DURATION_INT
        self.timer_start()
        self.update_gui()

       #emek
    def emek(self):
        self.ui.stackedWidget.setCurrentIndex(3)
       ###

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())