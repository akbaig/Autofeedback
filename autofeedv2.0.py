# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autofeed.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


import sys, os, time
import random
import threading
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 235)
        Form.setStyleSheet("")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(70, 70, 256, 71))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFocus()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 0, 321, 71))
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
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 160, 121, 41))
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.form = Form
        self.pushButton.clicked.connect(self.onclicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        #Form.setAttribute(Qt.WA_DeleteOnClose, True)
        Form.setWindowTitle(_translate("Form", "Contributor Selection"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "Course (Technical Writing) has multiple contributors. Select one:"))
        self.pushButton.setText(_translate("Form", "Select"))
        
    def onclicked(self):
        self.form.close()
         
class Ui_MainWindow(object):
    def openContributorWin(self):
        self.contWin = QtWidgets.QWidget()
        self.fui = Ui_Form()
        self.fui.setupUi(self.contWin)
        
    def showContributorWin(self):
        self.contWin.show()
        self.contWin.activateWindow()
        
    def updateContributorWin(self, courseName, contributors):
        _translate = QtCore.QCoreApplication.translate
        str = "Course (" + courseName + ") has multiple contributors. Select one:" 
        self.fui.label.setText(_translate("Form", str))
        for con_id in range(len(contributors)-1):
            listWidgetItem = QtWidgets.QListWidgetItem(contributors[con_id].text)
            self.fui.listWidget.addItem(listWidgetItem)
        self.fui.listWidget.setCurrentRow(0)
            
        
    def hideContributorWin(self):
        self.contWin.hide()
        
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
        self.title.setGeometry(QtCore.QRect(250, 80, 311, 61))
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.title.setStyleSheet("font: 75 italic 22pt \"Arial\";")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setLineWidth(1)
        self.title.setMidLineWidth(0)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.credits = QtWidgets.QLabel(self.centralwidget)
        self.credits.setGeometry(QtCore.QRect(480, 130, 101, 16))
        self.credits.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.credits.setMouseTracking(False)
        self.credits.setWhatsThis("")
        self.credits.setObjectName("credits")
        self.creditsGui = QtWidgets.QLabel(self.centralwidget)
        self.creditsGui.setGeometry(QtCore.QRect(660, 450, 141, 20))
        self.creditsGui.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.creditsGui.setObjectName("creditsGui")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 160, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.onOptionSelect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.feedButton.clicked.connect(self.onclicked)
    
    def onOptionSelect(self):
        if self.comboBox.currentIndex() == 0:
            self.feedButton.setEnabled(False)
        else:
            self.feedButton.setEnabled(True)
            
    def onclicked(self):
        _translate = QtCore.QCoreApplication.translate
        index = self.comboBox.currentIndex()
        if index == 0:
            self.progressLabel.setText(_translate("MainWindow", "ERROR: You must select a department"))
        elif not self.regNo.text():
            self.progressLabel.setText(_translate("MainWindow", "ERROR: Registration Number cannot be EMPTY"))
        elif not self.access_code.text():
            self.progressLabel.setText(_translate("MainWindow", "ERROR: Access Code cannot be EMPTY"))
        else:
            print(index)
            self.progressLabel.setText(_translate("MainWindow", "Initializing.."))
            Reg = self.regNo.text()
            Code = self.access_code.text()
            self.openContributorWin()
            loginThread = threading.Thread(target=login, args=(Reg, Code, index, self,))
            loginThread.start()
	
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autofeed"))
        self.feedButton.setText(_translate("MainWindow", "Start Auto-Feed"))
        self.progressLabel.setText(_translate("MainWindow", "Fetching departments from http://111.68.99.200/SRA-n/"))
        self.regNo.setPlaceholderText(_translate("MainWindow", "Your Registration No."))
        self.access_code.setPlaceholderText(_translate("MainWindow", "Your Access Code"))
        self.title.setToolTip(_translate("MainWindow", "Automation for feeding your courses\' feedbacks with random gen numbers."))
        self.title.setStatusTip(_translate("MainWindow", "Name of the program"))
        self.title.setText(_translate("MainWindow", "Autofeed v1.2 (PIEAS)"))
        self.credits.setToolTip(_translate("MainWindow", "Main coder"))
        self.credits.setStatusTip(_translate("MainWindow", "Coder"))
        self.credits.setText(_translate("MainWindow", "By Laughing-Kid"))
        self.creditsGui.setToolTip(_translate("MainWindow", "This program was first written in console. Later a gui was designed for it by AKBAIG. (gui stands for graphical user interface)"))
        self.creditsGui.setStatusTip(_translate("MainWindow", "GUI-Designer"))
        self.creditsGui.setText(_translate("MainWindow", "GUI-Designed by AKBAIG"))
        
    def updatedepartments(self, MainWindow):
        
        for o in get_departments():
            self.comboBox.addItem(o.text)
        
        _translate = QtCore.QCoreApplication.translate
        self.progressLabel.setText(_translate("MainWindow", "Departments Fetched"))
        
        


def run_driver():
    
    global browser
    global is_firefox
    is_firefox = False
    if getattr(sys, 'frozen', False):
    # executed as a bundled exe, the driver is in the extracted folder
        try:
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            browser = Chrome(chromedriver_path)
            
        except WebDriverException:
            geckodriver_path = os.path.join(sys._MEIPASS, "geckodriver.exe")
            browser = Firefox(executable_path=geckodriver_path)
            is_firefox = True
            delay = 5
    else:
    # executed as a simple script, the driver should be in `PATH`
        try:
            browser = Chrome()
        except WebDriverException:
            browser = Firefox()
            is_firefox = True
            delay = 5

    browser.get("http://111.68.99.200/SRA-n/")
    
def get_departments():

    check_element('ddlDegreeProg')
    select = Select(browser.find_element_by_id("ddlDegreeProg"))
    return select.options
            
def login(studentId, studentPassword, dept_index, self):

    #NOTE: I am continuously using find_by_element instead of storing it in a variable
    #because our universities bad coding practices resest the entire DOM and makes the
    #variable invalid
    
    select = Select(browser.find_element_by_id("ddlDegreeProg"))
    select.select_by_index(dept_index)
    id = browser.find_element_by_id("txtRegNo")
    id.clear()
    id.send_keys(studentId)
    
    password = browser.find_element_by_id("a63542B5")
    password.clear()
    password.send_keys(studentPassword,Keys.RETURN)
    
    try:
        browser.find_element_by_id("cmdViewTranscript")
        #element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "cmdViewTranscript")))
    except NoSuchElementException:
        _translate = QtCore.QCoreApplication.translate
        str = "ERROR: " + browser.find_element_by_id("lblMessage").text
        self.progressLabel.setText(_translate("MainWindow", str))
    else:
        self.feedButton.setEnabled(False)
        _translate = QtCore.QCoreApplication.translate
        self.progressLabel.setText(_translate("MainWindow", "Opening Main Menu.."))
        check_element('cmdViewTranscript')
        (browser.find_element_by_id("cmdViewTranscript")).send_keys(Keys.RETURN)
        self.progressLabel.setText(_translate("MainWindow", "Opening Feedback Page.."))
        check_element('btnfeedback')
        (browser.find_element_by_id("btnfeedback")).send_keys(Keys.RETURN)   
        check_element('_ctl0_ContentPlaceHolder1_ddlCourse')
        course_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))
        courses = course_id.options
        completed = 0.0
        portion = 100.0/(len(courses) - 1)
        sub_portion = (portion/18.0)
        self.progressLabel.setText(_translate("MainWindow", "Generating feedback.."))
        
        #Loops through the entire feedback and sets a random value for every question
        for name in range(len(courses) - 1):
            
            self.progressBar.setValue(completed)
            (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))).select_by_index(name)
            
            contributor_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))
            contributors = contributor_id.options
            num_of_cont = len(contributors)-1
            _course = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))
            _course_options = _course.options
            str = "Generating feedback for " + _course_options[name].text + ".."
            self.progressLabel.setText(_translate("MainWindow", str))
            if num_of_cont > 1:
                self.centralwidget.setEnabled(False)
                #popThread = threading.Thread(target=runContributorWin, args=(self,))
                #popThread.start()
                
                #self.showContributorWin()
                #self.updateContributorWin(_course_options[name].text, contributors)
                
                
                
                #print("Course", _course_options[name].text ,"has multiple contributors. Kindly select one: ")
                #for con_id in range(num_of_cont):
                    #print(con_id, ". ", contributors[con_id].text, sep="")
                #break
                #num = input("Enter option number: ")
                #(Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))).select_by_index(num)
                (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))).select_by_index(1)
                
            else:     
                (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))).select_by_index(0)

            for i in range(0,18):
                score = "_ctl0_ContentPlaceHolder1_txt" + (chr(ord('A') + i))
                randNumber = random.randrange(1,6)
                (browser.find_element_by_id(score)).send_keys(randNumber)#You can change the value here and set it between 1-5
                completed += sub_portion
                self.progressBar.setValue(int(completed))

            #Writes the messages in the two text areas. You can change the messages
            (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtComments")).send_keys("""No Comment""")
            (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtCommentsCourse")).send_keys("""No Comment""")

            (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit")).send_keys(Keys.RETURN)
            try: 
                browser.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset").send_keys(Keys.RETURN)
            except ElementNotInteractableException:
                print("Exception occured, loop index:", name, ";skipping course")
                (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtComments")).clear()
                (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtCommentsCourse")).clear()
        
        
        self.progressLabel.setText(_translate("MainWindow", "Feedback completed"))
        
def runContributorWin(self):
    self.openContributorWin()
    self.updateContributorWin(_course_options[name].text, contributors)
    
def check_element(element):
    if is_firefox:
        try:
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, element)))
        except TimeoutException:
            print ("Loading took too much time!")
            
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    run_driver()
    ui.updatedepartments(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    
    
	