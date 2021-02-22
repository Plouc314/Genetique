import bio
from PyQt5 import QtCore, QtGui, QtWidgets

_s = '&#160;'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1142, 770)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.button_exec = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_exec.setFont(font)
        self.button_exec.setObjectName("button_exec")
        self.horizontalLayout_2.addWidget(self.button_exec)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.textEdit_genome = QtWidgets.QTextEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_genome.setFont(font)
        self.textEdit_genome.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_genome.setObjectName("textEdit_genome")
        self.gridLayout_2.addWidget(self.textEdit_genome, 1, 0, 1, 1)
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
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.text_genome = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.text_genome.setFont(font)
        self.text_genome.setObjectName("text_genome")
        self.gridLayout_2.addWidget(self.text_genome, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.text_left = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_left.setFont(font)
        self.text_left.setStyleSheet("")
        self.text_left.setText("")
        self.text_left.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignTrailing)
        self.text_left.setWordWrap(False)
        self.text_left.setObjectName("text_left")
        self.gridLayout_4.addWidget(self.text_left, 0, 0, 1, 1)
        self.text_center = QtWidgets.QLabel(self.frame)
        self.text_center.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_center.setFont(font)
        self.text_center.setStyleSheet("")
        self.text_center.setText("")
        self.text_center.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.text_center.setObjectName("text_center")
        self.gridLayout_4.addWidget(self.text_center, 0, 1, 1, 1)
        self.text_right = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_right.setFont(font)
        self.text_right.setStyleSheet("")
        self.text_right.setText("")
        self.text_right.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.text_right.setWordWrap(False)
        self.text_right.setObjectName("text_right")
        self.gridLayout_4.addWidget(self.text_right, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 2, 0, 1, 1)
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
        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1142, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuCredits = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuCredits.setFont(font)
        self.menuCredits.setObjectName("menuCredits")
        self.menuhello = QtWidgets.QMenu(self.menuCredits)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuhello.setFont(font)
        self.menuhello.setObjectName("menuhello")
        self.menuAlexandre = QtWidgets.QMenu(self.menuhello)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuAlexandre.setFont(font)
        self.menuAlexandre.setObjectName("menuAlexandre")
        self.menuGitHub = QtWidgets.QMenu(self.menuCredits)
        font = QtGui.QFont()
        font.setPointSize(12)
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

        self.button_exec.clicked.connect(self.execute)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Génétique moléculaire"))
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
        self.title_ouput.setText(_translate("MainWindow", "Output"))
        self.menuCredits.setTitle(_translate("MainWindow", "Credits"))
        self.menuhello.setTitle(_translate("MainWindow", "Auteur"))
        self.menuAlexandre.setTitle(_translate("MainWindow", "Alexandre"))
        self.menuGitHub.setTitle(_translate("MainWindow", "GitHub"))
        self.actionGoumaz.setText(_translate("MainWindow", "Goumaz"))
        self.actionPlouc314.setText(_translate("MainWindow", "Plouc314"))

    def reset(self):
        self.text_left.setText('')
        self.text_center.setText('')
        self.text_right.setText('')

    def execute(self):

        self.reset()

        input_string = self.textEdit_genome.toPlainText()

        type_entree = self.box_entree.currentText()
        type_action = self.box_action.currentText()
        type_lecture = self.box_lecture.currentText()

        # lecture
        if type_lecture == "5\' → 3\'":
            start, end = "5'", "3'"
        else:
            start, end = "3'", "5'"
        
        brin = bio.Strand(input_string, start=start, end=end)

        try:
            if type_entree == "ARNm":
                brin.inv_transcribe()
            else:
                brin.transcribe()
        except Exception as e:
            if type(e) == KeyError:
                self.display_error("Le génome ne doit contenir que: A, T (U), G, C ...")
            else:
                self.display_error("Une erreur est survenue...")
            return

        # entree
        if type_entree == "Brin non-transcrit":
            brin = brin.complementary()

        elif type_entree == "ARNm":
            brin = brin.inv_transcribe()

        # action
        if type_action == "Constitution double brins":
            try:
                self.exec_double_brins(brin)
            except:
                self.display_error("Une erreur est survenue...")

        elif type_action == "Transcription":
            try:
                self.exec_transcription(brin)
            except:
                self.display_error("Une erreur est survenue...")
            
        elif type_action == "Traduction":
            
            if type_entree == "ARNm":
                try:
                    self.exec_traduction(brin)
                except:
                    self.display_error("Une erreur est survenue...")
                
            else:
                # handeln error -> input must be ARNm
                self.display_error("Il faut de l'ARNm pour effectuer une traduction.")

        elif type_action == "Tout":
            try:
                self.exec_tout(brin)
            except:
                self.display_error("Une erreur est survenue...")

    def display_error(self, msg):
        self.reset()
        self.text_left.setText(bio.get_c(msg, "red"))
        self.text_left.adjustSize()

    def _format_lines(self, string: str=None, lines: list=None):
        
        if lines is None:
            lines = string.split('\n')
        
        formatted_lines = [f'<p>{line}&#160;</p>' for line in lines] 

        return '\n'.join(formatted_lines)


    def exec_double_brins(self, brin):

        adn = bio.DNA(brin)
        lines = adn.__str__(get_lines=True)

        # add directions
        start = f'{adn.strand1.start}{_s*3}{adn.strand2.start}'
        end = f'{adn.strand1.end}{_s*3}{adn.strand2.end}'

        start = bio.get_c(start, "grey")
        end = bio.get_c(end, "grey")

        lines.insert(0, start)
        lines.append(end)

        string = self._format_lines(lines=lines)

        self.text_center.setText(string)

        self.text_center.adjustSize()

    def exec_transcription(self, brin):

        brin = brin.transcribe()
        lines = list(str(brin))

        # add directions
        start = bio.get_c(brin.start, "grey")
        end = bio.get_c(brin.end, "grey")

        lines = [start] + lines + [end]
        lines = self._format_lines(lines=lines)

        self.text_center.setText(lines)
        self.text_center.adjustSize()

    def exec_traduction(self, brin):
        ribose = bio.Ribose(brin.transcribe())

        # sep acid names and genome
        names, arn = [], []
        for line in ribose.__str__(side='left', get_lines=True):
            line = line.split(' ')
            names.append(' '.join(line[:-2]))
            arn.append(' '.join(line[-2:]))

        # add directions
        start = bio.get_c(ribose.start, "grey")
        end = bio.get_c(ribose.end, "grey")
        
        arn = [start] + arn + [end]
        names = [''] + names + ['']

        names = self._format_lines(lines=names)
        arn = self._format_lines(lines=arn)

        self.text_left.setText(names)
        self.text_center.setText(arn)

        self.text_left.adjustSize()
        self.text_center.adjustSize()


    def exec_tout(self, brin):

        adn = bio.DNA(brin)

        left, center, right = adn.display_translated(return_lines=True)

        # add directions
        start = f'{adn.strand2.start}{_s*3}{adn.strand1.start}{_s*3}{adn.strand2.start}{_s*3}{adn.strand1.start}'
        end = f'{adn.strand2.end}{_s*3}{adn.strand1.end}{_s*3}{adn.strand2.end}{_s*3}{adn.strand1.end}'
        
        start = bio.get_c(start, "grey")
        end = bio.get_c(end, "grey")

        center.insert(0, start)
        center.append(end)

        # add padding lines to left & right
        left = [''] + left + ['']
        right = [''] + right + ['']

        left = self._format_lines(lines=left)
        center = self._format_lines(lines=center)
        right = self._format_lines(lines=right)

        self.text_left.setText(left)
        self.text_center.setText(center)
        self.text_right.setText(right)

        self.text_left.adjustSize()
        self.text_center.adjustSize()
        self.text_right.adjustSize()
