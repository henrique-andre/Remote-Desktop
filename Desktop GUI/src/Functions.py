# GUI Functions
# import nessessary modules from Pyside6 and custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader

from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QGraphicsColorizeEffect

class GuiFunctions():
    def __init__(self, MainWindow):
        self.main = MainWindow
        self.ui =MainWindow.ui

        # apply font
        self.loadproductSansFont()


        #init app theme
        self.initializeAppTheme()

        # add click evt to search button

        self.ui.searchBtn.clicked.connect(self.showSearchResults)

    # Create search tooltip
    def createSearchTipOverlay(self):
        """Create a serch tip overlay under the search input"""
        self.searchTooltip = QCustomTipOverlay(
            title="Search results.",
            description="Searching...",
            icon=self.main.theme.PATH_RESOURCES+"feather/search.png", #icon path from theme resources
            isClosable=True,
            target=self.ui.searchinpCont_2, #put tip overlay under search input
            parent=self.main,
            deleteOnClose=True,
            duration=-1, #set duration to -1 to prevent auto-close
            tailPosition="top-center",
            closeIcon=self.main.theme.PATH_RESOURCES+"material_desingn/close.png",
            toolFlag = True
        )

    # # Create loader
    #     loader = QCustom3CirclesLoader(
    #         parent=self.searchTooltip,
    #         color=QColor(self.main.theme.COLOR_ACCENT_1), #color from theme
    #         penWidth=10,
    #         animationDuration=400
    #     )

        #add loader to the tipoverlay
    #show tip overlay
    def showSearchResults(self):
        try:
            self.searchTooltip.show()
        except: #tooltip deleted
            #re-init
            self.createSearchTipOverlay()
            self.searchTooltip.show()

    # initialize app theme
    def initializeAppTheme(self):
        """initialize the application theme from settings"""
        settings = QSettings()
        current_theme = settings.value("THEME")
        # print("Current theme is: ", current_theme)

        # Add theme to the theme list
        self.populateThemeList(current_theme)

        # Connect theme change signal to change app theme
        self.ui.themeList.currentTextChanged.connect(self.changeAppTheme)

    def populateThemeList(self, current_theme):
        """Populate the list from available app themes"""
        theme_count = -1
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)
            # check default theme/current theme
            if theme.defaultTheme or theme.name == current_theme:
                self.ui.themeList.setCurrentIndex(theme_count) #select the theme

    # change app theme
    def changeAppTheme(self):
        """Change app theme based on user selection"""
        settings = QSettings()
        selected_theme = self.ui.themeList.currentData()
        current_theme = settings.value("THEME")

        if current_theme != selected_theme:
            # apply new theme
            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)


    # apply custom font
    def loadproductSansFont(self):
        """Load and apply product sans font"""
        font_id = QFontDatabase.addApplicationFont("Desktop GUI/fonts/ProductSans-Regular.ttf")
        # if font loaded
        if font_id == -1:
            print("Failed to load Product Sans font")
            return
        
        # Apply font
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        if font_family:
            product_sans = QFont(font_family[0])
        else:
            product_sans = QFont("Sans Serif")

        # apply to main window
        self.main.setFont(product_sans)
