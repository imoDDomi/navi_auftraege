import subprocess
import sys
from re import sub

import keyboard
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase, QGuiApplication
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMainWindow

from suche_aufträge import Ui_Hauptfenster


class InputWindow(QDialog, Ui_Hauptfenster):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.le_auftragsnummer.returnPressed.connect(generate_path)


path = "C:\\MFT\\1_Auftraege\\21\\29\\2980_Heller_Daimler_Untertuerkheim_mFL5\\4_Elektrik_IBN"


def generate_path():
    window.close()

    linecontent = window.le_auftragsnummer.displayText()

    arg1 = linecontent[0:2]
    print(arg1)
    arg2 = linecontent[2:4]
    print(arg2)
    arg3 = linecontent[4:6]
    print(arg3)

    # arg2 = 80
    # arg3 = arg1 + arg2 + "Projektname"

    # generated_path = f"C:\\MFT\\1_Auftraege\\{arg1}\\{arg2}\\{arg3}\\4_Elektrik_IBN"

    # open_dir(generated_path)


def open_dir(path):

    print("test 2")
    subprocess.Popen(f"explorer {path}")


def main():
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Round)


if __name__ == "__main__":
    main()
    app = QApplication()
    window = InputWindow()
    window.show()
    sys.exit(app.exec())
