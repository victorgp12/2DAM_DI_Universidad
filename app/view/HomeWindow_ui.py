# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(1139, 732)
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(24)
        font.setBold(True)
        HomeWindow.setFont(font)
        self.centralwidget = QWidget(HomeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(250, 70, 881, 621))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 70, 231, 621))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.menuWidget = QWidget()
        self.menuWidget.setObjectName(u"menuWidget")
        self.menuWidget.setGeometry(QRect(0, 0, 217, 1200))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.menuWidget.sizePolicy().hasHeightForWidth())
        self.menuWidget.setSizePolicy(sizePolicy)
        self.menuWidget.setMinimumSize(QSize(0, 700))
        self.verticalLayoutWidget = QWidget(self.menuWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 221, 731))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnPage1 = QPushButton(self.verticalLayoutWidget)
        self.btnPage1.setObjectName(u"btnPage1")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.btnPage1.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage1)

        self.btnPage2 = QPushButton(self.verticalLayoutWidget)
        self.btnPage2.setObjectName(u"btnPage2")
        self.btnPage2.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage2)

        self.btnPage3 = QPushButton(self.verticalLayoutWidget)
        self.btnPage3.setObjectName(u"btnPage3")
        self.btnPage3.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage3)

        self.btnPage4 = QPushButton(self.verticalLayoutWidget)
        self.btnPage4.setObjectName(u"btnPage4")
        self.btnPage4.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage4)

        self.btnPage5 = QPushButton(self.verticalLayoutWidget)
        self.btnPage5.setObjectName(u"btnPage5")
        self.btnPage5.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage5)

        self.btnPage6 = QPushButton(self.verticalLayoutWidget)
        self.btnPage6.setObjectName(u"btnPage6")
        self.btnPage6.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage6)

        self.btnPage7 = QPushButton(self.verticalLayoutWidget)
        self.btnPage7.setObjectName(u"btnPage7")
        self.btnPage7.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage7)

        self.btnPage8 = QPushButton(self.verticalLayoutWidget)
        self.btnPage8.setObjectName(u"btnPage8")
        self.btnPage8.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage8)

        self.btnPage9 = QPushButton(self.verticalLayoutWidget)
        self.btnPage9.setObjectName(u"btnPage9")
        self.btnPage9.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage9)

        self.btnPage10 = QPushButton(self.verticalLayoutWidget)
        self.btnPage10.setObjectName(u"btnPage10")
        self.btnPage10.setFont(font1)

        self.verticalLayout.addWidget(self.btnPage10)

        self.scrollArea.setWidget(self.menuWidget)
        HomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HomeWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1139, 33))
        HomeWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HomeWindow)
        self.statusbar.setObjectName(u"statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"MainWindow", None))
        self.btnPage1.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 1", None))
        self.btnPage2.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 2", None))
        self.btnPage3.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 3", None))
        self.btnPage4.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 4", None))
        self.btnPage5.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 5", None))
        self.btnPage6.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 6", None))
        self.btnPage7.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 7", None))
        self.btnPage8.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 8", None))
        self.btnPage9.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 9", None))
        self.btnPage10.setText(QCoreApplication.translate("HomeWindow", u"P\u00e1gina 10", None))
    # retranslateUi

