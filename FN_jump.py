import os
import subprocess
import sys

from PySide6.QtCore import Qt
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
    try:
        FN_path = os.listdir(f"K:\\MFT\\1_Auftraege\\{arg1}\\{arg2}")  # Pfad wo die einzelnen Aufträge liegen

    except:
        subprocess.Popen(f"explorer K:\\MFT\\1_Auftraege\\{arg1}")
    arg3 = ""

    for i in FN_path:
        if i.startswith(arg3_fn):
            arg3 = i

    generated_path = f"K:\\MFT\\1_Auftraege\\{arg1}\\{arg2}\\{arg3}\\4_Elektrik_IBN"

    open_dir(generated_path, arg1)


def open_dir(FN_path, arg1):

    if os.path.exists(FN_path) == True:
        subprocess.Popen(f"explorer {FN_path}")

    else:
        subprocess.Popen(f"explorer K:\\MFT\\1_Auftraege\\{arg1}")


def showwindow():

    Screensize = getScreenSize()

    offset_taskbar = 75
    offset_side = 4
    x = Screensize[0] - window.width() - offset_side
    y = Screensize[1] - window.height() - offset_taskbar

    window.move(x, y)
    window.show()
    window.activateWindow()


def getScreenSize():

    return (QApplication.primaryScreen().size().width(), QApplication.primaryScreen().size().height())


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

    exit_app = menu.addAction("Exit")
    Systemtrayicon.setContextMenu(menu)
    exit_app.triggered.connect(exit_program)

    sys.exit(app.exec())
