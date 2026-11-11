from PyQt5.QtWidgets import *
import requests 

class AITChat(QWidget):
    def __init__(self):
        super().__init__()
        self.history = []
        self.setWindowTitle('AIT Chat')

        self.form = QFormLayout()
        self.button = QPushButton('Otprav')
        self.kto = QComboBox()
        self.komu = QLineEdit('')
        self.chto = QLineEdit('')
        self.chati = QTextEdit('')
        self.chati.setFixedSize(500, 500)

        self.form.addRow('Kto: ', self.kto)
        self.form.addRow('Komu: ', self.komu)
        self.form.addRow('Chto: ', self.chto)
        self.form.addRow('', self.button )
        self.form.addWidget(self.chati)

        self.findtext = QLineEdit('')
        self.form.addRow('Nayti: ', self.findtext)
        self.naydiknopka = QPushButton('Naydi')
        self.form.addWidget(self.naydiknopka)   
        self.naydiknopka.clicked.connect(self.naydif)


        self.clear = QPushButton('udali')
        self.clear.clicked.connect(self.udali)
        self.form.addWidget(self.clear)

        self.otslejka = QPushButton('otslejka VIP')
        self.otslejka.clicked.connect(self.otslejkaf)
        self.form.addWidget(self.otslejka)

        self.setLayout(self.form)
        self.button.clicked.connect(self.otprav)
        url = f'https://ait2026.pythonanywhere.com/kontakti'
        x = requests.get(url).text.split(',')
        for i in x:
            self.kto.addItem(i)
    
    def naydif(self):
        x = self.findtext.text()
        url = f'https://ait2026.pythonanywhere.com/tap?chto={x}'
        self.chati.setText(requests.get(url).text)
        self.history.append(f'hochet nayti {x}\npoluchil otvet:\n{self.chati.toPlainText()}\n')

    def otslejkaf(self):
        self.chati.setText('\n'.join(self.history))

    def udali(self):
        self.history.append(f'udalil text: \n{self.chati.toPlainText()}\n')
        self.chati.setText('')
    
    def otprav(self):
        kto = self.kto.text()
        komu = self.komu.text()
        chto = self.chto.text()
        url = f'https://ait2026.pythonanywhere.com/jonot?kto={kto}&komu={komu}&chto={chto}'
        x = requests.get(url)
        self.history.append(f'otpravil zapros: \n{url}\n')
        self.chati.setText(x.text.replace('<br>', '\n'))
        self.history.append(f'poluchil otvet: \n{x.text}\n')

if __name__ == "__main__":
    app = QApplication([])
    chat = AITChat()
    chat.show() 
    app.exec_()
