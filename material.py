# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bio.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1195, 739)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"\n"
"    background-color: rgb(45, 46, 54);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    \n"
"    color: rgb(96, 109, 156);\n"
"\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: rgb(48, 60, 101);\n"
"    color: rgb(176, 189, 236);\n"
"\n"
"    border-radius: 12px;\n"
"    \n"
"    padding-top: 10px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: rgb(205, 206, 214);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    \n"
"    color: rgb(162, 188, 255);\n"
"    background-color: rgb(48, 60, 101);\n"
"    \n"
"    border: 3px solid rgb(134, 160, 255);\n"
"    border-radius: 12px;\n"
"\n"
"    padding-left: 20px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    \n"
"    color: rgb(162, 188, 255);;\n"
"    background-color: rgb(48, 60, 101);\n"
"    \n"
"    border: 3px solid rgb(164, 190, 255);\n"
"    border-radius: 12px;\n"
"\n"
"    padding-left: 20px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    \n"
"    color: rgb(162, 188, 255);;\n"
"    background-color: rgb(28, 40, 71);\n"
"    \n"
"    border: 4px solid rgb(164, 190, 255);\n"
"    border-radius: 12px;\n"
"\n"
"    padding-left: 20px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    \n"
"    background-color: rgb(45, 46, 54);\n"
"    color: rgb(96, 109, 156);\n"
"\n"
"    border: 3px solid rgb(144, 162, 228);\n"
"    border-radius: 10px;\n"
"\n"
"    padding-top: 10px;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(45, 46, 54);\n"
"    color: rgb(126, 139, 186);\n"
"\n"
"    border: 3px solid rgb(174, 192, 255);\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(25, 26, 34);\n"
"    color: rgb(146, 159, 206);\n"
"\n"
"    border: 3px solid rgb(214, 232, 255);\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QComboBox {\n"
"    height: 30px;\n"
"    color: rgb(132, 158, 252);\n"
"    background-color: rgb(48, 60, 101);\n"
"\n"
"    border: 3px solid rgb(134, 160, 255);\n"
"    border-radius: 12px;\n"
"\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 3px solid rgb(164, 190, 255);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-radius: 8px;\n"
"    width: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    background-color: rgb(28, 40, 81);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(images/down-arrow.png);\n"
"}\n"
"\n"
"QListView {\n"
"    background-color: rgb(28, 40, 81);\n"
"    border-style: none;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color:  rgb(65, 66, 74);\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    color: rgb(235,235,235);\n"
"    background-color:  rgb(215, 0, 87);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QMenuBar::item:focus {\n"
"    color:  rgb(255,255,255);\n"
"    background-color: rgb(195, 0, 67);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    color: rgb(235,235,235);\n"
"    background-color:  rgb(215, 0, 87);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color:  rgb(255,255,255);\n"
"    background-color: rgb(195, 0, 67);\n"
"}\n"
"\n"
"/* ^C^V SCROLL BAR */\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);;\n"
"    width: 20px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(80, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.title_ouput = QtWidgets.QLabel(self.frame)
        self.title_ouput.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title_ouput.setFont(font)
        self.title_ouput.setObjectName("title_ouput")
        self.gridLayout_6.addWidget(self.title_ouput, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setStyleSheet("\n"
"border-radius: 12px;\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 531, 618))
        self.scrollAreaWidgetContents.setStyleSheet("QLabel {\n"
"    color: rgb(36, 49, 96);\n"
"\n"
"}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.text_left = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.text_left.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_left.setFont(font)
        self.text_left.setStyleSheet("")
        self.text_left.setText("")
        self.text_left.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_left.setWordWrap(False)
        self.text_left.setObjectName("text_left")
        self.gridLayout_4.addWidget(self.text_left, 0, 0, 1, 1)
        self.text_center = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.text_center.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_center.setFont(font)
        self.text_center.setStyleSheet("")
        self.text_center.setText("")
        self.text_center.setAlignment(QtCore.Qt.AlignCenter)
        self.text_center.setObjectName("text_center")
        self.gridLayout_4.addWidget(self.text_center, 0, 1, 1, 1)
        self.text_right = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_right.setFont(font)
        self.text_right.setStyleSheet("")
        self.text_right.setText("")
        self.text_right.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.text_right.setWordWrap(False)
        self.text_right.setObjectName("text_right")
        self.gridLayout_4.addWidget(self.text_right, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_6.addWidget(self.scrollArea, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.button_exec = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_exec.setFont(font)
        self.button_exec.setStyleSheet("")
        self.button_exec.setObjectName("button_exec")
        self.horizontalLayout_2.addWidget(self.button_exec)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.textEdit_genome = QtWidgets.QTextEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_genome.setFont(font)
        self.textEdit_genome.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_genome.setObjectName("textEdit_genome")
        self.gridLayout_2.addWidget(self.textEdit_genome, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_entree = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.text_entree.setFont(font)
        self.text_entree.setObjectName("text_entree")
        self.verticalLayout.addWidget(self.text_entree)
        self.box_entree = QtWidgets.QComboBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box_entree.setFont(font)
        self.box_entree.setObjectName("box_entree")
        self.box_entree.addItem("")
        self.box_entree.addItem("")
        self.box_entree.addItem("")
        self.verticalLayout.addWidget(self.box_entree)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text_action = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.text_action.setFont(font)
        self.text_action.setObjectName("text_action")
        self.verticalLayout_2.addWidget(self.text_action)
        self.box_action = QtWidgets.QComboBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box_action.setFont(font)
        self.box_action.setObjectName("box_action")
        self.box_action.addItem("")
        self.box_action.addItem("")
        self.box_action.addItem("")
        self.box_action.addItem("")
        self.verticalLayout_2.addWidget(self.box_action)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_lecture = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.text_lecture.setFont(font)
        self.text_lecture.setObjectName("text_lecture")
        self.verticalLayout_3.addWidget(self.text_lecture)
        self.box_lecture = QtWidgets.QComboBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box_lecture.setFont(font)
        self.box_lecture.setObjectName("box_lecture")
        self.box_lecture.addItem("")
        self.box_lecture.addItem("")
        self.verticalLayout_3.addWidget(self.box_lecture)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem3, 5, 1, 1, 1)
        self.text_genome = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.text_genome.setFont(font)
        self.text_genome.setObjectName("text_genome")
        self.gridLayout_2.addWidget(self.text_genome, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1195, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuCredits = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuCredits.setFont(font)
        self.menuCredits.setObjectName("menuCredits")
        self.menuhello = QtWidgets.QMenu(self.menuCredits)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuhello.setFont(font)
        self.menuhello.setObjectName("menuhello")
        self.menuAlexandre = QtWidgets.QMenu(self.menuhello)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuAlexandre.setFont(font)
        self.menuAlexandre.setObjectName("menuAlexandre")
        self.menuGitHub = QtWidgets.QMenu(self.menuCredits)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuGitHub.setFont(font)
        self.menuGitHub.setObjectName("menuGitHub")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGoumaz = QtWidgets.QAction(MainWindow)
        self.actionGoumaz.setObjectName("actionGoumaz")
        self.actionPlouc314 = QtWidgets.QAction(MainWindow)
        self.actionPlouc314.setObjectName("actionPlouc314")
        self.menuAlexandre.addAction(self.actionGoumaz)
        self.menuhello.addAction(self.menuAlexandre.menuAction())
        self.menuGitHub.addAction(self.actionPlouc314)
        self.menuCredits.addAction(self.menuhello.menuAction())
        self.menuCredits.addAction(self.menuGitHub.menuAction())
        self.menubar.addAction(self.menuCredits.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Génétique moléculaire"))
        self.title_ouput.setText(_translate("MainWindow", "Output"))
        self.button_exec.setText(_translate("MainWindow", "Exécuter"))
        self.text_entree.setText(_translate("MainWindow", "Type d\'entrée"))
        self.box_entree.setItemText(0, _translate("MainWindow", "Brin transcrits"))
        self.box_entree.setItemText(1, _translate("MainWindow", "Brin non-transcrits"))
        self.box_entree.setItemText(2, _translate("MainWindow", "ARNm"))
        self.text_action.setText(_translate("MainWindow", "Action"))
        self.box_action.setItemText(0, _translate("MainWindow", "Constitution double brins"))
        self.box_action.setItemText(1, _translate("MainWindow", "Transcription"))
        self.box_action.setItemText(2, _translate("MainWindow", "Traduction"))
        self.box_action.setItemText(3, _translate("MainWindow", "Tout"))
        self.text_lecture.setText(_translate("MainWindow", "Lecture"))
        self.box_lecture.setItemText(0, _translate("MainWindow", "5\' → 3\'"))
        self.box_lecture.setItemText(1, _translate("MainWindow", "3\' → 5\'"))
        self.text_genome.setText(_translate("MainWindow", "Génome"))
        self.menuCredits.setTitle(_translate("MainWindow", "Credits"))
        self.menuhello.setTitle(_translate("MainWindow", "Auteur"))
        self.menuAlexandre.setTitle(_translate("MainWindow", "Alexandre"))
        self.menuGitHub.setTitle(_translate("MainWindow", "GitHub"))
        self.actionGoumaz.setText(_translate("MainWindow", "Goumaz"))
        self.actionPlouc314.setText(_translate("MainWindow", "Plouc314"))
