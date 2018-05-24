# -*- coding: utf-8 -*-

#
# Created by: Ismael GraHms
#
# WARNING! All changes made in this file will be lost!
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from PyQt4 import QtCore, QtGui
import sys
import clipboard
import os
import webbrowser
import sip
import time
from pytube import YouTube

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    salvar = os.getcwd()+'/'+'Videos'
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(788, 523)
        Form.setMinimumSize(QtCore.QSize(788, 523))
        Form.setMaximumSize(QtCore.QSize(788, 523))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 10, 781, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 138, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 207, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 172, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 69, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 138, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 196, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 138, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 207, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 172, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 69, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 138, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 196, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 69, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 138, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 207, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 172, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 69, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 69, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 69, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 138, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 138, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 138, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.yudlabel = QtGui.QLabel(self.frame)
        self.yudlabel.setGeometry(QtCore.QRect(160, 30, 431, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sakkal Majalla"))
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.yudlabel.setFont(font)
        self.yudlabel.setAutoFillBackground(False)
        self.yudlabel.setFrameShape(QtGui.QFrame.WinPanel)
        self.yudlabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.yudlabel.setTextFormat(QtCore.Qt.AutoText)
        self.yudlabel.setScaledContents(False)
        self.yudlabel.setObjectName(_fromUtf8("yudlabel"))
        self.leitorTAB = QtGui.QTabWidget(Form)
        self.leitorTAB.setGeometry(QtCore.QRect(40, 150, 711, 301))
        self.leitorTAB.setAcceptDrops(False)
        self.leitorTAB.setAutoFillBackground(False)
        self.leitorTAB.setTabShape(QtGui.QTabWidget.Triangular)
        self.leitorTAB.setElideMode(QtCore.Qt.ElideLeft)
        self.leitorTAB.setTabsClosable(False)
        self.leitorTAB.setMovable(True)
        self.leitorTAB.setObjectName(_fromUtf8("leitorTAB"))
        self.downloadtab = QtGui.QWidget()
        self.downloadtab.setStatusTip(_fromUtf8(""))
        self.downloadtab.setObjectName(_fromUtf8("downloadtab"))

        self.linkEntry = QtGui.QLineEdit(self.downloadtab)
        self.linkEntry.setGeometry(QtCore.QRect(20, 60, 561, 21))
        self.linkEntry.setObjectName(_fromUtf8("linkEntry"))
        self.linkEntry.setStyleSheet(_fromUtf8("QLineEdit { color: blue;\n"

"                        \n"
"                        }\n"
"\n"
"\n"
""))

        #get link



        self.label = QtGui.QLabel(self.downloadtab)
        self.label.setGeometry(QtCore.QRect(20, 40, 551, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.processar = QtGui.QPushButton(self.downloadtab)
        self.processar.setGeometry(QtCore.QRect(600, 60, 91, 21))
        self.processar.setObjectName(_fromUtf8("processar"))
        self.dirBTN = QtGui.QPushButton(self.downloadtab)
        self.dirBTN.setGeometry(QtCore.QRect(500, 140, 81, 23))
        self.dirBTN.setObjectName(_fromUtf8("dirBTN"))
        self.qualidade_cnb = QtGui.QComboBox(self.downloadtab)
        self.qualidade_cnb.setGeometry(QtCore.QRect(350, 100, 231, 22))
        self.qualidade_cnb.setObjectName(_fromUtf8("qualidade_cnb"))
        self.qualidade_cnb.addItem(_fromUtf8(""))
        self.qualidade_cnb.addItem(_fromUtf8(""))
        self.qualidade_cnb.addItem(_fromUtf8(""))
        self.qualidade_cnb.addItem(_fromUtf8(""))
        self.qualidade_cnb.addItem(_fromUtf8(""))
        self.qualidade_cnb.addItem(_fromUtf8(""))
        self.qualidade_cnb.addItem(_fromUtf8(""))
        self.progressBar = QtGui.QProgressBar(self.downloadtab)
        self.progressBar.setGeometry(QtCore.QRect(40, 180, 561, 23))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar.setVisible(True)
        self.path_label = QtGui.QLabel(self.downloadtab)
        self.path_label.setGeometry(QtCore.QRect(360, 140, 141, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.path_label.setFont(font)
        self.path_label.setWordWrap(False)
        self.path_label.setObjectName(_fromUtf8("path_label"))
        self.DownloadBTN = QtGui.QPushButton(self.downloadtab)
        self.DownloadBTN.setGeometry(QtCore.QRect(600, 230, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.DownloadBTN.setFont(font)
        self.DownloadBTN.setAutoRepeat(False)
        self.DownloadBTN.setAutoExclusive(False)
        self.DownloadBTN.setAutoDefault(False)
        self.DownloadBTN.setDefault(False)
        self.DownloadBTN.setFlat(False)
        self.DownloadBTN.setObjectName(_fromUtf8("DownloadBTN"))
        self.DownloadBTN.setStyleSheet(_fromUtf8("QPushButton { color: white;\n"
"                        background: red\n"
"                        \n"
"                        }\n"
"\n"
"\n"
""))
        self.tamanhoLabel = QtGui.QLCDNumber(self.downloadtab)
        self.tamanhoLabel.setGeometry(QtCore.QRect(420, 220, 101, 51))
        self.tamanhoLabel.setSmallDecimalPoint(False)
        self.tamanhoLabel.setProperty("intValue", 0)
        self.tamanhoLabel.setObjectName(_fromUtf8("tamanhoLabel"))
        self.label_3 = QtGui.QLabel(self.downloadtab)
        self.label_3.setGeometry(QtCore.QRect(530, 240, 47, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.downloadtab)
        self.label_4.setGeometry(QtCore.QRect(370, 240, 41, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(self.downloadtab)
        self.line.setGeometry(QtCore.QRect(20, 150, 671, 41))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.videonameLabel = QtGui.QLabel(self.downloadtab)
        self.videonameLabel.setGeometry(QtCore.QRect(50, 240, 271, 31))
        self.videonameLabel.setText(_fromUtf8(""))
        self.videonameLabel.setObjectName(_fromUtf8("videonameLabel"))
        self.videonameLabel.setStyleSheet(_fromUtf8("QLabel { color: red;\n"

"                        \n"
"                        }\n"
"\n"
"\n"
""))
        self.leitorTAB.addTab(self.downloadtab, _fromUtf8(""))
        self.converttab = QtGui.QWidget()
        self.converttab.setObjectName(_fromUtf8("converttab"))
        self.toolButton = QtGui.QToolButton(self.converttab)
        self.toolButton.setGeometry(QtCore.QRect(20, 140, 201, 21))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.formatos = QtGui.QComboBox(self.converttab)
        self.formatos.setGeometry(QtCore.QRect(290, 140, 81, 21))
        self.formatos.setObjectName(_fromUtf8("formatos"))
        self.formatos.addItem(_fromUtf8(""))
        self.formatos.addItem(_fromUtf8(""))
        self.formatos.addItem(_fromUtf8(""))
        self.formatos.addItem(_fromUtf8(""))
        self.qualidade = QtGui.QComboBox(self.converttab)
        self.qualidade.setGeometry(QtCore.QRect(440, 140, 71, 22))
        self.qualidade.setObjectName(_fromUtf8("qualidade"))
        self.qualidade.addItem(_fromUtf8(""))
        self.qualidade.addItem(_fromUtf8(""))
        self.qualidade.addItem(_fromUtf8(""))
        self.qualidade.addItem(_fromUtf8(""))
        self.qualidade.setItemText(3, _fromUtf8(""))
        self.salvarDir = QtGui.QPushButton(self.converttab)
        self.salvarDir.setGeometry(QtCore.QRect(550, 140, 101, 23))
        self.salvarDir.setObjectName(_fromUtf8("salvarDir"))
        self.label_5 = QtGui.QLabel(self.converttab)
        self.label_5.setGeometry(QtCore.QRect(240, 140, 47, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.converttab)
        self.label_6.setGeometry(QtCore.QRect(380, 140, 61, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.convertprogress = QtGui.QProgressBar(self.converttab)
        self.convertprogress.setGeometry(QtCore.QRect(20, 210, 651, 23))
        self.convertprogress.setProperty("value", 0)
        self.convertprogress.setTextVisible(True)
        self.convertprogress.setObjectName(_fromUtf8("convertprogress"))
        self.lcdNumber = QtGui.QLCDNumber(self.converttab)
        self.lcdNumber.setGeometry(QtCore.QRect(540, 242, 64, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.publicidadeFrame = QtGui.QFrame(self.converttab)
        self.publicidadeFrame.setGeometry(QtCore.QRect(30, 10, 621, 111))
        self.publicidadeFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.publicidadeFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.publicidadeFrame.setObjectName(_fromUtf8("publicidadeFrame"))
        self.leitorTAB.addTab(self.converttab, _fromUtf8(""))
        self.leitortab = QtGui.QWidget()
        self.leitortab.setObjectName(_fromUtf8("leitortab"))
        self.screen = QtGui.QGraphicsView(self.leitortab)
        self.screen.setGeometry(QtCore.QRect(360, 20, 321, 201))
        self.screen.setObjectName(_fromUtf8("screen"))
        self.timeSlide = QtGui.QSlider(self.leitortab)
        self.timeSlide.setGeometry(QtCore.QRect(370, 226, 301, 20))
        self.timeSlide.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlide.setObjectName(_fromUtf8("timeSlide"))
        self.playbtn = QtGui.QPushButton(self.leitortab)
        self.playbtn.setGeometry(QtCore.QRect(494, 240, 61, 41))
        self.playbtn.setObjectName(_fromUtf8("playbtn"))
        self.nextbtn = QtGui.QPushButton(self.leitortab)
        self.nextbtn.setGeometry(QtCore.QRect(560, 250, 51, 21))
        self.nextbtn.setObjectName(_fromUtf8("nextbtn"))
        self.rwdbtn = QtGui.QPushButton(self.leitortab)
        self.rwdbtn.setGeometry(QtCore.QRect(440, 250, 51, 21))
        self.rwdbtn.setObjectName(_fromUtf8("rwdbtn"))
        self.groupBox = QtGui.QGroupBox(self.leitortab)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 271, 201))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.treeView = QtGui.QTreeView(self.groupBox)
        self.treeView.setGeometry(QtCore.QRect(10, 20, 251, 171))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.volume = QtGui.QDial(self.leitortab)
        self.volume.setGeometry(QtCore.QRect(30, 230, 31, 41))
        self.volume.setInvertedAppearance(False)
        self.volume.setInvertedControls(False)
        self.volume.setObjectName(_fromUtf8("volume"))
        self.label_2 = QtGui.QLabel(self.leitortab)
        self.label_2.setGeometry(QtCore.QRect(70, 240, 47, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.leitorTAB.addTab(self.leitortab, _fromUtf8(""))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(500, 110, 101, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.facebook = QtGui.QCommandLinkButton(Form)
        self.facebook.setGeometry(QtCore.QRect(630, 120, 121, 31))
        self.facebook.setObjectName(_fromUtf8("facebook"))

        self.retranslateUi(Form)
        self.leitorTAB.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Yud Express 1.0.2 By Ismael GraHms Beta Edition", None))
        self.yudlabel.setText(_translate("Form", "YuD Express 1.0.2", None))
        self.downloadtab.setWhatsThis(_translate("Form", "<html><head/><body><p>area de download</p></body></html>", None))
        self.label.setText(_translate("Form", "Digita ou cola o link do video que gostaria de baixar (Ex: http://www.youtube.com?v=iSmaElGraHms)", None))
        self.facebook.clicked.connect(self.fbpage)





        #convercoes

        self.toolButton.clicked.connect(self.selecionar_video)

        # botao de processar o video ou link
        self.processar.setText(_translate("Form", "Processar URL", None))
        self.processar.clicked.connect(self.videoprocess)

        # dir btn
        self.dirBTN.setText(_translate("Form", "Salvar aqui...", None))
        self.dirBTN.clicked.connect(self.salvaraqui)


        self.qualidade_cnb.setItemText(0, _translate("Form", "Melhor Qualidade", None))
        self.qualidade_cnb.setItemText(1, _translate("Form", "1080p Full HD", None))
        self.qualidade_cnb.setItemText(2, _translate("Form", "720p HD", None))
        self.qualidade_cnb.setItemText(3, _translate("Form", "480p Standard", None))
        self.qualidade_cnb.setItemText(4, _translate("Form", "360p Medio", None))
        self.qualidade_cnb.setItemText(5, _translate("Form", "240p Baixo", None))
        self.qualidade_cnb.setItemText(6, _translate("Form", "144p Muito Baixo", None))


        #salvar aqui label
        self.path_label.setText(_translate("Form", self.salvar, None))
        self.DownloadBTN.setText(_translate("Form", "DOWNLOAD", None))
        self.DownloadBTN.clicked.connect(self.download)
        self.label_3.setText(_translate("Form", "MB\'s", None))
        self.label_4.setText(_translate("Form", "tamanho", None))
        self.leitorTAB.setTabText(self.leitorTAB.indexOf(self.downloadtab), _translate("Form", "Area de download", None))
        self.toolButton.setText(_translate("Form", "Seleciona video para converter...", None))


        #formatos
        self.formatos.setItemText(0, _translate("Form", "WMA", None))
        self.formatos.setItemText(1, _translate("Form", "MP4", None))
        self.formatos.setItemText(2, _translate("Form", "MP3", None))
        self.formatos.setItemText(3, _translate("Form", "3GP", None))


        self.qualidade.setItemText(0, _translate("Form", "Alta", None))
        self.qualidade.setItemText(1, _translate("Form", "Medio", None))
        self.qualidade.setItemText(2, _translate("Form", "Baixa", None))
        self.salvarDir.setText(_translate("Form", "Salvar aqui...", None))
        self.label_5.setText(_translate("Form", "Formato :", None))
        self.label_6.setText(_translate("Form", "Qualidade :", None))
        self.leitorTAB.setTabText(self.leitorTAB.indexOf(self.converttab), _translate("Form", "Converter Video", None))
        self.playbtn.setText(_translate("Form", "PLAY/ ||", None))
        self.nextbtn.setText(_translate("Form", ">", None))
        self.rwdbtn.setText(_translate("Form", "<", None))
        self.groupBox.setTitle(_translate("Form", "Lista De Videos", None))
        self.label_2.setText(_translate("Form", "Volume", None))
        self.leitorTAB.setTabText(self.leitorTAB.indexOf(self.leitortab), _translate("Form", "Leitor YuD", None))
        self.label_7.setText(_translate("Form", "By Ismael GraHms", None))
        self.facebook.setText(_translate("Form", "facebook", None))


        if clipboard.paste().startswith('https://www.youtube') or clipboard.paste().startswith(
                'www.youtube') or clipboard.paste().startswith('youtube.com'):
            self.linkEntry.paste()


    def fbpage(self):
        webbrowser.open(url='https://web.facebook.com/FortySev7n')


        # code all time

    def videoprocess(self):

       try:

           self.link = str(self.linkEntry.text())



           if len(self.link) > 0:
               self.yt = YouTube(url=self.link, on_progress_callback=self.progress_func, on_complete_callback=self.dwn_complete)
               self.titulo = self.yt.title
               self.vidz = self.yt.streams.filter(progressive=True).all()
               self.x = 0
               for self.vid in self.vidz:
                   nv = str(self.vid).split()
                   res = str(nv[3].strip('res="'))

                   print str(self.x) + " . " + res
                   self.qualidade_cnb.setItemText(self.x, _translate("Form", res, None))
                   self.x += 1

               self.videonameLabel.setText(_fromUtf8(self.titulo))
               # videoFormat = str()
               self.v_index = int(self.qualidade_cnb.currentIndex())

               self.video = (self.vidz[self.v_index])
               print self.video
               mbsize = 1048576 #bytes
               self.mb = self.video.filesize/mbsize
               self.tamanhoLabel.display(float(self.mb))

               # globalvid = yt.streams.filter(file_extension='mp4', progressive=True).all()
               # print self.video.vidinfo
               if self.qualidade_cnb.currentIndex() == 1:
                   self.video = self.yt.streams.filter(file_extension='mp4', progressive=True).first()

                   self.tamanhoLabel.display((self.mb))

               # yt.register_on_progress_callback(self.show_progress_bar())
               self.default_path = os.getcwd() + '/' + 'Videos'


       except Exception, e:
           errorname = str(e).split()
           QtGui.QMessageBox.warning(self,'Mensagem de avisa', errorname[0] + " : Verifica se o Computador esta ligado a internet ou se o link  esta correcto", QtGui.QMessageBox.Retry)





            #################################                                                                   ###########################################





    def salvaraqui(self):

        self.salvar = QtGui.QFileDialog.getExistingDirectory(self, 'Escolher directorio')
        #salvar = os.getcwd()+'/'+'Videos'
        self.path_label.setText(_translate("Form", self.salvar, None))


    def percent(self, tem, total):
        percentagem = (float(tem) / float(total)) * float(100)
        return percentagem
    def begin(self):

        self.video.download(str(self.path), str(self.titulo + ' :' + 'Baixado atravez de YuD Express'))



    def download(self):

        self.path = self.salvar
        try:
            video = self.vidz[self.v_index]
            self.DownloadBTN.setText('...')
            self.progressBar.setVisible(True)
        except AttributeError:
            QtGui.QMessageBox.warning(self, 'Mensagem de aviso',"Tem que processar antes de baixar",
                                      QtGui.QMessageBox.Ok)



        self.begin()
        print str(self.path)



    def selecionar_video(self):
        self.con_video = self.file = str(QtGui.QFileDialog.getOpenFileName(None, 'Escolher Video', 'c:\\',"Arquivos  (*.mp4 *.wmv *.3gp *.avi)"))

    def progress_func(self,stream, chunk,file_handle, bytes_remaining):
        p = 0

        size = self.video.filesize
        #time.sleep(3)
        baixado = bytes_remaining - size
        #p = int(100 * size  / (size + bytes_remaining))

        while p <= 100:
            self.progressBar.setValue(p)
            p = int((float(baixado) / float(size)) * float(100))
            print p
            #p = self.percent(bytes_remaining, size)


    def dwn_complete(self, stream, file_handle):

        if QtGui.QMessageBox.question(None,'Abrir Video',"Video baixado com sucesso, gostaria de a abrir o video",QtGui.QMessageBox.Yes)=='Yes':
            os.startfile(file_handle)









if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon( QtGui.QIcon("imgs/movie.png") )

    global ex
    ex = Ui_Form()
    #ex.setWindowIcon(QtGui.QIcon('imgs/logo.ico'))
    ex.show()
    sys.exit(app.exec_())
