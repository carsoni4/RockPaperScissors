from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

class RockPaperScissors(QMainWindow):
    def __init__(self):
        # QT Init
        super().__init__() 


        self.setWindowTitle("Rock Paper Scissors :)")
        self.setFixedSize(400, 400)
        
        #Scoring
        self.player_score = 0
        self.computer_score = 0

        self.title_label = QLabel("Rock Paper Scissors")


        layout = QVBoxLayout()
        layout.addWidget(self.title_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


        

