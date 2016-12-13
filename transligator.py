"""
Select .txt file from file browser and create flash-cards from terminology list
contained therein
"""
import sys
#import main window obj from aqt
from aqt import mw
#import "show info" tool from utils.py
from aqt.utils import getFile
#import Qt Gui library
from aqt.qt import *


#function to execute when menu item is selected
def importTerminologyFile():
    getFile(mw, "")


#create new menu item "Import Terminology"
action = QAction("Import Terminology", mw)
# Connect signal "triggered" to slot "importTerminologyFile"
action.triggered.connect(importTerminologyFile)
#add to tools menu
mw.form.menuTools.addAction(action)