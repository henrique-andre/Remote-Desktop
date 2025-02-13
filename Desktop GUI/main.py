########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################


import os
import sys
########################################################################
# IMPORT GUI FILE
from src.ui_interface import *
########################################################################
#import function
from src.Functions import GuiFunctions
########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
            }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        #Application function
        self.app_functions = GuiFunctions(self)

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
