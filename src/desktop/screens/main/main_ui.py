# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMdiArea,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(837, 744)
        icon = QIcon()
        icon.addFile(u":/icons/resources/jr.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.act_banco_questor = QAction(MainWindow)
        self.act_banco_questor.setObjectName(u"act_banco_questor")
        self.act_comp_lanc_funrural = QAction(MainWindow)
        self.act_comp_lanc_funrural.setObjectName(u"act_comp_lanc_funrural")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mdi_area = QMdiArea(self.centralwidget)
        self.mdi_area.setObjectName(u"mdi_area")
        self.mdi_area.setStyleSheet(u"")
        brush = QBrush(QColor(159, 159, 159, 255))
        brush.setStyle(Qt.NoBrush)
        self.mdi_area.setBackground(brush)

        self.horizontalLayout.addWidget(self.mdi_area)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 837, 22))
        self.mnu_configuracoes = QMenu(self.menubar)
        self.mnu_configuracoes.setObjectName(u"mnu_configuracoes")
        self.menuImpostos = QMenu(self.menubar)
        self.menuImpostos.setObjectName(u"menuImpostos")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.mnu_configuracoes.menuAction())
        self.menubar.addAction(self.menuImpostos.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.mnu_configuracoes.addAction(self.act_banco_questor)
        self.menuImpostos.addAction(self.act_comp_lanc_funrural)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aplicativos Setor Fiscal", None))
        self.act_banco_questor.setText(QCoreApplication.translate("MainWindow", u"Banco Questor", None))
        self.act_comp_lanc_funrural.setText(QCoreApplication.translate("MainWindow", u"Comparar Lan\u00e7amentos Funrural", None))
        self.mnu_configuracoes.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.menuImpostos.setTitle(QCoreApplication.translate("MainWindow", u"Impostos", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
    # retranslateUi

