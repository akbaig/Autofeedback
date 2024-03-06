from PyQt5 import QtCore, QtGui, QtWidgets

import sys, os, time
import random
import threading
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

close = False
Indez = 0
         
class Ui_MainWindow(QtCore.QObject):

    progressBarUpdate = QtCore.pyqtSignal(int)
    setVisibility = QtCore.pyqtSignal(object, bool)
    selectListItem = QtCore.pyqtSignal(object, int)

    
    def openContributorWin(self):
        self.setVisibility.emit(self.groupBox, True)
    def updateContributorWin(self, courseName, contributors):
        _translate = QtCore.QCoreApplication.translate
        str = "Course (" + courseName + ") has multiple contributors. Select one:" 
        self.label.setText(_translate("Form", str))
        for con_id in range(len(contributors)-1):
            listWidgetItem = QtWidgets.QListWidgetItem(contributors[con_id].text)
            self.listWidget.addItem(listWidgetItem)
        
        self.selectListItem.emit(self.listWidget, 0)
            
        
    def hideContributorWin(self):
        self.setVisibility.emit(self.groupBox, False)
        self.setVisibility.emit(self.progressLabel, True)
        self.setVisibility.emit(self.progressBar, True)
        self.setVisibility.emit(self.feedButton, True)
        self.setVisibility.emit(self.regNo, True)
        self.setVisibility.emit(self.access_code, True)
        self.setVisibility.emit(self.comboBox, True)
        self.setVisibility.emit(self.checkBox, True)
        self.setVisibility.emit(self.checkBox_2, True)
        self.listWidget.clear()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 496)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        layoutGrid = QtWidgets.QGridLayout()
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget") 
        self.feedButton = QtWidgets.QPushButton(self.centralwidget)
        self.feedButton.setGeometry(QtCore.QRect(340, 290, 141, 51))
        self.feedButton.setObjectName("feedButton")
        self.feedButton.setEnabled(False)
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(20, 390, 781, 31))
        self.progressLabel.setTextFormat(QtCore.Qt.AutoText)
        self.progressLabel.setScaledContents(False)
        self.progressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressLabel.setObjectName("progressLabel")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(340, 350, 141, 21))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.regNo = QtWidgets.QLineEdit(self.centralwidget)
        self.regNo.setGeometry(QtCore.QRect(340, 200, 141, 31))
        self.regNo.setInputMask("")
        self.regNo.setAlignment(QtCore.Qt.AlignCenter)
        self.regNo.setObjectName("regNo")
        self.access_code = QtWidgets.QLineEdit(self.centralwidget)
        self.access_code.setGeometry(QtCore.QRect(340, 240, 141, 31))
        self.access_code.setInputMask("")
        self.access_code.setAlignment(QtCore.Qt.AlignCenter)
        self.access_code.setObjectName("access_code")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(210, 80, 401, 61))
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.title.setStyleSheet("font: 75 bold italic 27pt \"Times New Roman\";")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setLineWidth(1)
        self.title.setMidLineWidth(0)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.credits = QtWidgets.QLabel(self.centralwidget)
        self.credits.setGeometry(QtCore.QRect(510, 130, 101, 16))
        self.credits.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.credits.setMouseTracking(False)
        self.credits.setWhatsThis("")
        self.credits.setObjectName("credits")
        self.creditsGui = QtWidgets.QLabel(self.centralwidget)
        self.creditsGui.setGeometry(QtCore.QRect(630, 450, 250, 20))
        self.creditsGui.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.creditsGui.setObjectName("creditsGui")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 160, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.onOptionSelect)
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        #self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(250, 160, 311, 241))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(30, 100, 256, 71))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(100, 190, 121, 41))
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(490, 300, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(490, 320, 141, 17))
        self.checkBox_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox_2.setObjectName("checkBox_2")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.feedButton.clicked.connect(self.onclicked)
        self.pushButton.clicked.connect(self.onclicked2)
        self.listWidget.itemClicked.connect(self.itemActivated_event)
        
        
        self.progressBarUpdate.connect(self.updateProgressBar)
        self.setVisibility.connect(self.updateVisibility)
        self.selectListItem.connect(self.updateListItem)
    
    @QtCore.pyqtSlot(int)
    def updateProgressBar(self, value):
        self.progressBar.setValue(value)
        
    @QtCore.pyqtSlot(object, bool)
    def updateVisibility(self, object, value):
        object.setVisible(value)
        
    @QtCore.pyqtSlot(object, int)
    def updateListItem(self, object, value):
        (object.item(value)).setSelected(True)
        
    def itemActivated_event(self, item):
        global Indez
        Indez = self.listWidget.row(item)
        
    def onclicked2(self):
        self.hideContributorWin()
        global close 
        close = True
    
    def onOptionSelect(self):
        _translate = QtCore.QCoreApplication.translate
        if self.comboBox.currentIndex() == 0:
            self.feedButton.setEnabled(False)
            send_msg(self, "notify", "Select your department")
        else:
            self.feedButton.setEnabled(True)
            send_msg(self, "notify", "Enter Reg. No & Access Code")
            
    def onclicked(self):
        index = self.comboBox.currentIndex()
        if index == 0:
            send_msg(self, "error", "You must select a department")
        elif not self.regNo.text():
            send_msg(self, "error", "Registration Number cannot be EMPTY")
        elif not self.access_code.text():
            send_msg(self, "error", "Access Code cannot be EMPTY")
        else:
            send_msg(self, "notify", "Initializing..")
            Reg = self.regNo.text()
            Code = self.access_code.text()
            self.feedButton.setEnabled(False)
            self.progressBarUpdate.emit(0)
            browser.get("http://111.68.99.200/SRA-n/")
            startLoginThread(self, Reg, Code, index)
            
	
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autofeed"))
        MainWindow.setWindowIcon(QtGui.QIcon('blue.ico'))
        self.feedButton.setText(_translate("MainWindow", "Start Auto-Feed"))
        self.progressLabel.setText(_translate("MainWindow", "Please wait while we fetch departments from http://111.68.99.200/SRA-n/"))
        self.regNo.setPlaceholderText(_translate("MainWindow", "Your Registration No."))
        self.access_code.setPlaceholderText(_translate("MainWindow", "Your Access Code"))
        self.title.setToolTip(_translate("MainWindow", "Automation for feeding your courses\' feedbacks with random gen numbers."))
        self.title.setStatusTip(_translate("MainWindow", "Name of the program"))
        self.title.setText(_translate("MainWindow", "Autofeed v3.4 (PIEAS)"))
        self.credits.setToolTip(_translate("MainWindow", "Main coder"))
        self.credits.setStatusTip(_translate("MainWindow", "Coder"))
        self.credits.setText(_translate("MainWindow", "By Laughing-Kid"))
        self.creditsGui.setToolTip(_translate("MainWindow", "This program was first written in console. Later a gui was designed for it by AKBAIG. (gui stands for graphical user interface)"))
        self.creditsGui.setStatusTip(_translate("MainWindow", "GUI-Designer"))
        self.creditsGui.setText(_translate("MainWindow", "GUI-Programmed by AKBAIG"))
        
        self.label.setText(_translate("MainWindow", "Course (Technical Writing) has multiple contributors. Choose one "))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Select"))
        
        self.checkBox.setText(_translate("MainWindow", "Regular"))
        self.checkBox_2.setText(_translate("MainWindow", "Detailed"))
        
    def updatedepartments(self, MainWindow):
        
        for o in get_departments(self):
            self.comboBox.addItem(o.text) 
        send_msg(self, "notify", "Select your department")
        
        

