from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPalette, QColor
import tkinter as tk
import tkinter.filedialog
import os, pathlib
from os import path
import sys


class Application:
    base_dir = pathlib.Path(__file__).parent.resolve()
    
    def __init__(self):
        self.app = QApplication([])
        self.setTheme()

        self.ui = uic.loadUi(self.basePath('ui', 'MainWindow.ui'))

        #tie functions to signals
        self.ui.page1_select_files_button.clicked.connect(self.signal_selectFiles)
        self.ui.page1_output_button.clicked.connect(self.signal_output)

        #end of tie functions

        self.tk_root = None
        pass


    def showMe(self):
        self.ui.show()

    def exec(self):
        return self.app.exec()


    def basePath(self, *args):
        """Return the full path of the folders and files\n
        Ex. "ui" and "file.ui" will return "basepath//ui//file.ui"
        """
        base_path = os.path.join(self.base_dir, args[0])
        for arg in args[1:]:
            base_path = os.path.join(base_path, arg)
        return base_path


    def createTkWindow(self):
        """Instantiate the tk root window and return the reference"""
        if(self.tk_root is None):
            self.tk_root =  tk.Tk()
            #hide the main window
            self.tk_root.withdraw()
        return self.tk_root

    def setTheme(self):
        """Set the theme of the app"""
        self.app.setStyle('Fusion')
        self.app.setWindowIcon(QtGui.QIcon(self.basePath('icons', 'ITA_icon.png')))
        palette = QPalette()
        #setting dark theme from https://stackoverflow.com/questions/48256772/dark-theme-for-qt-widgets
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.app.setPalette(palette)



# Start of signal functions

    def signal_selectFiles(self):
        """Return the list of files"""
        #open a browseable window
        root = self.createTkWindow()
        files =  tk.filedialog.askopenfilenames(parent=root, title='Choose your files')
        #add files to list
        if(len(files)>0):
            self.ui.page1_input_files.addItems(files)

    def signal_output(self):
        """Select the output directory for the results"""
        # open a window
        root = self.createTkWindow()
        folder = tk.filedialog.askdirectory()

        self.ui.page1_output.setText(folder)








# end of signals
def main():
    app = Application()
        
    app.showMe()
    sys.exit(app.exec())







if __name__=="__main__":
    main()