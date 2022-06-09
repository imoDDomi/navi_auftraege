import os
import subprocess
import sys
import tkinter as tk

from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtWidgets import QApplication, QDialog, QMenu, QSystemTrayIcon

from suche_aufträge import Ui_Hauptfenster


class InputWindow(QDialog, Ui_Hauptfenster):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.le_auftragsnummer.returnPressed.connect(generate_path)

    def closeEvent(self, evnt):
        evnt.ignore()
        window.hide()


def exit_program():
    sys.exit(app.exec())


def generate_path():
    window.hide()

    linecontent = window.le_auftragsnummer.displayText()

    arg1 = linecontent[0:2]  # 21

    arg2 = linecontent[2:4]  # 29

    arg3_fn = arg2 + linecontent[4:6]  # 2980

    path = os.listdir(f"C:\\MFT\\1_Auftraege\\{arg1}\\{arg2}")  # Pfad wo die einzelnen Aufträge liegen

    arg3 = ""
    for i in path:
        if i.startswith(arg3_fn):
            arg3 = i

    generated_path = f"C:\\MFT\\1_Auftraege\\{arg1}\\{arg2}\\{arg3}\\4_Elektrik_IBN"

    open_dir(generated_path)


def open_dir(path):

    subprocess.Popen(f"explorer {path}")


def showwindow():

    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 3000x800 -2183 x -1460  (817, 540 )

    x = screen_width - 2183
    y = screen_height - 1460

    window.move(x, y)
    window.show()
    window.activateWindow()


def main():
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Round)


if __name__ == "__main__":
    main()
    app = QApplication()

    window = InputWindow()

    tray_icon = QIcon()
    tray_icon.addFile("icons/lupe_white.png")
    Systemtrayicon = QSystemTrayIcon()
    Systemtrayicon.setIcon(tray_icon)
    Systemtrayicon.setToolTip("Suche Auftrag")
    Systemtrayicon.show()

    Systemtrayicon.activated.connect(showwindow)

    menu = QMenu()

    exit_app = menu.addAction("exit")
    Systemtrayicon.setContextMenu(menu)
    exit_app.triggered.connect(exit_program)

    sys.exit(app.exec())
