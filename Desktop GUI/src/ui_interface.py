# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(936, 510)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menuesquerdo = QWidget(self.centralwidget)
        self.menuesquerdo.setObjectName(u"menuesquerdo")
        self.verticalLayout = QVBoxLayout(self.menuesquerdo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.menuesquerdo)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_2 = QWidget(self.menuesquerdo)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_brands/icons/font_awesome/brands/creative-commons-pd-alt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_brands/icons/font_awesome/brands/salesforce.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_brands/icons/font_awesome/brands/angellist.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/aod.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.menuesquerdo)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_5 = QPushButton(self.widget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.pushButton_7)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.menuesquerdo, 0, Qt.AlignLeft)

        self.menucentral = QWidget(self.centralwidget)
        self.menucentral.setObjectName(u"menucentral")
        self.menucentral.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.menucentral)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_4 = QWidget(self.menucentral)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_8 = QPushButton(self.widget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.pushButton_8)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.stackedWidget = QStackedWidget(self.menucentral)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_6 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_5 = QWidget(self.settingsPage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.frame = QFrame(self.widget_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout_7.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.settingsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_8 = QVBoxLayout(self.informationPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.informationPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.informationPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_9 = QVBoxLayout(self.helpPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.helpPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.helpPage)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.menucentral)

        self.maiBody = QWidget(self.centralwidget)
        self.maiBody.setObjectName(u"maiBody")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maiBody.sizePolicy().hasHeightForWidth())
        self.maiBody.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.maiBody)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header = QWidget(self.maiBody)
        self.header.setObjectName(u"header")
        self.horizontalLayout_6 = QHBoxLayout(self.header)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.titleTxt_2 = QLabel(self.header)
        self.titleTxt_2.setObjectName(u"titleTxt_2")

        self.horizontalLayout_6.addWidget(self.titleTxt_2)

        self.frame_6 = QFrame(self.header)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.notificationBtn_2 = QPushButton(self.frame_6)
        self.notificationBtn_2.setObjectName(u"notificationBtn_2")
        icon9 = QIcon()
        icon9.addFile(u":/material_design/icons/material_design/notifications.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationBtn_2.setIcon(icon9)

        self.horizontalLayout_10.addWidget(self.notificationBtn_2)

        self.moreBtn_2 = QPushButton(self.frame_6)
        self.moreBtn_2.setObjectName(u"moreBtn_2")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/more-horizontal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moreBtn_2.setIcon(icon10)

        self.horizontalLayout_10.addWidget(self.moreBtn_2)

        self.profileBtn_2 = QPushButton(self.frame_6)
        self.profileBtn_2.setObjectName(u"profileBtn_2")
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn_2.setIcon(icon11)

        self.horizontalLayout_10.addWidget(self.profileBtn_2)


        self.horizontalLayout_6.addWidget(self.frame_6)

        self.searchinpCont_2 = QFrame(self.header)
        self.searchinpCont_2.setObjectName(u"searchinpCont_2")
        self.searchinpCont_2.setFrameShape(QFrame.StyledPanel)
        self.searchinpCont_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.searchinpCont_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.searchinpCont_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(16, 16))
        self.label_10.setMaximumSize(QSize(16, 16))
        self.label_10.setPixmap(QPixmap(u":/feather/icons/feather/search.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.lineEdit_2 = QLineEdit(self.searchinpCont_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_11.addWidget(self.lineEdit_2)

        self.pushButton_10 = QPushButton(self.searchinpCont_2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_11.addWidget(self.pushButton_10)


        self.horizontalLayout_6.addWidget(self.searchinpCont_2)

        self.frame_7 = QFrame(self.header)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.minimizeBtn_2 = QPushButton(self.frame_7)
        self.minimizeBtn_2.setObjectName(u"minimizeBtn_2")
        icon12 = QIcon()
        icon12.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn_2.setIcon(icon12)

        self.horizontalLayout_12.addWidget(self.minimizeBtn_2)

        self.restorebtn_2 = QPushButton(self.frame_7)
        self.restorebtn_2.setObjectName(u"restorebtn_2")
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/window_undock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restorebtn_2.setIcon(icon13)

        self.horizontalLayout_12.addWidget(self.restorebtn_2)

        self.closeBtn_2 = QPushButton(self.frame_7)
        self.closeBtn_2.setObjectName(u"closeBtn_2")
        icon14 = QIcon()
        icon14.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn_2.setIcon(icon14)

        self.horizontalLayout_12.addWidget(self.closeBtn_2)


        self.horizontalLayout_6.addWidget(self.frame_7, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.header, 0, Qt.AlignTop)

        self.mainContents = QWidget(self.maiBody)
        self.mainContents.setObjectName(u"mainContents")
        self.horizontalLayout_7 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mainPagesCont = QWidget(self.mainContents)
        self.mainPagesCont.setObjectName(u"mainPagesCont")
        self.verticalLayout_11 = QVBoxLayout(self.mainPagesCont)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.stackedWidget_2 = QStackedWidget(self.mainPagesCont)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_12 = QVBoxLayout(self.homePage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.homePage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_8)

        self.stackedWidget_2.addWidget(self.homePage)
        self.dataAnalysisPage = QWidget()
        self.dataAnalysisPage.setObjectName(u"dataAnalysisPage")
        self.verticalLayout_13 = QVBoxLayout(self.dataAnalysisPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.dataAnalysisPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_9)

        self.stackedWidget_2.addWidget(self.dataAnalysisPage)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)


        self.horizontalLayout_7.addWidget(self.mainPagesCont)

        self.menuDireito = QWidget(self.mainContents)
        self.menuDireito.setObjectName(u"menuDireito")

        self.horizontalLayout_7.addWidget(self.menuDireito)


        self.verticalLayout_10.addWidget(self.mainContents)

        self.footer = QWidget(self.maiBody)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.frame_2 = QFrame(self.footer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_5.addWidget(self.progressBar)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.sizeGripe = QFrame(self.footer)
        self.sizeGripe.setObjectName(u"sizeGripe")
        self.sizeGripe.setMinimumSize(QSize(15, 15))
        self.sizeGripe.setMaximumSize(QSize(15, 15))
        self.sizeGripe.setFrameShape(QFrame.StyledPanel)
        self.sizeGripe.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sizeGripe, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.maiBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Prime", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Teste", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Teste1", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Teste2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center Menu", None))
        self.pushButton_8.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.titleTxt_2.setText(QCoreApplication.translate("MainWindow", u"Teste - Andre Janela", None))
        self.notificationBtn_2.setText("")
        self.moreBtn_2.setText("")
        self.profileBtn_2.setText("")
        self.label_10.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Ctrl+ K", None))
        self.minimizeBtn_2.setText("")
        self.restorebtn_2.setText("")
        self.closeBtn_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Data Analysis Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Data Analy", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Teste Andre", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Theme Progress", None))
    # retranslateUi

