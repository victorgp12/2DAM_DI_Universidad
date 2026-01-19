# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Asignatura.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AsignaturasView(object):
    def setupUi(self, AsignaturasView):
        if not AsignaturasView.objectName():
            AsignaturasView.setObjectName(u"AsignaturasView")
        AsignaturasView.resize(700, 650)
        self.verticalLayout = QVBoxLayout(AsignaturasView)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.frameHeader = QFrame(AsignaturasView)
        self.frameHeader.setObjectName(u"frameHeader")
        self.hboxLayout = QHBoxLayout(self.frameHeader)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.lblTitulo = QLabel(self.frameHeader)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(24)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout.addWidget(self.lblTitulo)


        self.verticalLayout.addWidget(self.frameHeader)

        self.frameContexto = QFrame(AsignaturasView)
        self.frameContexto.setObjectName(u"frameContexto")
        self.hboxLayout1 = QHBoxLayout(self.frameContexto)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.lblContexto = QLabel(self.frameContexto)
        self.lblContexto.setObjectName(u"lblContexto")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.lblContexto.setFont(font1)
        self.lblContexto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout1.addWidget(self.lblContexto)


        self.verticalLayout.addWidget(self.frameContexto)

        self.frameMain = QFrame(AsignaturasView)
        self.frameMain.setObjectName(u"frameMain")
        self.gridLayoutMain = QGridLayout(self.frameMain)
        self.gridLayoutMain.setObjectName(u"gridLayoutMain")
        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.txt_buscar = QLineEdit(self.frameMain)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.hboxLayout2.addWidget(self.txt_buscar)

        self.label = QLabel(self.frameMain)
        self.label.setObjectName(u"label")

        self.hboxLayout2.addWidget(self.label)

        self.cb_curso = QComboBox(self.frameMain)
        self.cb_curso.setObjectName(u"cb_curso")

        self.hboxLayout2.addWidget(self.cb_curso)

        self.label1 = QLabel(self.frameMain)
        self.label1.setObjectName(u"label1")

        self.hboxLayout2.addWidget(self.label1)

        self.cb_cuatrimestre = QComboBox(self.frameMain)
        self.cb_cuatrimestre.setObjectName(u"cb_cuatrimestre")

        self.hboxLayout2.addWidget(self.cb_cuatrimestre)

        self.label2 = QLabel(self.frameMain)
        self.label2.setObjectName(u"label2")

        self.hboxLayout2.addWidget(self.label2)

        self.cb_obligatoria = QComboBox(self.frameMain)
        self.cb_obligatoria.setObjectName(u"cb_obligatoria")

        self.hboxLayout2.addWidget(self.cb_obligatoria)


        self.gridLayoutMain.addLayout(self.hboxLayout2, 0, 0, 1, 2)

        self.tbl_asignaturas = QTableWidget(self.frameMain)
        self.tbl_asignaturas.setObjectName(u"tbl_asignaturas")

        self.gridLayoutMain.addWidget(self.tbl_asignaturas, 1, 0, 4, 1)

        self.btn_nueva = QPushButton(self.frameMain)
        self.btn_nueva.setObjectName(u"btn_nueva")

        self.gridLayoutMain.addWidget(self.btn_nueva, 1, 1, 1, 1)

        self.btn_editar = QPushButton(self.frameMain)
        self.btn_editar.setObjectName(u"btn_editar")

        self.gridLayoutMain.addWidget(self.btn_editar, 2, 1, 1, 1)

        self.btn_eliminar = QPushButton(self.frameMain)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.gridLayoutMain.addWidget(self.btn_eliminar, 3, 1, 1, 1)

        self.btn_refrescar = QPushButton(self.frameMain)
        self.btn_refrescar.setObjectName(u"btn_refrescar")

        self.gridLayoutMain.addWidget(self.btn_refrescar, 4, 1, 1, 1)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.btn_profesores = QPushButton(self.frameMain)
        self.btn_profesores.setObjectName(u"btn_profesores")

        self.hboxLayout3.addWidget(self.btn_profesores)

        self.btn_alumnos = QPushButton(self.frameMain)
        self.btn_alumnos.setObjectName(u"btn_alumnos")

        self.hboxLayout3.addWidget(self.btn_alumnos)

        self.btn_clases = QPushButton(self.frameMain)
        self.btn_clases.setObjectName(u"btn_clases")

        self.hboxLayout3.addWidget(self.btn_clases)

        self.btnExportarPdf = QPushButton(self.frameMain)
        self.btnExportarPdf.setObjectName(u"btnExportarPdf")

        self.hboxLayout3.addWidget(self.btnExportarPdf)


        self.gridLayoutMain.addLayout(self.hboxLayout3, 5, 0, 1, 2)

        self.lbl_estado = QLabel(self.frameMain)
        self.lbl_estado.setObjectName(u"lbl_estado")

        self.gridLayoutMain.addWidget(self.lbl_estado, 6, 0, 1, 2)


        self.verticalLayout.addWidget(self.frameMain)


        self.retranslateUi(AsignaturasView)

        QMetaObject.connectSlotsByName(AsignaturasView)
    # setupUi

    def retranslateUi(self, AsignaturasView):
        AsignaturasView.setWindowTitle(QCoreApplication.translate("AsignaturasView", u"Asignaturas", None))
        self.lblTitulo.setText(QCoreApplication.translate("AsignaturasView", u"ASIGNATURAS", None))
        self.lblContexto.setText(QCoreApplication.translate("AsignaturasView", u"Grado seleccionado:", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("AsignaturasView", u"Buscar asignatura...", None))
        self.label.setText(QCoreApplication.translate("AsignaturasView", u"Curso:", None))
        self.label1.setText(QCoreApplication.translate("AsignaturasView", u"Cuatrimestre:", None))
        self.label2.setText(QCoreApplication.translate("AsignaturasView", u"Tipo:", None))
        self.btn_nueva.setText(QCoreApplication.translate("AsignaturasView", u"Nueva", None))
        self.btn_editar.setText(QCoreApplication.translate("AsignaturasView", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("AsignaturasView", u"Eliminar", None))
        self.btn_refrescar.setText(QCoreApplication.translate("AsignaturasView", u"Refrescar", None))
        self.btn_profesores.setText(QCoreApplication.translate("AsignaturasView", u"Profesores", None))
        self.btn_alumnos.setText(QCoreApplication.translate("AsignaturasView", u"Alumnos", None))
        self.btn_clases.setText(QCoreApplication.translate("AsignaturasView", u"Clases", None))
        self.btnExportarPdf.setText(QCoreApplication.translate("AsignaturasView", u"Exportar PDF", None))
        self.lbl_estado.setText(QCoreApplication.translate("AsignaturasView", u"Listo", None))
    # retranslateUi

