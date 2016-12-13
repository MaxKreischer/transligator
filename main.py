#! python3
"""
Multi line comment legibility test!
Taken from: A simple addon from Anki addon doc site
"""

#import main window obj from aqt
from aqt import mw
#import "show info" tool from utils.py
from aqt.utils import showInfo
#import Qt Gui library
from aqt.qt import *

#function to execute when menu item is selected

def importTerminologyFile():
    cardCount = mw.col.cardCount
    showInfo("Card count: %d" % cardCount)

#create new menu item "Import Terminology"
action = QAction("Import Terminology", mw)
#set to call function when clicked
action.triggered.connect(importTerminologyFile)
#add to tools menu
mw.form.menuTools.addAction(action)