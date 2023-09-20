from PyQt5 import QtWidgets, QtCore
import requests

class KalkulackaMeny(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(KalkulackaMeny, self).__init__(**kwargs)

        self.setWindowTitle("PŘEVOD MĚNY")
        self.nastaveni_okna()
        self.show()

    def nastaveni_okna(self):
        # vytvoření okna a kontejnerů
        okno = QtWidgets.QWidget()
        okno_layout = QtWidgets.QVBoxLayout()
        box1_layout = QtWidgets.QHBoxLayout()
        box2_layout = QtWidgets.QHBoxLayout()
        box3_layout = QtWidgets.QHBoxLayout()

        self.setCentralWidget(okno)
        okno.setLayout(okno_layout)
        okno_layout.addLayout(box1_layout)
        okno_layout.addLayout(box2_layout)
        okno_layout.addLayout(box3_layout)

        # vytvoření obsahu widgetů
        self.cislo_edit = QtWidgets.QLineEdit(self)
        self.mena1_combobox = QtWidgets.QComboBox(self)
        self.text_label = QtWidgets.QLabel("-->")
        self.mena2_combobox = QtWidgets.QComboBox(self)
        self.vypocti_button = QtWidgets.QPushButton("PŘEVÉST",self)
        self.vysledek_label = QtWidgets.QLabel("", self)

        self.mena1_combobox.addItem("CZK")
        self.mena1_combobox.addItem("EUR")
        self.mena1_combobox.addItem("USD")
        self.mena2_combobox.addItem("EUR")
        self.mena2_combobox.addItem("USD")
        self.mena2_combobox.addItem("CZK")

        # úrava vzhledu
        self.setMinimumSize(350, 50)
        self.setStyleSheet("margin: 5 px; font-family: Calibri; font-size: 15px;")
        self.cislo_edit.setFixedWidth(150)
        self.vypocti_button.setFixedWidth(150)
        self.cislo_edit.setStyleSheet("padding: 7px")
        self.mena1_combobox.setStyleSheet("padding: 7px")
        self.text_label.setStyleSheet("padding: 7px")
        self.mena2_combobox.setStyleSheet("padding: 7px")
        self.vypocti_button.setStyleSheet("padding: 7px")
        self.vysledek_label.setStyleSheet("padding: 7px; border: 1px dotted black;")
        self.vysledek_label.setAlignment(QtCore.Qt.AlignHCenter)

        # rozmístění
        box1_layout.addStretch()
        box1_layout.addWidget(self.cislo_edit)
        box1_layout.addWidget(self.mena1_combobox)
        box1_layout.addWidget(self.text_label)
        box1_layout.addWidget(self.mena2_combobox)
        box1_layout.addStretch()
        box2_layout.addStretch()
        box2_layout.addWidget(self.vypocti_button)
        box2_layout.addStretch()
        box3_layout.addWidget(self.vysledek_label)

        # funkce tlačítek
        self.vypocti_button.clicked.connect(self.ziskani_prevodu)
        

    def ziskani_prevodu(self):
        castka = float(self.cislo_edit.text())
        z_meny = self.mena1_combobox.currentText()
        na_menu = self.mena2_combobox.currentText()

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={na_menu}&from={z_meny}&amount={castka}"

        payload = {}
        headers= {
        "apikey": "F1FECq6BpcL44GHVGahNIc4Pxg7Ac8dZ"
        }
        try:
            response = requests.request("GET", url, headers=headers, data = payload)
            result = response.json()
            castka_po = round(result["result"], 2)
            vysledek = f"{castka} {z_meny} = {castka_po} {na_menu}"
            self.vysledek_label.setText(vysledek)
        except:
            self.vysledek_label.setText("Došlo k chybě...")
