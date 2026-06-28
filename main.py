import sys
from PyQt6.QtWidgets import QApplication
from rps.gui import RockPaperScissors

def main():
    gui = QApplication(sys.argv)
    window = RockPaperScissors()
    window.show()

    sys.exit(gui.exec())

if __name__ == "__main__":
    main()