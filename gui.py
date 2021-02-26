import bio
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from material import Ui_MainWindow

_s = '&#160;'

class HomeWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button_exec.clicked.connect(self.execute)
        self.actionPlouc314.triggered.connect(self.open_github)
        self.actionGoumaz.triggered.connect(self.open_wiki)

    def open_github(self):
        link = "https://github.com/Plouc314"
        url = QtCore.QUrl(link)
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Could not open url')

    def open_wiki(self):
        link = "https://en.wikipedia.org/wiki/Sweden"
        url = QtCore.QUrl(link)
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Could not open url')

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

        start = bio.get_c(start, "#243160") # same blue as in QLabel
        end = bio.get_c(end, "#243160") # same blue as in QLabel

        lines.insert(0, start)
        lines.append(end)

        string = self._format_lines(lines=lines)

        self.text_center.setText(string)


    def exec_transcription(self, brin):

        brin = brin.transcribe()
        lines = list(str(brin))

        # add directions
        start = bio.get_c(brin.start, "#243160") # same blue as in QLabel
        end = bio.get_c(brin.end, "#243160") # same blue as in QLabel

        lines = [start] + lines + [end]
        lines = self._format_lines(lines=lines)

        self.text_center.setText(lines)

    def exec_traduction(self, brin):
        ribose = bio.Ribose(brin.transcribe())

        # sep acid names and genome
        names, arn = [], []
        for line in ribose.__str__(side='left', get_lines=True):
            line = line.split(' ')
            names.append(' '.join(line[:-2]))
            arn.append(' '.join(line[-2:]))

        # add directions
        start = bio.get_c(ribose.start, "#243160") # same blue as in QLabel
        end = bio.get_c(ribose.end, "#243160") # same blue as in QLabel
        
        arn = [start] + arn + [end]
        names = [''] + names + ['']

        names = self._format_lines(lines=names)
        arn = self._format_lines(lines=arn)

        self.text_left.setText(names)
        self.text_center.setText(arn)



    def exec_tout(self, brin):

        adn = bio.DNA(brin)

        left, center, right = adn.display_translated(return_lines=True)

        # add directions
        start = f'{adn.strand2.start}{_s*3}{adn.strand1.start}{_s*3}{adn.strand2.start}{_s*3}{adn.strand1.start}'
        end = f'{adn.strand2.end}{_s*3}{adn.strand1.end}{_s*3}{adn.strand2.end}{_s*3}{adn.strand1.end}'
        
        start = bio.get_c(start, "#243160") # same blue as in QLabel
        end = bio.get_c(end, "#243160") # same blue as in QLabel

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

