"""
Select .txt file from file browser and create flash-cards from terminology list
contained therein
"""
import sys
#import main window obj from aqt
from aqt import mw
#import Qt Gui library
from aqt.qt import *
from aqt import editor
from anki import cards
from anki import notes
import dialog


#function to execute when menu item is selected
def doImportTerminologyFile():
    (path, model, fieldMap, ok) = ImportSettingsDialog().getDialogResult()
    if not ok:
        return

class ImportSettingsDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, mw)
        self.form = dialog.Ui_Form()
        self.form.setupUi(self)
        self.form.buttonBox.accepted.connect(self.accept)
        self.form.buttonBox.rejected.connect(self.reject)
        self.form.btn_browse.clicked.connect(self.onBrowse)
        # The path to the media directory chosen by user
        self.terminologyDir = None
        # The number of fields in the note type we are using
        self.fieldCount = 0
        self.exec_()

    def getDialogResult(self):
        """Return a tuple containing the user-defined settings to follow
        for an import. The tuple contains four items (in order):
         - Path to chosen media directory
         - The model (note type) to use for new notes
         - A dictionary that maps each of the fields in the model to an
           integer index from the ACTIONS list
         - True/False indicating whether the user clicked OK/Cancel"""

        if self.result() == QDialog.Rejected:
            return (None, None, None, False)

        model = self.form.modelList.currentItem().model
        # Iterate the grid rows to populate the field map
        fieldMap = {}
        grid = self.form.fieldMapGrid
        for row in range(self.fieldCount):
            # QLabel with field name
            field = grid.itemAtPosition(row, 0).widget().text()
            # QComboBox with index from the action list
            action = grid.itemAtPosition(row, 1).widget().currentIndex()
            fieldMap[field] = action

        return (self.terminologyDir, model, fieldMap, True)

    def onBrowse(self):
        """Show the directory selection dialog."""
        path = QFileDialog.getExistingDirectory(mw, "Import Directory")
        if not path:
            return
        self.terminologyDir = path
        self.form.terminologyDir.setText(self.terminologyDir)
        self.form.terminologyDir.setStyleSheet("")

    def accept(self):
        # Show a red warning box if the user tries to import without selecting
        # a directory.
        if not self.terminologyDir:
            self.form.terminologyDir.setStyleSheet("border: 1px solid red")
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


action = QAction("Media Import...", mw)
mw.connect(action, pyqtSignal("triggered()"), doImportTerminologyFile)
mw.form.menuTools.addAction(action)
