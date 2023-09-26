import requests
import sys
from PyQt5 import QtWidgets
from kalkulacka_prevod import KalkulackaMeny
from kalkulacka_clas import KalkulackaClasic
from api_keys import api_key_teplota

class HlavniOkno(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(HlavniOkno, self).__init__(**kwargs)

        self.setWindowTitle("SET KALKULAČEK")
        self.nastaveni_okna()
        self.cas()
        self.teplota()
        self.show()

    def nastaveni_okna(self):
        # vytvoření okna a kontejnerů
        hlavni_okno = QtWidgets.QWidget()
        hlavni_okno_layout = QtWidgets.QVBoxLayout()
        box1_layout = QtWidgets.QHBoxLayout()
        box2_layout = QtWidgets.QHBoxLayout()
        box3_layout = QtWidgets.QHBoxLayout()
        box4_layout = QtWidgets.QHBoxLayout()

        self.setCentralWidget(hlavni_okno)
        hlavni_okno.setLayout(hlavni_okno_layout)
        hlavni_okno_layout.addLayout(box1_layout)
        hlavni_okno_layout.addLayout(box2_layout)
        hlavni_okno_layout.addLayout(box3_layout)
        hlavni_okno_layout.addLayout(box4_layout)

        # vytvoření obsahu okna
        self.datum_label = QtWidgets.QLabel("", self)
        self.teplota_label = QtWidgets.QLabel("", self)
        self.text_label = QtWidgets.QLabel("Vyberte požadovanou kalkulačku:", self)
        self.kalkulacka_klasic_button = QtWidgets.QPushButton("ZÁKLADNÍ ARIT. OPERACE", self)
        self.kalkulacka_meny_button = QtWidgets.QPushButton("PŘEVOD MĚN", self)

        # rozmístění
        box1_layout.addStretch()
        box1_layout.addWidget(self.datum_label)
        box1_layout.addWidget(self.teplota_label)
        box1_layout.addStretch()
        box2_layout.addStretch()
        box2_layout.addWidget(self.text_label)
        box2_layout.addStretch()
        box3_layout.addWidget(self.kalkulacka_klasic_button)
        box4_layout.addWidget(self.kalkulacka_meny_button)

        # úprava vzhledu
        self.setMinimumWidth(500)
        self.kalkulacka_klasic_button.setFixedWidth(300)
        self.kalkulacka_meny_button.setFixedWidth(300)
        self.setStyleSheet("font-family: Calibri; font-size: 15px;")
        self.kalkulacka_klasic_button.setStyleSheet("margin: 2.5px; padding: 7px")
        self.kalkulacka_meny_button.setStyleSheet("margin: 2.5px; padding: 7px")
        self.datum_label.setStyleSheet("font-weight: bold")
        self.teplota_label.setStyleSheet("font-weight: bold")
        self.text_label.setStyleSheet("padding-top: 15px")

        # funkce
        self.kalkulacka_klasic_button.clicked.connect(self.open_kal_klasic)
        self.kalkulacka_meny_button.clicked.connect(self.open_kal_meny)


    def cas(self):
        """
        Funkce zkusí pomocí API získat aktuální čas v Praze.
        Lokalitu je možné měnit pouzev samotném kódu.

        Pokud se data nepodaří získat, zobrazí funkce
        chybovou hlášku.
        """
        try:
            mesto_cas = "Europe/Prague"
            url_time = f"http://worldtimeapi.org/api/timezone/{mesto_cas}"
            response_time = requests.get(url_time).json()
            datum = response_time["datetime"]
            rok = datum[:4]
            mesic = datum[5:7]
            den = datum[8:10]

            self.datum_label.setText(f"Vítejte! Dnes je {den}.{mesic}.{rok}")
        except:
            self.datum_label.setText("Čas nelze načíst...")

    def teplota(self):
        """
        Funkce zkusí pomocí API získat aktuální teplotu v Praze.
        Lokalitu je možné měnit pouzev samotném kódu.

        Pokud se data nepodaří získat, zobrazí funkce
        chybovou hlášku.
        """
        try:
            api_key = api_key_teplota
            mesto_pocasi = "Prague"
            url_weather = f"https://api.openweathermap.org/data/2.5/weather?q={mesto_pocasi}&appid={api_key}&units=metric"
            response_weather = requests.get(url_weather).json()
            teplota = round(response_weather["main"]["temp"], 1)

            self.teplota_label.setText(f"a v Praze máme {teplota}°C.")
        except:
            self.teplota_label.setText("Teplotu nelze načíst...")

    def open_kal_klasic(self):
        """
        Funkce otevře naimportovanou kalkulačku pro
        sčítání a odčítání.
        """
        self.kalkulacka_clasic = KalkulackaClasic()
        self.kalkulacka_clasic.show()

    def open_kal_meny(self):
        """
        Funkce otevře naimportovanou kalkulačku pro
        převod měn.
        """
        self.kalkulacka_meny = KalkulackaMeny()
        self.kalkulacka_meny.show()


aplikace = QtWidgets.QApplication(sys.argv)
okno = HlavniOkno()
sys.exit(aplikace.exec_())