# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suche_aufträge.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLineEdit, QSizePolicy, QSpacerItem, QWidget)

class Ui_Hauptfenster(object):
    def setupUi(self, Hauptfenster):
        if not Hauptfenster.objectName():
            Hauptfenster.setObjectName(u"Hauptfenster")
        Hauptfenster.resize(182, 60)
        Hauptfenster.setMinimumSize(QSize(182, 60))
        Hauptfenster.setMaximumSize(QSize(182, 60))
        icon = QIcon()
        icon.addFile(u"icons/lupe_black.png", QSize(), QIcon.Normal, QIcon.Off)
        Hauptfenster.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Hauptfenster)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_auftragsnummer = QLineEdit(Hauptfenster)
        self.le_auftragsnummer.setObjectName(u"le_auftragsnummer")
        self.le_auftragsnummer.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.le_auftragsnummer, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Hauptfenster)

        QMetaObject.connectSlotsByName(Hauptfenster)
    # setupUi

    def retranslateUi(self, Hauptfenster):
        Hauptfenster.setWindowTitle(QCoreApplication.translate("Hauptfenster", u"Auftr\u00e4ge", None))
        self.le_auftragsnummer.setPlaceholderText(QCoreApplication.translate("Hauptfenster", u"Auftragsnummer", None))
    # retranslateUi

