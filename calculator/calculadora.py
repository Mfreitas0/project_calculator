import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class   Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        
        self.display = QLineEdit()
        self.grid = QGridLayout(self.cw)
        self.grid.addWidget(self.display, 0, 0,1, 5)
        
        self.setCentralWidget(self.cw)
        
if __name__ == '__main__':
        qt = QApplication(sys.argv)
        calc = Calculadora()
        calc.show()
        qt.exec_()