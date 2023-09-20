import requests
import sys
from PyQt5 import QtWidgets
from kalkulacka_prevod import KalkulackaMeny
from kalkulacka_clas import KalkulackaClasic

class HlavniOkno(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(HlavniOkno, self).__init__(**kwargs)

        self.setWindowTitle("SET KALKULAČEK")
        self.nastaveni_okna()
        self.datum_cas()
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
        self.datum_cas_label = QtWidgets.QLabel("", self)
        self.text_label = QtWidgets.QLabel("Vyberte požadovanou kalkulačku:", self)
        self.kalkulacka_klasic_button = QtWidgets.QPushButton("SČÍTÁNÍ A ODČÍTÁNÍ", self)
        self.kalkulacka_meny_button = QtWidgets.QPushButton("PŘEVOD MĚN", self)

        # rozmístění
        box1_layout.addStretch()
        box1_layout.addWidget(self.datum_cas_label)
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
        self.datum_cas_label.setStyleSheet("font-weight: bold; padding: 15px")

        # funkce
        self.kalkulacka_klasic_button.clicked.connect(self.open_kal_klasic)
        self.kalkulacka_meny_button.clicked.connect(self.open_kal_meny)


    def datum_cas(self):
        """
        Funkce zkusí pomocí API získat aktuální datum
        a teplotu v Praze. Lokalitu je možné měnit pouze
        v samotném kódu.

        Pokud se data nepodaří získat, zobrazí funkce
        chybovou hlášku.
        """
        try:
            # TEPLOTA
            api_key = "bd9bf362a1412b429ebdae8203164e73"
            mesto_weather = "Prague"
            url_weather = f"https://api.openweathermap.org/data/2.5/weather?q={mesto_weather}&appid={api_key}&units=metric"
            response_weather = requests.get(url_weather).json()
            teplota = round(response_weather["main"]["temp"], 1)

            # DEN
            mesto_cas = "Europe/Prague"
            url_time = f"http://worldtimeapi.org/api/timezone/Europe/Prague"
            response_time = requests.get(url_time).json()
            datum = response_time["datetime"]
            rok = datum[:4]
            mesic = datum[5:7]
            den = datum[8:10]

            self.datum_cas_label.setText(f"Vítejte! Dnes je {den}.{mesic}.{rok} a v Praze máme {teplota}°C.")
        except:
            self.datum_cas_label.setText("Data nelze načíst...")


    def open_kal_klasic(self):
        """
        Funkce otevře naimportovanou kalkulačku pro
        sčítání a odčítání.
        """
        kalkulacka_clasic = KalkulackaClasic()
        self.stacked_widget.addWidget(kalkulacka_clasic)
        self.stacked_widget.setCurrentWidget(kalkulacka_clasic)

    def open_kal_meny(self):
        """
        Funkce otevře naimportovanou kalkulačku pro
        převod měn.
        """
        kalkulacka_meny = KalkulackaMeny()
        self.stacked_widget.addWidget(kalkulacka_meny)
        self.stacked_widget.setCurrentWidget(kalkulacka_meny)


aplikace = QtWidgets.QApplication(sys.argv)
okno = HlavniOkno()
sys.exit(aplikace.exec_())