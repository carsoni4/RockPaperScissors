from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

class RockPaperScissors(QMainWindow):
    def __init__(self):
        #QT Init
        super().__init__() 


        self.setWindowTitle("Rock Paper Scissors :)")
        self.setFixedSize(400, 400)
        

