import os

import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLineEdit,QLabel,QListWidget

import mysql.connector

os.system('cls')


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sanjarbek2006',
    database = 'yuqlama'
)

mycursor = mydb.cursor()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600, 730)

        self.btn_shoh = QPushButton(self)
        self.btn_shoh.setText('Присутствовал')

        self.btn_fotima  = QPushButton(self) 
        self.btn_fotima.setText('Присутствовал')

        self.btn_uzim = QPushButton(self)
        self.btn_uzim.setText('Присутствовал')

        self.btn_nurmuhammad = QPushButton(self)
        self.btn_nurmuhammad.setText('Присутствовал')

        self.btn_jahongir = QPushButton(self)
        self.btn_jahongir.setText('Присутствовал')

        self.btn_tolibjon = QPushButton(self)
        self.btn_tolibjon.setText('Присутствовал')

        self.btn_lobar = QPushButton(self)
        self.btn_lobar.setText('Присутствовал')

        self.btn_muhammadaziz = QPushButton(self)
        self.btn_muhammadaziz.setText('Присутствовал')
        

        self.btn_dilshod = QPushButton(self)
        self.btn_dilshod.setText('Присутствовал')

        self.btn_farhodbek = QPushButton(self)
        self.btn_farhodbek.setText('Присутствовал')

        self.btn_farangiz = QPushButton(self)
        self.btn_farangiz.setText('Присутствовал')

        self.btn_jonibek = QPushButton(self)
        self.btn_jonibek.setText('Присутствовал')

        self.btn_bekzod = QPushButton(self)
        self.btn_bekzod.setText('Присутствовал')

        self.btn_azizbek = QPushButton(self)
        self.btn_azizbek.setText('Присутствовал')

        self.btn_bekbulsin = QPushButton(self)
        self.btn_bekbulsin.setText('Присутствовал')

        self.btn_sevinch = QPushButton(self)    
        self.btn_sevinch.setText('Присутствовал') 


        self.uquvchila = QLabel('Ученики',self)
        self.uquvchila.move(250, 10)
        self.uquvchila.setStyleSheet(
            'color: #BF3EFF;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.save = QPushButton('Сохранить',self)
        self.save.move(460, 680)
        self.save.setStyleSheet(
            'color: #00C957;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.otmen = QPushButton('Отменить',self)
        self.otmen.move(350, 680)
        self.otmen.setStyleSheet(
            'color: #FF3030;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.shoh = QLabel('Abdusattorov Shohrux',self)
        self.shoh.move(30, 30)
        self.btn_shoh.move(450,30)
        self.btn_shoh.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.shoh.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.fotima = QLabel('Aliboyeva Fotima',self)
        self.fotima.move(30, 70)
        self.btn_fotima.move(450,70)
        self.btn_fotima.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.fotima.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.sanjarbek = QLabel('Berdiqulov Sanjarbek',self)
        self.sanjarbek.move(30, 110)
        self.btn_uzim.move(450,110)
        self.btn_uzim.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.sanjarbek.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.nurmuhammad = QLabel('Davletov Nurmuhammad',self)
        self.nurmuhammad.move(30, 150)
        self.btn_nurmuhammad.move(450,150)
        self.btn_nurmuhammad.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.nurmuhammad.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.jahongir = QLabel('Fayzullayev Jahongir',self)
        self.jahongir.move(30, 190)
        self.btn_jahongir.move(450,190)
        self.btn_jahongir.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.jahongir.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.tolibjon = QLabel('Fayzullayev Tolibjon',self)
        self.tolibjon.move(30, 230)
        self.btn_tolibjon.move(450,230)
        self.btn_tolibjon.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.tolibjon.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.lobar = QLabel("G'oziyeva Lobar",self)
        self.lobar.move(30, 270)
        self.btn_lobar.move(450,270)
        self.btn_lobar.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.lobar.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.muhammadaziz = QLabel('Komiljonov Muhammadaziz',self)
        self.muhammadaziz.move(30, 310)
        self.btn_muhammadaziz.move(450,310)
        self.btn_muhammadaziz.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.muhammadaziz.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.dilshod = QLabel('Komiljonov Dilshod',self)
        self.dilshod.move(30, 350)
        self.btn_dilshod.move(450,350)
        self.btn_dilshod.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.dilshod.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.farhodbek = QLabel('Madrahimov Farhodbek',self)
        self.farhodbek.move(30, 390)
        self.btn_farhodbek.move(450,390)
        self.btn_farhodbek.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.farhodbek.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.farangiz = QLabel('Nasriddinova Farangizxon',self)
        self.farangiz.move(30, 430)
        self.btn_farangiz.move(450,430)
        self.btn_farangiz.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.farangiz.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.jonibek = QLabel('Olimov Jonibek',self)
        self.jonibek.move(30, 470)
        self.btn_jonibek.move(450,470)
        self.btn_jonibek.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.jonibek.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.bekzod = QLabel('Poyonov Bekzod',self)
        self.bekzod.move(30, 510)
        self.btn_bekzod.move(450,510)
        self.btn_bekzod.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.bekzod.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.azizbek = QLabel('Rahmatullayev Azizbek',self)
        self.azizbek.move(30, 550)
        self.btn_azizbek.move(450,550)
        self.btn_azizbek.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.azizbek.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.bekbulsin = QLabel("Rajabboyev Bekbo'lsin",self)
        self.bekbulsin.move(30, 590)
        self.btn_bekbulsin.move(450,590)
        self.btn_bekbulsin.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.bekbulsin.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.sevinch = QLabel('Xayriddinova Sevinch',self)
        self.sevinch.move(30, 630)
        self.btn_sevinch.move(450,630)
        self.btn_sevinch.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.sevinch.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'   
        )

        self.show()

        self.c_1 = 0
        self.c_2 = 0
        self.c_3 = 0
        self.c_4 = 0
        self.c_5 = 0
        self.c_6 = 0
        self.c_7 = 0
        self.c_8 = 0
        self.c_9 = 0
        self.c_10 = 0
        self.c_11 = 0
        self.c_12 = 0
        self.c_13 = 0
        self.c_14 = 0
        self.c_15 = 0
        self.c_16 = 0

        self.btn_shoh.clicked.connect(self.press_btn_shoh)
        self.btn_fotima.clicked.connect(self.press_btn_fotima)
        self.btn_uzim.clicked.connect(self.press_btn_sanjarbek)
        self.btn_nurmuhammad.clicked.connect(self.press_btn_nurmuhammad)
        self.btn_jahongir.clicked.connect(self.press_btn_jahongir)
        self.btn_tolibjon.clicked.connect(self.press_btn_tolibjon)
        self.btn_lobar.clicked.connect(self.press_btn_lobar)
        self.btn_muhammadaziz.clicked.connect(self.press_btn_muhammadaziz)
        self.btn_dilshod.clicked.connect(self.press_btn_dilshod)
        self.btn_farhodbek.clicked.connect(self.press_btn_fathodbek)
        self.btn_farangiz.clicked.connect(self.press_btn_farangiz)
        self.btn_jonibek.clicked.connect(self.press_btn_jonibek)
        self.btn_bekzod.clicked.connect(self.press_btn_bekzod)
        self.btn_azizbek.clicked.connect(self.press_btn_azizbek)
        self.btn_bekbulsin.clicked.connect(self.press_btn_bekbulsin)
        self.btn_sevinch.clicked.connect(self.press_btn_sevinch)
        self.otmen.clicked.connect(self.press_btn_close)
        self.save.clicked.connect(self.press_btn_save)


    def press_btn_shoh(self):
        if self.c_1 % 2 == 0:
            self.btn_shoh.setText('Отсутствовал')
            self.btn_shoh.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_shoh.setText('Присутствовал')
            self.btn_shoh.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_1 +=1

    def press_btn_fotima(self):
        if self.c_2 % 2 == 0:
            self.btn_fotima.setText('Отсутствовал')
            self.btn_fotima.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_fotima.setText('Присутствовал')
            self.btn_fotima.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_2 +=1
    
    def press_btn_sanjarbek(self):
        if self.c_3 % 2 == 0:
            self.btn_uzim.setText('Отсутствовал')
            self.btn_uzim.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_uzim.setText('Присутствовал')
            self.btn_uzim.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_3 +=1
    
    def press_btn_nurmuhammad(self):
        if self.c_4 % 2 == 0:
            self.btn_nurmuhammad.setText('Отсутствовал')
            self.btn_nurmuhammad.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_nurmuhammad.setText('Присутствовал')
            self.btn_nurmuhammad.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_4 +=1
    
    def press_btn_jahongir(self):
        if self.c_5 % 2 == 0:
            self.btn_jahongir.setText('Отсутствовал')
            self.btn_jahongir.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_jahongir.setText('Присутствовал')
            self.btn_jahongir.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_5 +=1

    def press_btn_tolibjon(self):
        if self.c_6 % 2 == 0:
            self.btn_tolibjon.setText('Отсутствовал')
            self.btn_tolibjon.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_tolibjon.setText('Присутствовал')
            self.btn_tolibjon.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_6 +=1

    def press_btn_lobar(self):
        if self.c_7 % 2 == 0:
            self.btn_lobar.setText('Отсутствовал')
            self.btn_lobar.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_lobar.setText('Присутствовал')
            self.btn_lobar.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_7 +=1
    
    def press_btn_muhammadaziz(self):
        if self.c_8 % 2 == 0:
            self.btn_muhammadaziz.setText('Отсутствовал')
            self.btn_muhammadaziz.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_muhammadaziz.setText('Присутствовал')
            self.btn_muhammadaziz.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_8 +=1
    
    def press_btn_dilshod(self):
        if self.c_9 % 2 == 0:
            self.btn_dilshod.setText('Отсутствовал')
            self.btn_dilshod.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_dilshod.setText('Присутствовал')
            self.btn_dilshod.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_9 +=1

    def press_btn_fathodbek(self):
        if self.c_10 % 2 == 0:
            self.btn_farhodbek.setText('Отсутствовал')
            self.btn_farhodbek.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_farhodbek.setText('Присутствовал')
            self.btn_farhodbek.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_10 +=1
    
    def press_btn_farangiz(self):
        if self.c_11 % 2 == 0:
            self.btn_farangiz.setText('Отсутствовал')
            self.btn_farangiz.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_farangiz.setText('Присутствовал')
            self.btn_farangiz.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_11 +=1

    def press_btn_jonibek(self):
        if self.c_12 % 2 == 0:
            self.btn_jonibek.setText('Отсутствовал')
            self.btn_jonibek.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_jonibek.setText('Присутствовал')
            self.btn_jonibek.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_12 +=1
    
    def press_btn_bekzod(self):
        if self.c_13 % 2 == 0:
            self.btn_bekzod.setText('Отсутствовал')
            self.btn_bekzod.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_bekzod.setText('Присутствовал')
            self.btn_bekzod.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_13 +=1
    
    def press_btn_azizbek(self):
        try:
            if self.c_14 % 2 == 0:
                self.btn_azizbek.setText('Отсутствовал')
                self.btn_azizbek.setStyleSheet(
                'color: red;'
                'font-size: 15px;'
                'font-weight: bold;'   
            )
            else:
                self.btn_azizbek.setText('Присутствовал')
                self.btn_azizbek.setStyleSheet(
                'color: black;'
                'font-size: 15px;'
                'font-weight: bold;'
            )
            self.c_14 +=1
        except Exception as err:
            print(err)
        else:
            print('norm')
    
    def press_btn_bekbulsin(self):
        if self.c_15 % 2 == 0:
            self.btn_bekbulsin.setText('Отсутствовал')
            self.btn_bekbulsin.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'
        )
        else:
            self.btn_bekbulsin.setText('Присутствовал')
            self.btn_bekbulsin.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_15 +=1
    
    def press_btn_sevinch(self):
        if self.c_16 % 2 == 0:
            self.btn_sevinch.setText('Отсутствовал')
            self.btn_sevinch.setStyleSheet(
            'color: red;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        else:
            self.btn_sevinch.setText('Присутствовал')
            self.btn_sevinch.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.c_16 +=1
    
    def press_btn_close(self):
        self.c_1 = 0
        self.c_2 = 0
        self.c_3 = 0
        self.c_4 = 0
        self.c_5 = 0
        self.c_6 = 0
        self.c_7 = 0
        self.c_8 = 0
        self.c_9 = 0
        self.c_10 = 0
        self.c_11 = 0
        self.c_12 = 0
        self.c_13 = 0
        self.c_14 = 0
        self.c_15 = 0
        self.c_16 = 0
        self.btn_shoh.setText('Присутствовал')
        self.btn_fotima.setText('Присутствовал')
        self.btn_uzim.setText('Присутствовал')
        self.btn_nurmuhammad.setText('Присутствовал')
        self.btn_jahongir.setText('Присутствовал')
        self.btn_tolibjon.setText('Присутствовал')
        self.btn_lobar.setText('Присутствовал')
        self.btn_muhammadaziz.setText('Присутствовал')
        self.btn_dilshod.setText('Присутствовал')
        self.btn_farhodbek.setText('Присутствовал')
        self.btn_farangiz.setText('Присутствовал')
        self.btn_jonibek.setText('Присутствовал')
        self.btn_bekzod.setText('Присутствовал')
        self.btn_azizbek.setText('Присутствовал')
        self.btn_bekbulsin.setText('Присутствовал')
        self.btn_sevinch.setText('Присутствовал')
        
        self.btn_shoh.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.btn_fotima.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.btn_uzim.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.btn_nurmuhammad.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.btn_jahongir.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.btn_tolibjon.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
        self.btn_lobar.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_muhammadaziz.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_dilshod.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_farhodbek.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_farangiz.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_jonibek.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_bekzod.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_azizbek.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_bekbulsin.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_sevinch.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

    def press_btn_save(self):
        self.close()
        self.Spage = SecondPage()
        self.Spage.show()

        if self.c_1 % 2 == 0:
            full_name = ['Abdusattorov Shohrux']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Abdusattorov Shohrux']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()


        if self.c_2 % 2 == 0:
            full_name = ['Aliboyeva Fotima']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Aliboyeva Fotima']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()

    
        if self.c_3 % 2 == 0:
            full_name = ['Berdiqulov Sanjarbek']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Berdiqulov Sanjarbek']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_4 % 2 == 0:
            full_name = ['Davletov Nurmuhammad']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Davletov Nurmuhammad']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_5 % 2 == 0:
            full_name = ['Fayzullayev Jahongir']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Fayzullayev Jahongir']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_6 % 2 == 0:
            full_name = ['Fayzullayev Tolibjon']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Fayzullayev Tolibjon']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_7 % 2 == 0:
            full_name = ["G'oziyeva Lobar"]
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ["G'oziyeva Lobar"]
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_8 % 2 == 0:
            full_name = ['Komiljonov Muhammadaziz']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            name = ['Komiljonov Muhammadaziz']
            sql = "INSERT INTO kelmaganlar (full_name) values (%s)"
            val = (name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_9 % 2 == 0:
            full_name =[ 'Komiljonov Dilshod']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = [ 'Komiljonov Dilshod']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_10 % 2 == 0:
            full_name =[ 'Madrahimov Farhodbek']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name =[ 'Madrahimov Farhodbek']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()

        if self.c_11 % 2 == 0:
                full_name = ['Nasriddinova Farangizxon']
                sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
                val = (full_name)
                mycursor.execute(sql,val)
                mydb.commit()
        else:
            try:
                full_name =  ["Nasriddinova Farangizxon"]
                sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
                val = (full_name)
                mycursor.execute(sql,val)
                mydb.commit()
            except Exception as err:
                print(err)
        
        if self.c_12 % 2 == 0:
            full_name = ['Olimov Jonibek']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Olimov Jonibek']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_13 % 2 == 0:
            full_name = ['Payonov Bekzod']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Payonov Bekzod']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_14 % 2 == 0:
            full_name = ['Rahmatullayev Azizbek']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Rahmatullayev Azizbek']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        if self.c_15 % 2 == 0:
            full_name = ['Rajabbayev Bekbo\'lsin']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ["Rajabbayev Bekbolsin"]
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        
        
        if self.c_16 % 2 == 0:
            full_name = ['Xayriddinova Sevinch']
            sql = "INSERT INTO kelganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            full_name = ['Xayriddinova Sevinch']
            sql = "INSERT INTO kelmaganlar (FULL_NAME) VALUES (%s)"
            val = (full_name)
            mycursor.execute(sql,val)
            mydb.commit()
    

class SecondPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 600)

        self.btn_kelganlar = QPushButton(self)
        self.btn_kelganlar.setText('IN CLASS')

        self.btn_kelmaganlar = QPushButton(self)
        self.btn_kelmaganlar.setText('NOT IN CLASS')

        self.exit = QPushButton(self)
        self.exit.setText('EXIT')

        self.initIU1()

        self.initIU2()

        self.initIU3()

        self.exit.clicked.connect(self.press_btn_exit)

        self.btn_kelganlar.clicked.connect(self.press_btn_kelganlar)

        self.btn_kelmaganlar.clicked.connect(self.press_btn_kelmaganlar)


    def initIU1(self):
        self.btn_kelganlar.setStyleSheet(
            'background-color: #EEAEEE; '
            'font: 30px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_kelganlar.setFixedSize(300,80)
        self.btn_kelganlar.move(110,100)

    def initIU2(self):
        self.btn_kelmaganlar.setStyleSheet(
            'background-color: #EEAEEE; '
            'font: 30px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_kelmaganlar.setFixedSize(300,80)
        self.btn_kelmaganlar.move(110,200)
    
    def initIU3(self):
        self.exit.setStyleSheet(
            'background-color: #EEAEEE; '
            'font: 30px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.exit.setFixedSize(300,80)
        self.exit.move(110,300)
    

    def press_btn_exit(self):
        try:
            with mydb.cursor() as cursor:
                sql = f"""
                delete from kelganlar where full_name = full_name;        
                """
                cursor.execute(sql)
                result = cursor.fetchall()
                mydb.commit()

                sql = f"""
                delete from kelmaganlar where full_name = full_name;        
                """
                cursor.execute(sql)
                result = cursor.fetchall()
                mydb.commit()
        except Exception as err:
            print(err)
    
        self.close()    

    
    def press_btn_kelganlar(self):
        self.kelgan_third = Third_page_kelganlar()
        self.close()
        self.kelgan_third.show()
    
    def press_btn_kelmaganlar(self):
        self.kelmagan_third = Third_page_kelmaganlar()
        self.close()
        self.kelmagan_third.show()


class Third_page_kelganlar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600, 730)

        self.btn_exit = QPushButton(self)
        self.btn_exit.setText('BACK')
        self.btn_exit.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )

        self.v_box = QVBoxLayout()
        
        self.qlw = QListWidget()

        self.v_box.addWidget(self.qlw)
        self.v_box.addWidget(self.btn_exit)

        self.setLayout(self.v_box)

        self.show_data()

        self.btn_exit.clicked.connect(self.press_exit)

    def show_data(self):
        try:
            with mydb.cursor() as cursor:
                sql = f"""
                select * from kelganlar           
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    self.i = self
                    self.i.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
                    self.i = str(i)
                    self.qlw.addItem(str(self.i[2:-3]))
        except Exception as err:
            print(err)
    
    def press_exit(self):
        self.two = SecondPage()
        self.close()
        self.two.show()





class Third_page_kelmaganlar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600, 730)

        self.v_box = QVBoxLayout()
        
        self.qlw = QListWidget()

        self.btn_exit = QPushButton(self)
        self.btn_exit.setText('BACK')

        self.setLayout(self.v_box)

        self.show_data()

        self.v_box.addWidget(self.qlw)
        self.v_box.addWidget(self.btn_exit)

        self.btn_exit.clicked.connect(self.press_exit)

        self.btn_exit.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )

    def show_data(self):
        try:
            with mydb.cursor() as cursor:
                sql = f"""
                select * from kelmaganlar           
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    self.i = self
                    self.i.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
                    self.i = str(i)
                    self.qlw.addItem(str(self.i[2:-3]))
        except Exception as err:
            print(err)
        
    def press_exit(self):
        self.two = SecondPage()
        self.close()
        self.two.show()
        
app = QApplication(sys.argv)

win = MainWindow()

sys.exit(app.exec_())