def startLoginThread(self, Reg, Code, index):
    loginThread = threading.Thread(target=login, args=(Reg, Code, index, self,))
    loginThread.start()
    
def run_driver(ui, MainWindow):   
  
    global browser
    try:
        browser = Chrome(ChromeDriverManager().install())
    except WebDriverException:
        send_msg(ui, "error", "Chrome not found")
            
    browser.get("http://111.68.99.200/SRA-n/")
    ui.updatedepartments(MainWindow)
    MainWindow.activateWindow()
    ui.comboBox.setEnabled(True)
    
def send_msg(ui, type, msg):
    _translate = QtCore.QCoreApplication.translate
    if type == "notify":
        ui.progressLabel.setStyleSheet("color: #000000;font-weight: bold;")
    elif type == "error":
        ui.progressLabel.setStyleSheet("color: #A11515;font-weight: bold;")
    elif type == "success":
        ui.progressLabel.setStyleSheet("color: #33AA33;font-weight: bold;")
    ui.progressLabel.setText(_translate("MainWindow", msg))
        
    
def get_departments(self):
    
    if check_element(self, "ddlDegreeProg"):
        select = Select(browser.find_element_by_id("ddlDegreeProg"))
        return select.options
    else:
        browser.quit()
            
def login(studentId, studentPassword, dept_index, self):

    #NOTE: I am continuously using find_by_element instead of storing it in a variable
    #because our universities bad coding practices resest the entire DOM and makes the
    #variable invalid
    
    #no check here because we already found the staleness of "ddlDegreeProg" before
    select = Select(browser.find_element_by_id("ddlDegreeProg"))
    select.select_by_index(dept_index)
    if check_element(self, "txtRegNo"):
        id = browser.find_element_by_id("txtRegNo")
        id.clear()
        id.send_keys(studentId)
    else:
        return 
    
    if check_element(self, "a63542B5"):
        password = browser.find_element_by_id("a63542B5")
        password.clear()
        password.send_keys(studentPassword,Keys.RETURN)
    else:
        return   
    try:
        browser.find_element_by_id("cmdViewTranscript")
    except NoSuchElementException:
        send_msg(self, "error", browser.find_element_by_id("lblMessage").text)
    else:
        send_msg(self, "notify", "Opening Menu..")
        (browser.find_element_by_id("cmdViewTranscript")).send_keys(Keys.RETURN)
        send_msg(self, "notify", "Opening Feedback Page..")
        (browser.find_element_by_id("btnfeedback")).send_keys(Keys.RETURN)
        if check_element(self, "_ctl0_ContentPlaceHolder1_ddlCourse"):
            try:
                element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "_ctl0_ContentPlaceHolder1_ddlCourse")))
            except TimeoutException:
                send_msg(self, "error", "Unexcepted timeout, try again")
            else:
                course_id = Select(element)
                courses = course_id.options
                if self.checkBox.isChecked() or self.checkBox_2.isChecked():
                    return_val = 1
                    if self.checkBox.isChecked():
                        return_val = feedback(self, len(courses)-1) 
                    if self.checkBox_2.isChecked() and return_val == 1:
                        detailed_feedback(self, len(courses)-1)
                else:
                    send_msg(self, "error", "You must select a feedback option")
        else:
            return
    finally:
        self.feedButton.setEnabled(True)
    
