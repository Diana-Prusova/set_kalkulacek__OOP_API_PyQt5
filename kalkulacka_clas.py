from PyQt5 import QtWidgets, QtCore


class KalkulackaClasic(QtWidgets.QMainWindow):

    def __init__(self, **kwargs):
        super(KalkulackaClasic, self).__init__(**kwargs)

        self.setWindowTitle("Kalkulačka")
        self.init_gui()
        self.show()

    def init_gui(self):
        # vytvoření okna a kontejnerů
        formular = QtWidgets.QWidget()
        formular_layout = QtWidgets.QVBoxLayout()
        box_layout1 = QtWidgets.QHBoxLayout()
        box_layout2 = QtWidgets.QHBoxLayout()
        box_layout3 = QtWidgets.QHBoxLayout()

        self.setCentralWidget(formular)
        formular.setLayout(formular_layout)
        formular_layout.addLayout(box_layout1)
        formular_layout.addLayout(box_layout2)
        formular_layout.addLayout(box_layout3)

        # vytvoření obsahu widgetů
        self.cislo1_edit = QtWidgets.QLineEdit(self)
        self.cislo2_edit = QtWidgets.QLineEdit(self)
        self.vypocti_button = QtWidgets.QPushButton("SPOČÍTAT", self)
        self.roletka_combobox = QtWidgets.QComboBox(self)
        self.vysledek_label = QtWidgets.QLabel("0", self)

        self.roletka_combobox.addItem("+")
        self.roletka_combobox.addItem("-")
        self.roletka_combobox.addItem("*")
        self.roletka_combobox.addItem("/")

        # úrava vzhledu
        self.setMinimumSize(350, 50)
        self.setStyleSheet("margin: 5 px; font-family: Calibri; font-size: 15px;")
        self.cislo1_edit.setStyleSheet("padding: 7px")
        self.cislo2_edit.setStyleSheet("padding: 7px")
        self.vypocti_button.setStyleSheet("padding: 7px")
        self.roletka_combobox.setStyleSheet("padding: 7px")
        self.vysledek_label.setStyleSheet("padding: 7px; border: 1px dotted black;")
        self.vysledek_label.setAlignment(QtCore.Qt.AlignHCenter)

        # rozmístění
        box_layout1.addWidget(self.cislo1_edit)
        box_layout1.addWidget(self.roletka_combobox)
        box_layout1.addWidget(self.cislo2_edit)
        box_layout2.addWidget(self.vypocti_button)
        box_layout3.addWidget(self.vysledek_label)

        # funkce tlačítek
        self.vypocti_button.clicked.connect(self.vypocti)
        


    
    def vycisti(self):
        """
        Funkce po vypočtení příkladu vyčistí 
        zadávací pole.
        """
        self.cislo1_edit.setText("")
        self.cislo2_edit.setText("")

    def vypocti(self):
        """
        Funkce získá zadaná data a vypočítá 
        a zobrazí výsledek.
        """
        chyba = ""
        vysledek = 0

        try:
            cislo1 = float(self.cislo1_edit.text())
            cislo2 = float(self.cislo2_edit.text())
            operator = self.roletka_combobox.currentText()

            if operator == "+":
                vysledek = cislo1 + cislo2
                self.vycisti()
            elif operator == "-":
                vysledek = cislo1 - cislo2
                self.vycisti()
            elif operator == "*":
                vysledek = cislo1 * cislo2
                self.vycisti()
            elif operator == "/":
                if cislo2 == 0:
                    chyba = "CHYBA: nelze dělit nulou."
                else:
                    vysledek = cislo1 / cislo2
                    self.vycisti()
        except:
            chyba = "CHYBA: nebylo zadáno číslo."
            
        if len(chyba) > 1:
            self.vysledek_label.setText(chyba)
        else:
            self.vysledek_label.setText(str(round(vysledek, 3)))



   