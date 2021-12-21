# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 850)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(650, 600))
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.splitter = QSplitter(MainWindow)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setMinimumSize(QSize(0, 0))
        self.splitter.setOrientation(Qt.Vertical)
        self.vWidgetContent = QWidget(self.splitter)
        self.vWidgetContent.setObjectName(u"vWidgetContent")
        self.vLayoutContentMain = QVBoxLayout(self.vWidgetContent)
        self.vLayoutContentMain.setObjectName(u"vLayoutContentMain")
        self.label = QLabel(self.vWidgetContent)
        self.label.setObjectName(u"label")

        self.vLayoutContentMain.addWidget(self.label)

        self.hWidget = QWidget(self.vWidgetContent)
        self.hWidget.setObjectName(u"hWidget")
        self.hLayout = QHBoxLayout(self.hWidget)
        self.hLayout.setObjectName(u"hLayout")
        self.pushButtonTest = QPushButton(self.hWidget)
        self.pushButtonTest.setObjectName(u"pushButtonTest")

        self.hLayout.addWidget(self.pushButtonTest)

        self.QWidgetContent = QWidget(self.hWidget)
        self.QWidgetContent.setObjectName(u"QWidgetContent")
        self.vLayoutContent = QVBoxLayout(self.QWidgetContent)
        self.vLayoutContent.setObjectName(u"vLayoutContent")
        self.textEdit = QTextEdit(self.QWidgetContent)
        self.textEdit.setObjectName(u"textEdit")

        self.vLayoutContent.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vLayoutContent.addItem(self.verticalSpacer)


        self.hLayout.addWidget(self.QWidgetContent)


        self.vLayoutContentMain.addWidget(self.hWidget)

        self.hWidgetBottom = QWidget(self.vWidgetContent)
        self.hWidgetBottom.setObjectName(u"hWidgetBottom")
        self.hLayoutConsolerVersion = QHBoxLayout(self.hWidgetBottom)
        self.hLayoutConsolerVersion.setObjectName(u"hLayoutConsolerVersion")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayoutConsolerVersion.addItem(self.horizontalSpacer)

        self.version = QLabel(self.hWidgetBottom)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.version.setFont(font)

        self.hLayoutConsolerVersion.addWidget(self.version, 0, Qt.AlignRight)


        self.vLayoutContentMain.addWidget(self.hWidgetBottom)

        self.splitter.addWidget(self.vWidgetContent)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MassCreator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"test3", None))
        self.pushButtonTest.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">test2</p></body></html>", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"version", None))
    # retranslateUi

