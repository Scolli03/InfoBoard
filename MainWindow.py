from PyQt5.QtWidgets import QApplication, QFormLayout, QMainWindow, QScrollArea, QVBoxLayout, QWidget
from PyQt5.QtCore import QFile, QTextStream
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.setCentralWidget(MainWindow)
        self.setObjectName('centralwidget')        
        self.setWindowTitle("My Feed")
        self.setGeometry(1620, 40, 300, 985)
        file = QFile("dark.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)      

        self.mainLayout = QVBoxLayout(self.centralWidget)
        self.mainLayout.setObjectName('mainLayout')


        
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
