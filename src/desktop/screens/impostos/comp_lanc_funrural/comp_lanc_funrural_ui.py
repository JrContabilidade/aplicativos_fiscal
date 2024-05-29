# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comp_lanc_funrural.ui'
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
    QDateEdit,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_CompLancFunrural(object):
    def setupUi(self, CompLancFunrural):
        if not CompLancFunrural.objectName():
            CompLancFunrural.setObjectName('CompLancFunrural')
        CompLancFunrural.resize(630, 411)
        CompLancFunrural.setMinimumSize(QSize(630, 411))
        self.verticalLayout = QVBoxLayout(CompLancFunrural)
        self.verticalLayout.setObjectName('verticalLayout')
        self.grp_arq_funrural = QGroupBox(CompLancFunrural)
        self.grp_arq_funrural.setObjectName('grp_arq_funrural')
        self.horizontalLayout = QHBoxLayout(self.grp_arq_funrural)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.txt_arq_funrural = QLineEdit(self.grp_arq_funrural)
        self.txt_arq_funrural.setObjectName('txt_arq_funrural')
        self.txt_arq_funrural.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txt_arq_funrural)

        self.btn_arq_funrural = QPushButton(self.grp_arq_funrural)
        self.btn_arq_funrural.setObjectName('btn_arq_funrural')
        self.btn_arq_funrural.setMinimumSize(QSize(45, 0))
        self.btn_arq_funrural.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout.addWidget(self.btn_arq_funrural)

        self.verticalLayout.addWidget(self.grp_arq_funrural)

        self.frm_empresa = QFrame(CompLancFunrural)
        self.frm_empresa.setObjectName('frm_empresa')
        self.frm_empresa.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_empresa)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.lbl_empresa = QLabel(self.frm_empresa)
        self.lbl_empresa.setObjectName('lbl_empresa')

        self.horizontalLayout_2.addWidget(self.lbl_empresa)

        self.txt_empresa = QSpinBox(self.frm_empresa)
        self.txt_empresa.setObjectName('txt_empresa')
        self.txt_empresa.setMinimumSize(QSize(45, 0))
        self.txt_empresa.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.txt_empresa.setMaximum(9999)

        self.horizontalLayout_2.addWidget(self.txt_empresa)

        self.lbl_filial = QLabel(self.frm_empresa)
        self.lbl_filial.setObjectName('lbl_filial')

        self.horizontalLayout_2.addWidget(self.lbl_filial)

        self.txt_filial = QSpinBox(self.frm_empresa)
        self.txt_filial.setObjectName('txt_filial')
        self.txt_filial.setMinimumSize(QSize(45, 0))
        self.txt_filial.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_2.addWidget(self.txt_filial)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addWidget(self.frm_empresa)

        self.frm_data = QGroupBox(CompLancFunrural)
        self.frm_data.setObjectName('frm_data')
        self.horizontalLayout_3 = QHBoxLayout(self.frm_data)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.lbl_data_inicio = QLabel(self.frm_data)
        self.lbl_data_inicio.setObjectName('lbl_data_inicio')
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lbl_data_inicio.sizePolicy().hasHeightForWidth()
        )
        self.lbl_data_inicio.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.lbl_data_inicio)

        self.txt_data_inicio = QDateEdit(self.frm_data)
        self.txt_data_inicio.setObjectName('txt_data_inicio')
        self.txt_data_inicio.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.txt_data_inicio)

        self.lbl_data_final = QLabel(self.frm_data)
        self.lbl_data_final.setObjectName('lbl_data_final')

        self.horizontalLayout_3.addWidget(self.lbl_data_final)

        self.txt_data_final = QDateEdit(self.frm_data)
        self.txt_data_final.setObjectName('txt_data_final')
        self.txt_data_final.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.txt_data_final)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addWidget(self.frm_data)

        self.grp_chaves_lcto = QGroupBox(CompLancFunrural)
        self.grp_chaves_lcto.setObjectName('grp_chaves_lcto')
        self.horizontalLayout_5 = QHBoxLayout(self.grp_chaves_lcto)
        self.horizontalLayout_5.setObjectName('horizontalLayout_5')
        self.txt_chaves_lcto = QPlainTextEdit(self.grp_chaves_lcto)
        self.txt_chaves_lcto.setObjectName('txt_chaves_lcto')
        self.txt_chaves_lcto.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.txt_chaves_lcto)

        self.btn_copiar = QPushButton(self.grp_chaves_lcto)
        self.btn_copiar.setObjectName('btn_copiar')

        self.horizontalLayout_5.addWidget(self.btn_copiar)

        self.verticalLayout.addWidget(self.grp_chaves_lcto)

        self.frm_botoes = QWidget(CompLancFunrural)
        self.frm_botoes.setObjectName('frm_botoes')
        self.horizontalLayout_4 = QHBoxLayout(self.frm_botoes)
        self.horizontalLayout_4.setObjectName('horizontalLayout_4')
        self.btn_baixar_modelo = QPushButton(self.frm_botoes)
        self.btn_baixar_modelo.setObjectName('btn_baixar_modelo')
        self.btn_baixar_modelo.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_4.addWidget(self.btn_baixar_modelo)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btn_limpar = QPushButton(self.frm_botoes)
        self.btn_limpar.setObjectName('btn_limpar')

        self.horizontalLayout_4.addWidget(self.btn_limpar)

        self.btn_processar = QPushButton(self.frm_botoes)
        self.btn_processar.setObjectName('btn_processar')

        self.horizontalLayout_4.addWidget(self.btn_processar)

        self.verticalLayout.addWidget(self.frm_botoes)

        self.retranslateUi(CompLancFunrural)

        QMetaObject.connectSlotsByName(CompLancFunrural)

    # setupUi

    def retranslateUi(self, CompLancFunrural):
        CompLancFunrural.setWindowTitle(
            QCoreApplication.translate(
                'CompLancFunrural', 'Comparar lan\u00e7amento Funrural', None
            )
        )
        self.grp_arq_funrural.setTitle(
            QCoreApplication.translate(
                'CompLancFunrural', 'Arquivo Funrural', None
            )
        )
        self.btn_arq_funrural.setText(
            QCoreApplication.translate('CompLancFunrural', '...', None)
        )
        self.lbl_empresa.setText(
            QCoreApplication.translate('CompLancFunrural', 'Empresa', None)
        )
        self.lbl_filial.setText(
            QCoreApplication.translate('CompLancFunrural', 'FIlial', None)
        )
        self.frm_data.setTitle(
            QCoreApplication.translate(
                'CompLancFunrural', 'Per\u00edodo dos Lan\u00e7amentos', None
            )
        )
        self.lbl_data_inicio.setText(
            QCoreApplication.translate('CompLancFunrural', 'Data Inicio', None)
        )
        self.lbl_data_final.setText(
            QCoreApplication.translate('CompLancFunrural', 'Data Final', None)
        )
        self.grp_chaves_lcto.setTitle(
            QCoreApplication.translate(
                'CompLancFunrural', 'Chave de Lan\u00e7amento Funrural', None
            )
        )
        self.btn_copiar.setText(
            QCoreApplication.translate('CompLancFunrural', 'Copiar', None)
        )
        self.btn_baixar_modelo.setText(
            QCoreApplication.translate(
                'CompLancFunrural', 'Baixar Modelo', None
            )
        )
        self.btn_limpar.setText(
            QCoreApplication.translate('CompLancFunrural', 'Limpar', None)
        )
        self.btn_processar.setText(
            QCoreApplication.translate('CompLancFunrural', 'Processar', None)
        )

    # retranslateUi