def feedback(self, courses_len):
    
    completed = 0.0
    portion = 100.0/(courses_len)
    sub_portion = (portion/18.0)
    send_msg(self, "success", "Starting feedback-automation..")
    #Loops through the entire feedback and sets a random value for every question
    for name in range(courses_len):

        self.progressBarUpdate.emit(int(completed))
        if check_element(self, "_ctl0_ContentPlaceHolder1_ddlCourse"):
            (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))).select_by_index(name)
            if check_element(self, "_ctl0_ContentPlaceHolder1_ddlContributor"):
                contributor_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))
                contributors = contributor_id.options
                num_of_cont = len(contributors)-1
                if check_element(self, "_ctl0_ContentPlaceHolder1_ddlCourse"):
                    _course = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))
                    _course_name = _course.options[name].text
                    msg = "Generating regular feedback for " + _course_name + ".."
                    send_msg(self, "success", msg)
                    #checking cookies
                    dict = browser.get_cookie(_course_name)
                    if dict:
                        msg = "Contributor of course " + _course_name + " FOUND in cookies.."
                        send_msg(self, "success", msg)
                        contributor_id.select_by_visible_text(dict.get("value"))
                    else:
                        if num_of_cont > 1:                            
                            self.setVisibility.emit(self.progressLabel, False)
                            self.setVisibility.emit(self.progressBar, False)
                            self.setVisibility.emit(self.feedButton, False)
                            self.setVisibility.emit(self.regNo, False)
                            self.setVisibility.emit(self.access_code, False)
                            self.setVisibility.emit(self.comboBox, False)
                            self.setVisibility.emit(self.checkBox, False)
                            self.setVisibility.emit(self.checkBox_2, False)
                            
                            self.openContributorWin()
                            self.updateContributorWin(_course_name, contributors)
                            close2Thread = threading.Thread(target=checkclose, args=())
                            close2Thread.start()
                            close2Thread.join()
                            global close
                            close = False
                            global Indez
                            if check_element(self, "_ctl0_ContentPlaceHolder1_ddlContributor"):
                                contributor_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))
                                contributors = contributor_id.options
                                contributor_id.select_by_index(Indez)
                                browser.add_cookie({"name": _course_name, "value": contributors[Indez].text})
                            else:
                                return 0
                        else:     
                            if check_element(self, "_ctl0_ContentPlaceHolder1_ddlContributor"):
                                contributor_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))
                                contributors = contributor_id.options
                                contributor_id.select_by_index(0)
                                browser.add_cookie({"name": _course_name, "value": contributors[0].text})
                            else:
                                return 0
                            
                    for i in range(0,18):
                        score = "_ctl0_ContentPlaceHolder1_txt" + (chr(ord('A') + i))
                        randNumber = random.randrange(1,6)
                        if (element:=check_element(self, score)):
                            element.send_keys(randNumber)
                        else:
                            return 0
                        completed += sub_portion
                        self.progressBarUpdate.emit(int(completed))
                        
                    #Writes the messages in the two text areas. You can change the messages
                    if (element:=check_element(self, "_ctl0_ContentPlaceHolder1_txtComments")):
                        element.send_keys("""No Comment""")
                    else:
                        return 0
                    if (element:=check_element(self, "_ctl0_ContentPlaceHolder1_txtCommentsCourse")):
                        element.send_keys("""No Comment""")
                    else:
                        return 0
                    if (element:=check_element(self, "_ctl0_ContentPlaceHolder1_cmdSubmit")):
                        element.send_keys(Keys.RETURN)
                    else:
                        return 0
                    if (element:=check_element(self, "_ctl0_ContentPlaceHolder1_cmdReset")):
                        try:
                            element.send_keys(Keys.RETURN)
                        except ElementNotInteractableException:
                            send_msg(self, "error", "Feedback already submitted")
                            (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtComments")).clear()
                            (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtCommentsCourse")).clear()
                    else:
                        return 0     
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    send_msg(self, "success", "Feedback completed")
    return 1

def detailed_feedback(self, courses_len):
    
    send_msg(self, "success", "Starting detailed feedback-automation..")
    boxId = ("A1","A2","A3","A4","B2","B3","B4","C1","C2","C3","C4","C5","D1","D2","D3",\
    "D4","D5","E1","E2","E3","E4","F1","F2","F3","F4","G1","G2","G3","G4","H1","H2","H3","I1","I2")
    
    completed = 0.0
    courses_prog = 25.0
    portion = courses_prog/(courses_len)
    
    
    for name in range(courses_len):
        (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))).select_by_index(name)
        _course = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))
        c_name = _course.options[name].text
        dict = browser.get_cookie(c_name)
        if dict:
            msg = "Contributor of course " + c_name + " FOUND in cookies.."
            send_msg(self, "success", msg)
        else:
            (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))).select_by_index(name)
            contributor_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))
            contributors = contributor_id.options
            num_of_cont = len(contributors)-1
            _course = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))
            _course_name = _course.options[name].text
            msg = "Saving contributor of " + _course_name + ".."
            send_msg(self, "success", msg)
            
            if num_of_cont > 1:
                self.setVisibility.emit(self.progressLabel, False)
                self.setVisibility.emit(self.progressBar, False)
                self.setVisibility.emit(self.feedButton, False)
                self.setVisibility.emit(self.regNo, False)
                self.setVisibility.emit(self.access_code, False)
                self.setVisibility.emit(self.comboBox, False)
                self.setVisibility.emit(self.checkBox, False)
                self.setVisibility.emit(self.checkBox_2, False)
                self.openContributorWin()
                self.updateContributorWin(_course_name, contributors)
                closeThread = threading.Thread(target=checkclose, args=())
                closeThread.start()
                closeThread.join()
                global close
                close = False
                global Indez
                contributor_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))
                contributors = contributor_id.options
                contributor_id.select_by_index(Indez)
                browser.add_cookie({"name": _course_name, "value": contributors[Indez].text})
                
            else:
                contributor_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))
                contributors = contributor_id.options
                contributor_id.select_by_index(0)
                browser.add_cookie({"name": _course_name, "value": contributors[0].text})
        
        completed += portion
        self.progressBarUpdate.emit(int(completed))
        
    
    browser.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdCourseEvaluation2").send_keys(Keys.RETURN)
    _courses = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")).options
    courseLength = len(_courses)
    
    
    
    if courseLength == 0:
        send_msg(self, "error", "All the detailed feedbacks have already been submitted before")
        self.progressBarUpdate.emit(100)
        
    else:
        
        portion = (100.0-courses_prog)/courseLength
        sub_portion = portion/len(boxId)
        for i in range(courseLength):
            c_name = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")).options[0].text
            dict = browser.get_cookie(c_name)
            if dict: 
                Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse")).select_by_index(0)
                browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtfnames").send_keys(dict.get("value"))  
                #notification
                msg = "Generating detailed feedback for " + c_name + ".."
                send_msg(self, "success", msg)
                #generating rand feedback
                (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtB1")).send_keys("5")
                for run in range(len(boxId)):
                    completed += sub_portion
                    self.progressBarUpdate.emit(int(completed))
                    try:
                        currentElement = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "_ctl0_ContentPlaceHolder1_txt"+boxId[run])))
                    except TimeoutException:
                        send_msg(self, "error", "Error occured; An HTML element was not found.. Try again")
                        return
                    else:
                        randNumber = random.randrange(1,6)
                        if(currentElement.tag_name == "textarea"):
                            currentElement.send_keys("No comment")
                        else:
                            currentElement.send_keys(randNumber)
     
                (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit")).send_keys(Keys.RETURN)
                (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset")).send_keys(Keys.RETURN)
            else:
                completed += portion
                self.progressBarUpdate.emit(int(completed))
                msg = "No cookie found for " + c_name
                send_msg(self, "error", msg)
            
        send_msg(self, "success", "Detailed feedback completed")
            
def check_element(object, element_id):    
    try:
        element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, element_id)))
    except StaleElementReferenceException:
            send_msg(object, "error", "ERROR: [" + element_id + "]'s staleness not found. Try running the program again?")
            return False
    else:
        return element
            
def checkclose():
    while(not close):
        time.sleep(1)
        pass
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    driverThread = threading.Thread(target=run_driver, args=(ui, MainWindow,))
    driverThread.start()
    MainWindow.show()
    ui.comboBox.setEnabled(False)
    ui.groupBox.setVisible(False)  
    sys.exit(app.exec_())
    
    