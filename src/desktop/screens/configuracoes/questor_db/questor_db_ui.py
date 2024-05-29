# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'questor_db.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_QuestorDB(object):
    def setupUi(self, QuestorDB):
        if not QuestorDB.objectName():
            QuestorDB.setObjectName('QuestorDB')
        QuestorDB.resize(430, 139)
        QuestorDB.setMinimumSize(QSize(430, 139))
        QuestorDB.setMaximumSize(QSize(430, 139))
        self.verticalLayout = QVBoxLayout(QuestorDB)
        self.verticalLayout.setObjectName('verticalLayout')
        self.grd_form = QGridLayout()
        self.grd_form.setObjectName('grd_form')
        self.lbl_porta = QLabel(QuestorDB)
        self.lbl_porta.setObjectName('lbl_porta')

        self.grd_form.addWidget(self.lbl_porta, 3, 2, 1, 1)

        self.txt_banco = QLineEdit(QuestorDB)
        self.txt_banco.setObjectName('txt_banco')

        self.grd_form.addWidget(self.txt_banco, 0, 1, 1, 3)

        self.txt_host = QLineEdit(QuestorDB)
        self.txt_host.setObjectName('txt_host')

        self.grd_form.addWidget(self.txt_host, 3, 1, 1, 1)

        self.txt_senha = QLineEdit(QuestorDB)
        self.txt_senha.setObjectName('txt_senha')
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.grd_form.addWidget(self.txt_senha, 1, 3, 1, 1)

        self.lbl_usuario = QLabel(QuestorDB)
        self.lbl_usuario.setObjectName('lbl_usuario')

        self.grd_form.addWidget(self.lbl_usuario, 1, 0, 1, 1)

        self.txt_porta = QSpinBox(QuestorDB)
        self.txt_porta.setObjectName('txt_porta')
        self.txt_porta.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.txt_porta.setMaximum(99999)

        self.grd_form.addWidget(self.txt_porta, 3, 3, 1, 1)

        self.txt_usuario = QLineEdit(QuestorDB)
        self.txt_usuario.setObjectName('txt_usuario')

        self.grd_form.addWidget(self.txt_usuario, 1, 1, 1, 1)

        self.lbl_banco = QLabel(QuestorDB)
        self.lbl_banco.setObjectName('lbl_banco')

        self.grd_form.addWidget(self.lbl_banco, 0, 0, 1, 1)

        self.lbl_senha = QLabel(QuestorDB)
        self.lbl_senha.setObjectName('lbl_senha')

        self.grd_form.addWidget(self.lbl_senha, 1, 2, 1, 1)

        self.lbl_host = QLabel(QuestorDB)
        self.lbl_host.setObjectName('lbl_host')

        self.grd_form.addWidget(self.lbl_host, 3, 0, 1, 1)

        self.btn_salvar = QPushButton(QuestorDB)
        self.btn_salvar.setObjectName('btn_salvar')

        self.grd_form.addWidget(self.btn_salvar, 4, 3, 1, 1)

        self.verticalLayout.addLayout(self.grd_form)

        QWidget.setTabOrder(self.txt_banco, self.txt_usuario)
        QWidget.setTabOrder(self.txt_usuario, self.txt_senha)
        QWidget.setTabOrder(self.txt_senha, self.txt_host)
        QWidget.setTabOrder(self.txt_host, self.txt_porta)

        self.retranslateUi(QuestorDB)

        QMetaObject.connectSlotsByName(QuestorDB)

    # setupUi

    def retranslateUi(self, QuestorDB):
        QuestorDB.setWindowTitle(
            QCoreApplication.translate(
                'QuestorDB', 'Banco de Dados Questor', None
            )
        )
        self.lbl_porta.setText(
            QCoreApplication.translate('QuestorDB', 'Porta', None)
        )
        self.lbl_usuario.setText(
            QCoreApplication.translate('QuestorDB', 'Usuario', None)
        )
        self.lbl_banco.setText(
            QCoreApplication.translate('QuestorDB', 'Banco', None)
        )
        self.lbl_senha.setText(
            QCoreApplication.translate('QuestorDB', 'Senha', None)
        )
        self.lbl_host.setText(
            QCoreApplication.translate('QuestorDB', 'Host', None)
        )
        self.btn_salvar.setText(
            QCoreApplication.translate('QuestorDB', 'Salvar', None)
        )

    # retranslateUi
