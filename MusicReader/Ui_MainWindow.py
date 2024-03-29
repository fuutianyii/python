# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\python\MusicReader\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1162, 770)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 770))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 770))
        MainWindow.setBaseSize(QtCore.QSize(30, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\python\\MusicReader\\icons.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftframe = QtWidgets.QFrame(self.centralwidget)
        self.leftframe.setMinimumSize(QtCore.QSize(200, 600))
        self.leftframe.setMaximumSize(QtCore.QSize(200, 600))
        self.leftframe.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leftframe.setAutoFillBackground(False)
        self.leftframe.setStyleSheet("")
        self.leftframe.setObjectName("leftframe")
        self.formLayout = QtWidgets.QFormLayout(self.leftframe)
        self.formLayout.setObjectName("formLayout")
        self.logo = QtWidgets.QLabel(self.leftframe)
        self.logo.setMinimumSize(QtCore.QSize(170, 100))
        self.logo.setMaximumSize(QtCore.QSize(170, 100))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.logo)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.firstbuttom = QtWidgets.QPushButton(self.leftframe)
        self.firstbuttom.setMinimumSize(QtCore.QSize(170, 60))
        self.firstbuttom.setMaximumSize(QtCore.QSize(170, 60))
        self.firstbuttom.setObjectName("firstbuttom")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.firstbuttom)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.secondbutton = QtWidgets.QPushButton(self.leftframe)
        self.secondbutton.setMinimumSize(QtCore.QSize(170, 60))
        self.secondbutton.setMaximumSize(QtCore.QSize(170, 60))
        self.secondbutton.setObjectName("secondbutton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.secondbutton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.thirdbuttom = QtWidgets.QPushButton(self.leftframe)
        self.thirdbuttom.setMinimumSize(QtCore.QSize(170, 60))
        self.thirdbuttom.setMaximumSize(QtCore.QSize(170, 60))
        self.thirdbuttom.setObjectName("thirdbuttom")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.thirdbuttom)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.forthbuttom = QtWidgets.QPushButton(self.leftframe)
        self.forthbuttom.setMinimumSize(QtCore.QSize(170, 60))
        self.forthbuttom.setMaximumSize(QtCore.QSize(170, 60))
        self.forthbuttom.setObjectName("forthbuttom")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.forthbuttom)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.frithbuttom = QtWidgets.QPushButton(self.leftframe)
        self.frithbuttom.setMinimumSize(QtCore.QSize(170, 60))
        self.frithbuttom.setMaximumSize(QtCore.QSize(170, 60))
        self.frithbuttom.setSizeIncrement(QtCore.QSize(170, 60))
        self.frithbuttom.setBaseSize(QtCore.QSize(169, 60))
        self.frithbuttom.setObjectName("frithbuttom")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.frithbuttom)
        self.horizontalLayout.addWidget(self.leftframe)
        self.Rightframe = QtWidgets.QStackedWidget(self.centralwidget)
        self.Rightframe.setMinimumSize(QtCore.QSize(0, 0))
        self.Rightframe.setObjectName("Rightframe")
        self.MainPage = QtWidgets.QWidget()
        self.MainPage.setObjectName("MainPage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.MainPage)
        self.verticalLayout_9.setContentsMargins(-1, 0, 0, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(11, -1, -1, 11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 11, 2, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.shutdownwindows1 = QtWidgets.QPushButton(self.MainPage)
        self.shutdownwindows1.setMaximumSize(QtCore.QSize(30, 30))
        self.shutdownwindows1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("f:\\python\\MusicReader\\localfile/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shutdownwindows1.setIcon(icon1)
        self.shutdownwindows1.setObjectName("shutdownwindows1")
        self.horizontalLayout_8.addWidget(self.shutdownwindows1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(100, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.mainlogo = QtWidgets.QLabel(self.MainPage)
        self.mainlogo.setMinimumSize(QtCore.QSize(170, 100))
        self.mainlogo.setMaximumSize(QtCore.QSize(170, 100))
        self.mainlogo.setText("")
        self.mainlogo.setPixmap(QtGui.QPixmap("f:\\python\\MusicReader\\logo.png"))
        self.mainlogo.setObjectName("mainlogo")
        self.horizontalLayout_9.addWidget(self.mainlogo)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, -1, 50, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.mainsearch = QtWidgets.QLineEdit(self.MainPage)
        self.mainsearch.setMinimumSize(QtCore.QSize(0, 50))
        self.mainsearch.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.mainsearch.setFont(font)
        self.mainsearch.setStyleSheet("background:#343436;border-radius:25px;padding:3px 10px;color:rgb(255, 255, 255);font-family:\'微软雅黑\';font-size:20px;")
        self.mainsearch.setText("")
        self.mainsearch.setObjectName("mainsearch")
        self.verticalLayout_8.addWidget(self.mainsearch)
        spacerItem7 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.Rightframe.addWidget(self.MainPage)
        self.waitingpage = QtWidgets.QWidget()
        self.waitingpage.setObjectName("waitingpage")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.waitingpage)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.label = QtWidgets.QLabel(self.waitingpage)
        self.label.setMinimumSize(QtCore.QSize(300, 300))
        self.label.setMaximumSize(QtCore.QSize(300, 300))
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.Rightframe.addWidget(self.waitingpage)
        self.infopage = QtWidgets.QWidget()
        self.infopage.setObjectName("infopage")
        self.rightframe = QtWidgets.QFormLayout(self.infopage)
        self.rightframe.setContentsMargins(11, 0, 0, -1)
        self.rightframe.setObjectName("rightframe")
        self.frame = QtWidgets.QFrame(self.infopage)
        self.frame.setMinimumSize(QtCore.QSize(0, 600))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(11, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(11, 9, 0, 11)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.shutdownwindows2 = QtWidgets.QPushButton(self.frame_3)
        self.shutdownwindows2.setMaximumSize(QtCore.QSize(30, 30))
        self.shutdownwindows2.setText("")
        self.shutdownwindows2.setIcon(icon1)
        self.shutdownwindows2.setObjectName("shutdownwindows2")
        self.horizontalLayout_5.addWidget(self.shutdownwindows2)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainimage = QtWidgets.QLabel(self.frame_2)
        self.mainimage.setMinimumSize(QtCore.QSize(300, 300))
        self.mainimage.setMaximumSize(QtCore.QSize(300, 300))
        self.mainimage.setObjectName("mainimage")
        self.horizontalLayout_4.addWidget(self.mainimage)
        spacerItem11 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.listframe = QtWidgets.QFrame(self.frame_2)
        self.listframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listframe.setObjectName("listframe")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.listframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.listframe)
        self.frame_4.setMinimumSize(QtCore.QSize(100, 40))
        self.frame_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.return1 = QtWidgets.QPushButton(self.frame_4)
        self.return1.setMinimumSize(QtCore.QSize(100, 40))
        self.return1.setMaximumSize(QtCore.QSize(100, 40))
        self.return1.setObjectName("return1")
        self.horizontalLayout_6.addWidget(self.return1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.tableWidget = QtWidgets.QTableWidget(self.listframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 380))
        self.tableWidget.setMaximumSize(QtCore.QSize(400, 380))
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.bottomframe = QtWidgets.QFrame(self.listframe)
        self.bottomframe.setMinimumSize(QtCore.QSize(400, 0))
        self.bottomframe.setMaximumSize(QtCore.QSize(400, 16777215))
        self.bottomframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomframe.setObjectName("bottomframe")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.bottomframe)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.getmusic = QtWidgets.QPushButton(self.bottomframe)
        self.getmusic.setMinimumSize(QtCore.QSize(150, 40))
        self.getmusic.setMaximumSize(QtCore.QSize(150, 40))
        self.getmusic.setObjectName("getmusic")
        self.horizontalLayout_3.addWidget(self.getmusic)
        self.verticalLayout_2.addWidget(self.bottomframe)
        self.horizontalLayout_4.addWidget(self.listframe)
        self.verticalLayout.addWidget(self.frame_2)
        self.rightframe.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.frame)
        self.Rightframe.addWidget(self.infopage)
        self.horizontalLayout.addWidget(self.Rightframe)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.musicplayer = QtWidgets.QStackedWidget(self.centralwidget)
        self.musicplayer.setMinimumSize(QtCore.QSize(0, 100))
        self.musicplayer.setMaximumSize(QtCore.QSize(16777215, 100))
        self.musicplayer.setObjectName("musicplayer")
        self.musicplayerPage1 = QtWidgets.QWidget()
        self.musicplayerPage1.setObjectName("musicplayerPage1")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.musicplayerPage1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget = QtWidgets.QWidget(self.musicplayerPage1)
        self.widget.setObjectName("widget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Playersongname = QtWidgets.QLabel(self.widget)
        self.Playersongname.setMinimumSize(QtCore.QSize(150, 0))
        self.Playersongname.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Playersongname.setObjectName("Playersongname")
        self.horizontalLayout_10.addWidget(self.Playersongname)
        self.control = QtWidgets.QFrame(self.widget)
        self.control.setMinimumSize(QtCore.QSize(150, 0))
        self.control.setMaximumSize(QtCore.QSize(150, 16777215))
        self.control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control.setObjectName("control")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.control)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lastmusic = QtWidgets.QPushButton(self.control)
        self.lastmusic.setMinimumSize(QtCore.QSize(40, 30))
        self.lastmusic.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lastmusic.setStyleSheet("")
        self.lastmusic.setText("")
        self.lastmusic.setObjectName("lastmusic")
        self.horizontalLayout_12.addWidget(self.lastmusic)
        self.OnandOff = QtWidgets.QPushButton(self.control)
        self.OnandOff.setMinimumSize(QtCore.QSize(40, 30))
        self.OnandOff.setMaximumSize(QtCore.QSize(40, 30))
        self.OnandOff.setStyleSheet("")
        self.OnandOff.setText("")
        self.OnandOff.setObjectName("OnandOff")
        self.horizontalLayout_12.addWidget(self.OnandOff)
        self.nextmusic = QtWidgets.QPushButton(self.control)
        self.nextmusic.setMinimumSize(QtCore.QSize(40, 30))
        self.nextmusic.setMaximumSize(QtCore.QSize(40, 16777215))
        self.nextmusic.setStyleSheet("")
        self.nextmusic.setText("")
        self.nextmusic.setObjectName("nextmusic")
        self.horizontalLayout_12.addWidget(self.nextmusic)
        self.horizontalLayout_10.addWidget(self.control)
        self.runnedtime = QtWidgets.QLabel(self.widget)
        self.runnedtime.setMinimumSize(QtCore.QSize(60, 20))
        self.runnedtime.setMaximumSize(QtCore.QSize(60, 20))
        self.runnedtime.setObjectName("runnedtime")
        self.horizontalLayout_10.addWidget(self.runnedtime)
        self.progress_slider = QtWidgets.QSlider(self.widget)
        self.progress_slider.setEnabled(False)
        self.progress_slider.setMinimumSize(QtCore.QSize(200, 0))
        self.progress_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.progress_slider.setMaximum(1000)
        self.progress_slider.setOrientation(QtCore.Qt.Horizontal)
        self.progress_slider.setObjectName("progress_slider")
        self.horizontalLayout_10.addWidget(self.progress_slider)
        self.maxtime = QtWidgets.QLabel(self.widget)
        self.maxtime.setMinimumSize(QtCore.QSize(60, 20))
        self.maxtime.setMaximumSize(QtCore.QSize(60, 20))
        self.maxtime.setObjectName("maxtime")
        self.horizontalLayout_10.addWidget(self.maxtime)
        self.musicvoice = QtWidgets.QSlider(self.widget)
        self.musicvoice.setMinimumSize(QtCore.QSize(30, 0))
        self.musicvoice.setMaximumSize(QtCore.QSize(30, 16777215))
        self.musicvoice.setSizeIncrement(QtCore.QSize(30, 0))
        self.musicvoice.setProperty("value", 99)
        self.musicvoice.setOrientation(QtCore.Qt.Vertical)
        self.musicvoice.setObjectName("musicvoice")
        self.horizontalLayout_10.addWidget(self.musicvoice)
        self.verticalLayout_12.addWidget(self.widget)
        self.musicplayer.addWidget(self.musicplayerPage1)
        self.horizontalLayout_2.addWidget(self.musicplayer)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Rightframe.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.firstbuttom.setText(_translate("MainWindow", "网易云"))
        self.secondbutton.setText(_translate("MainWindow", "QQ"))
        self.thirdbuttom.setText(_translate("MainWindow", "酷狗"))
        self.forthbuttom.setText(_translate("MainWindow", "酷我"))
        self.frithbuttom.setText(_translate("MainWindow", "设置"))
        self.label.setText(_translate("MainWindow", "waiting"))
        self.mainimage.setText(_translate("MainWindow", "mainimage"))
        self.return1.setText(_translate("MainWindow", "返回"))
        self.getmusic.setText(_translate("MainWindow", " 下载"))
        self.Playersongname.setText(_translate("MainWindow", "musicreader"))
        self.runnedtime.setText(_translate("MainWindow", "00:00"))
        self.maxtime.setText(_translate("MainWindow", "00:00"))
