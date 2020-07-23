import json
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import QFile, QTextStream
from MainWindow import MainWindow
def getdata():
    with open('data.json','r') as jf:
        data = json.load(jf)

        for key, value in data.items():
            print(key,value)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
