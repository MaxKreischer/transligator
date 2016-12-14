"""
Select .txt file from file browser and create flash-cards from terminology list
contained therein
"""
import sys
import csv
#import main window obj from aqt
from aqt import mw
#import Qt Gui library
from aqt.qt import *
from aqt import editor
from anki import cards
from anki import notes
from anki import decks
from aqt.utils import showInfo
import dialog


#function to execute when menu item is selected
def doImportTerminologyFile():
    # get file from browsing the directory tree
    fileName, ok = ImportSettingsDialog().getDialogResult()
    if not ok:
        return




class ImportSettingsDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, mw)
        self.form = dialog.Ui_Form()
        self.form.setupUi(self)
        self.form.buttonBox.accepted.connect(self.accept)
        self.form.buttonBox.rejected.connect(self.reject)
        self.form.pushButton.clicked.connect(self.onBrowse)
        # The path to the media directory chosen by user
        self.terminologyList = None
        # The number of fields in the note type we are using
        self.fieldCount = 0
        self.exec_()

    def getDialogResult(self):
        # TODO: model and dictionary no longer in use, maybe again in future
        """Return a tuple containing the user-defined settings to follow
        for an import. The tuple contains four items (in order):

         - Path to chosen media directory
         - The model (note type) to use for new notes
         - A dictionary that maps each of the fields in the model to an
           integer index from the ACTIONS list
         - True/False indicating whether the user clicked OK/Cancel"""

        if self.result() == QDialog.Rejected:
            return None, False

        return self.terminologyList, True

    def onBrowse(self):
        """Show the directory selection dialog."""
        fileName = QFileDialog.getOpenFileName(mw, "Import Terminology List")
        if not fileName:
            return
        """Check for file type and format data accordingly. """
        if fileName.endswith('.txt'):
            #   showInfo('Is a text file')
            # open textfile and read it line-wise
            txtLines = open(fileName, 'r').readlines()
            # set up table for terminology list
            self.form.tableWidget.setColumnCount(2)
            self.form.tableWidget.setRowCount(len(txtLines))
            nativeLang = QTableWidgetItem("Native")
            targetLang = QTableWidgetItem("Target")
            self.form.tableWidget.setHorizontalHeaderItem(0, nativeLang)
            self.form.tableWidget.setHorizontalHeaderItem(1, targetLang)
            # fill table widget with terminology entries for user-feedback
            for idx in range(len(txtLines)):
                idxDelim = txtLines[idx].find("\t")
                inputItem_0 = QTableWidgetItem(txtLines[idx][0:idxDelim])
                inputItem_1 = QTableWidgetItem(txtLines[idx][idxDelim:].lstrip())
                self.form.tableWidget.setItem(idx, 0, inputItem_0)
                self.form.tableWidget.setItem(idx, 1, inputItem_1)

        elif fileName.endswith('.csv'):
            with open(fileName, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=',')
                rowSize = 0
                colSize = 0
                rows = []
                for row in data:
                    rows.append(row)
                    colSize = len(row)
                    rowSize = rowSize+1
                self.form.tableWidget.setColumnCount(colSize)
                self.form.tableWidget.setRowCount(rowSize)
                header0 = QTableWidgetItem(rows[0][0])
                header1 = QTableWidgetItem(rows[0][1])
                header2 = QTableWidgetItem(rows[0][2])
                header3 = QTableWidgetItem(rows[0][3])
                self.form.tableWidget.setHorizontalHeaderItem(0, header0)
                self.form.tableWidget.setHorizontalHeaderItem(1, header1)
                self.form.tableWidget.setHorizontalHeaderItem(2, header2)
                self.form.tableWidget.setHorizontalHeaderItem(3, header3)
                rows = rows[1:]
                for idx in range(rowSize-1):
                    inputItem_0 = QTableWidgetItem(rows[idx][0])
                    inputItem_1 = QTableWidgetItem(rows[idx][1])
                    inputItem_2 = QTableWidgetItem(rows[idx][2])
                    inputItem_3 = QTableWidgetItem(rows[idx][3])
                    self.form.tableWidget.setItem(idx, 0, inputItem_0)
                    self.form.tableWidget.setItem(idx, 1, inputItem_1)
                    self.form.tableWidget.setItem(idx, 2, inputItem_2)
                    self.form.tableWidget.setItem(idx, 3, inputItem_3)

        self.terminologyList = fileName
        self.form.terminologyList.setText(self.terminologyList)
        self.form.terminologyList.setStyleSheet("")

    def accept(self):
        # Show a red warning box if the user tries to import without selecting
        # a directory.
        if not self.terminologyList:
            self.form.terminologyList.setStyleSheet("border: 1px solid red")
            return
        QDialog.accept(self)

    def clearLayout(self, layout):
        """Convenience method to remove child widgets from a layout."""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())


action = QAction("Import Terminology", mw)
mw.connect(action, SIGNAL("triggered()"), doImportTerminologyFile)
mw.form.menuTools.addAction(action)
