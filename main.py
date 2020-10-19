from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import calendar
import time
import sys
import petcal, signup_popup, food_warn_popup, foodedit, schedule_popup, changeimg
import petdb
import webbrowser
import requests
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.by import By

class mainClass():
    ###method
    def __init__(self, ui):
        self.mainwindow = mainwindow
        self.window = ui
        self.userPopup = userData
        self.userFood = userfood
        self.foodWarn = foodWarn
        self.schedule = schedule
        self.img = changeimg
        self.userdb = petdb.userData()
        self.userid = ''
        self.yearNmonth = []
        self.page = 0
        self.location = ''
        self.title = []
        self.phone = []
        self.address = []
        self.morePage = False
        self.pageCount = 0
        self.friendPageCount = 0
        ####window handler
        self.window.home.clicked.connect(lambda: self.goPage(0))
        self.window.findingFriend.clicked.connect(lambda: self.goPage(1))
        self.window.findingHospital.clicked.connect(lambda: self.goPage(2))
        self.window.purchasingFood.clicked.connect(lambda: self.goPage(3))
        self.window.thumbNail1.clicked.connect(lambda: self.openTube(1))
        self.window.thumbNail2.clicked.connect(lambda: self.openTube(2))
        self.window.thumbnail3.clicked.connect(lambda: self.openTube(3))
        self.window.moreVideo.clicked.connect(lambda: webbrowser.open("https://tv.naver.com/search/clip?query=진돗개산책&sort=rel&page=1&isTag=false"))
        self.window.join.clicked.connect(self.userpopupOpen)
        self.window.editFood.clicked.connect(self.foodopen)
        self.window.logout.clicked.connect(self.logout)
        self.window.login.clicked.connect(self.login)
        self.window.userIMG.clicked.connect(self.openimg)
        self.window.makeSchedule.clicked.connect(self.openSchedule)
        self.window.purchasingFood.clicked.connect(self.foodExplorer)
        self.window.goNext.clicked.connect(self.goNext)
        self.window.goPrev.clicked.connect(self.goPrev)
        self.window.yearNdate.clicked.connect(self.goNow)
        self.window.minimize.clicked.connect(lambda: mainwindow.showMinimized())
        self.window.maximize.clicked.connect(lambda: mainwindow.showMaximized())
        self.window.close.clicked.connect(mainwindow.close)
        self.window.hoispitlaNextPage.clicked.connect(self.nextHospital)
        self.window.hospitalPrevPage.clicked.connect(self.prevHospital)
        self.window.friendNextPage.clicked.connect(self.nextFriend)
        self.window.friendPrevPage.clicked.connect(self.prevFriend)
        ###userpopup handler
        self.userPopup.idCheck.clicked.connect(self.idCheck)
        self.userPopup.confirm.clicked.connect(self.userSignup)
        self.userPopup.close.clicked.connect(usermainFrame.close)
        ###userfood handler
        self.userFood.confirm.clicked.connect(self.userfood)
        self.userFood.close.clicked.connect(foodmainFrame.close)
        ###foodwarn handler
        self.foodWarn.close.clicked.connect(foodWarnmainFrame.close)
        self.foodWarn.confirm.clicked.connect(self.foodExplorer)
        self.foodWarn.cancel.clicked.connect(foodWarnmainFrame.close)
        ###img handler
        self.img.confirm.clicked.connect(self.imgchange)
        self.img.close.clicked.connect(changeimgmainFrame.close)
        ###schedule handler
        self.schedule.confirm.clicked.connect(self.saveSchedule)
        self.schedule.add.clicked.connect(self.addSchedule)
        self.schedule.close.clicked.connect(schedulemainFrame.close)
        self.makeCalendar()
        
    def makeyearndate(self):
        yearndate = str(self.yearNmonth[0]) + "년 " + str(self.yearNmonth[1]) + "월"
        return str(yearndate)

    def goNow(self):
        self.yearNmonth = []
        self.makeCalendar()
        
    def goNext(self):
        if self.yearNmonth[1] == 12:
            self.yearNmonth[1] = 1
            self.yearNmonth[0] += 1
        else:
            self.yearNmonth[1] += 1
        yearndate = self.makeyearndate()
        self.window.yearNdate.setText(yearndate)
        self.makeCalendar()

    def goPrev(self):
        if self.yearNmonth[1] == 1:
            self.yearNmonth[1] = 12
            self.yearNmonth[0] -= 1
        else:
            self.yearNmonth[1] -= 1
        yearndate = self.makeyearndate()
        self.window.yearNdate.setText(yearndate)
        self.makeCalendar()

    def makeCalendar(self):
        for i in range (7):
            for f in range (6):
                day = mainwindow.findChild(QtWidgets.QWidget, "c" +\
                    str(f) + "_" + str(i))
                day.setStyleSheet("background-color: rgb(255, 255, 255)")
                if i == 0:
                    day.setStyleSheet("color: rgb(255, 0, 0);")
                if i == 6:
                    day.setStyleSheet("color: rgb(0, 0, 255);")
                day.setText("")
        
        today = str(datetime.date.today())
        today = today.split('-')
        if self.yearNmonth == []:
            yearndate = today[0] + "년 " + today[1] + "월"
            self.yearNmonth.append(int(today[0]))
            self.yearNmonth.append(int(today[1]))
            self.yearNmonth.append(int(today[2]))
            self.window.yearNdate.setText(yearndate)

        year = int(self.yearNmonth[0])
        month = int(self.yearNmonth[1])
        date = int(self.yearNmonth[2])
        # day = int(datetime.date(year, month, date).weekday())

        thismonth = list(calendar.monthrange(year, month))
        
        if thismonth[0] == 6:
            thismonth[0] == 0
        else:
            thismonth[0] += 1

        first = mainwindow.findChild(QtWidgets.QWidget, "c" + "0_" +\
             str(thismonth[0]))
        first.setText("1")
        week = 0
        sevenDays = thismonth[0] + 1
        for i in range (2, thismonth[1] + 1):
            if sevenDays == 7:
                sevenDays = 0
                week += 1
            after = mainwindow.findChild(QtWidgets.QWidget, "c" + \
                str(week) + "_" + str(sevenDays))
            after.setText(str(i))
            sevenDays += 1

        if self.yearNmonth[0] == int(today[0]) and self.yearNmonth[1] == int(today[1]):
            for i in range(6):
                for f in range (7):
                    day = mainwindow.findChild(QtWidgets.QWidget,\
                        "c" + str(i) + "_" + str(f))
                    days = day.text()
                    if str(int(today[2])) == str(days):
                        day.setStyleSheet(
                        "border-radius: 20px;\n"
                        "border: 3px solid;\n"
                        "border-color: rgb(0, 0, 0)")

        if self.userid != '':
            scheduleList = self.userdb.showSchedule(self.userid)
            for i in range (len(scheduleList)):
                scheduledate = str(scheduleList[i][0])
                scheduledate = scheduledate.split("/")
                if scheduledate[0] == str(self.yearNmonth[1]):
                    for i in range(6):
                        for f in range (7):
                            day = mainwindow.findChild(QtWidgets.QWidget,\
                                "c" + str(i) + "_" + str(f))
                            days = day.text()
                            if scheduledate[1] == str(days):
                                day.setStyleSheet("background-color: rgb(255, 230, 153);\n"
                                "border-radius: 0px;")

    def getHospitalData(self, location, first):
        if first == True or self.morePage == True:
            option = webdriver.ChromeOptions()
            option.add_argument("headless")
            chromeDriverPath = "D:/Desktop/chromedriver.exe"
            driver = webdriver.Chrome(chromeDriverPath, options = option)
            searchWord = location + "동물병원"
            driver.get("https://map.naver.com/v5/search/{}".format(searchWord))
                # WebDriverWait(driver, 5).until(
                #     expected_conditions.invisibility_of_element(
                #     (By.CLASS_NAME, "phone")
                #     )
                # )
            time.sleep(2)
            if self.morePage == True:
                for i in range (self.pageCount):
                    driver.find_element_by_xpath("//*[@id='container']/div[1]/shrinkable-layout/search-layout/search-list/search-list-contents/div/div[2]/button[2]").click()
                    time.sleep(0.5)
                self.morePage = False
            soup = BeautifulSoup(driver.page_source, "html.parser")
            self.title = soup.select(
            "div.list_search.ng-tns-c134-4 > search-item-place > div > div > div.title_box > strong.search_title"
            )

        for i in range (4):
            oneTitle = self.title[i + self.page].select_one(
                "span.search_title_text"
                ).text
            label = mainwindow.findChild(QtWidgets.QWidget, "nameInfo" + str(i + 1))
            label.setText(oneTitle)
        if first == True:
            self.phone = soup.select(
                "div.list_search.ng-tns-c134-4 > search-item-place > div > div > div.search_text_box > span.phone"
            )
        for i in range (4):
            onePhone = self.phone[i + self.page].text

            label = mainwindow.findChild(QtWidgets.QLabel, "phoneInfo" + str(i + 1))
            label.setText(onePhone)
        if first == True:
            self.address = soup.select(
                "div.list_search.ng-tns-c134-4 > search-item-place > div > div > div.search_text_box.ng-star-inserted > span"
            )
        for i in range (4):
            oneAddress = self.address[i + self.page].text
            label = mainwindow.findChild(QtWidgets.QWidget, "addressInfo" + str(i + 1))
            label.setText(oneAddress)
    ###listener
    def prevFriend(self):
        if self.friendPageCount > 0:
            self.friendPageCount -= 1
            self.userdb.setFriend(self.window, self.userid, self.friendPageCount)

    def nextFriend(self):
        self.friendPageCount += 1
        check = self.userdb.setFriend(self.window, self.userid, self.friendPageCount)
        if check != None:
            self.friendPageCount = check

    def nextHospital(self):
        self.page += 4
        if self.page == 20:
            self.morePage = True
            self.page = 0
            self.pageCount += 1
        self.getHospitalData(self.location, False)
            
    def prevHospital(self):
        if self.pageCount > 0:
            self.morePage = True
            self.page = 16
            self.pageCount -= 1
        elif self.page > 1:
            self.page -= 4
        else:
            return None
         
        self.getHospitalData(self.location, False)

    def openTube(self, num):
        keyWord = "진돗개산책"
        url = requests.get("https://tv.naver.com/search/clip?query={}&sort=rel&page=1&isTag=false".format(keyWord))
        req = url.text
        soup = BeautifulSoup(req, "html.parser")

        thumb = soup.select(
            'div.cds_area > div.thl > div.thl_a '
        )
        tempthumb = ''
        i = num
        tempthumb = thumb[i].find("a")["href"]
        tempthumb = "https://tv.naver.com" + str(tempthumb)
        webbrowser.open(tempthumb)

    def userSignup(self):
        self.userdb.signup(self.userPopup)
        usermainFrame.close()

    def foodExplorer(self):
        if self.userdb.checkUser(self.window.loginNout):
            foodName = self.userdb.getFoodName(self.userid)
            if foodName == False or foodName.strip() == '':
                QtWidgets.QMessageBox.information(self.window.purchasingFood, "알림", "사료정보를 입력해주세요")
            else:
                url = "https://search.shopping.naver.com/search/all?query={}".format(foodName)
                webbrowser.open(url)
        foodWarnmainFrame.close()

    def addSchedule(self):
        nowRow = self.schedule.schedule.rowCount()
        self.schedule.schedule.insertRow(nowRow)

    def saveSchedule(self):
        self.userdb.saveSchedule(self.userid, self.schedule.schedule,\
            self.schedule.schedule.rowCount())
        self.userdb.setSchedule(self.window, self.schedule.schedule, self.userid)
        self.makeCalendar()
        schedulemainFrame.close()

    def openSchedule(self):
        if self.userdb.checkUser(self.window.loginNout):
            schedulemainFrame.show()
        else:
            QtWidgets.QMessageBox.information(self.window.makeSchedule, "알림", "로그인을 해주세요")

    def login(self):
        userId = self.window.pw.text()
        userPw = self.window.id.text()
        if self.userdb.loginCheck(userId, userPw):
            QtWidgets.QMessageBox.information(self.window.login, "알림", "로그인성공")
            self.window.loginNout.setCurrentIndex(1)
            self.userdb.showId(self.window, userId)
            self.userid = userId
            self.window.pw.setText('')
            self.window.id.setText('')
            self.getThumbnail()
            self.makeCalendar()
            self.userdb.setData(self.window, userId)
            self.userdb.setFriend(self.window, userId, self.friendPageCount)
            self.userdb.setFoodPopup(self.userFood, userId)
            self.userdb.setSchedule(self.window, self.schedule.schedule, userId)
            self.location = self.userdb.getLocation(self.userid)
            self.getHospitalData(self.location, True)
            if self.userdb.isFoodOk(userId) == False:
                foodWarnmainFrame.show()
        else:
            QtWidgets.QMessageBox.information(self.window.login, "알림", "ID나 PW 확인해주세요")
    
    def logout(self):
        QtWidgets.QMessageBox.information(self.window.logout, "알림", "로그아웃")
        self.window.loginNout.setCurrentIndex(0)
        self.userid = ''
        self.userdb.resetData(self.window)
        self.window.menupage.setCurrentIndex(0)
        self.window.home.setStyleSheet("QPushButton{\n"
            "background-color: rgb(217, 217, 217);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")
        self.window.findingFriend.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")        
        self.window.findingHospital.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")        
        self.window.purchasingFood.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")
        
    def foodopen(self):
        if self.userdb.checkUser(self.window.loginNout):
            foodmainFrame.show()
        else:
            QtWidgets.QMessageBox.information(self.window.editFood, "알림", "로그인을 해주세요")

    def imgchange(self):
        filePath = self.img.filePath.text()
        self.userdb.getImgPath(filePath, self.window, self.userid)
        changeimgmainFrame.close()

    def userfood(self):
        wholeFood = float(self.userFood.wholeFoodInput.text())
        foodeating = float(self.userFood.FoodEatingInput.text())
        dayEating = float(self.userFood.dayEatingInput.text())
        foodname = self.userFood.foodNameInput.text()
        self.userdb.userFood(self.userid, self.userFood, wholeFood, foodeating, dayEating, foodname)
        foodmainFrame.close()

    def userpopupOpen(self):
        self.userPopup.idInput.setText('')
        self.userPopup.passwordInput.setText('')
        self.userPopup.locationInput.setText('')
        self.userPopup.emailInput.setText('')
        usermainFrame.show()

    def openimg(self):
        if self.userdb.checkUser(self.window.loginNout):
            changeimgmainFrame.show()
        else:
            QtWidgets.QMessageBox.information(self.window.userIMG, "알림", "로그인을 해주세요")

    def getThumbnail(self):
        keyWord = "진돗개산책"
        url = requests.get("https://tv.naver.com/search/clip?query={}&sort=rel&page=1&isTag=false".format(keyWord))
        req = url.text
        soup = BeautifulSoup(req, "html.parser")

        thumb = soup.select(
            'div.cds_area > div.thl > div.thl_a > a '
        )
        tempthumb = ''
        for i in range (3):
            tempthumb = thumb[i].find("img")["src"]
            urllib.request.urlretrieve(tempthumb, "C:\\Users\\Public\\" + str(i) + ".jpg")
        self.makeThumbnail()

    def makeThumbnail(self):
        self.window.thumbNail1.setText("")
        self.window.thumbNail1.setStyleSheet("background-color: rgb(255, 230, 153);\n"
        "border-radius: 20px;\n"
        "background-image: url('C:/Users/Public/0.jpg');")
        self.window.thumbNail2.setText("")
        self.window.thumbNail2.setStyleSheet("background-color: rgb(255, 230, 153);\n"
        "border-radius: 20px;\n"
        "background-image: url('C:/Users/Public/1.jpg');")
        self.window.thumbnail3.setText("")
        self.window.thumbnail3.setStyleSheet("background-color: rgb(255, 230, 153);\n"
        "border-radius: 20px;\n"
        "background-image: url('C:/Users/Public/2.jpg');")

    def goPage(self, pageNum): 
        if pageNum == 0 or self.userdb.checkUser(self.window.loginNout):
            self.window.menupage.setCurrentIndex(pageNum)
        else:
            QtWidgets.QMessageBox.information(self.window.menupage, "알림", "로그인을 해주세요")
            return 0
        if pageNum == 0:
            self.window.home.setStyleSheet("QPushButton{\n"
            "background-color: rgb(217, 217, 217);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")
            self.window.findingFriend.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")        
            self.window.findingHospital.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")        
            self.window.purchasingFood.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")
        elif pageNum == 1:
            
            self.window.home.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")
            self.window.findingFriend.setStyleSheet("QPushButton{\n"
            "background-color: rgb(217, 217, 217);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")        
            self.window.findingHospital.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"           
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")       
            self.window.purchasingFood.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")
        elif pageNum == 2:
            
            self.window.home.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")    
            self.window.findingFriend.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")        
            self.window.findingHospital.setStyleSheet("QPushButton{\n"
            "background-color: rgb(217, 217, 217);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")        
            self.window.purchasingFood.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")
        elif pageNum == 3:
            
            self.window.home.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")
            self.window.findingFriend.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"       
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"  
            "}")        
            self.window.findingHospital.setStyleSheet("QPushButton{\n"
            "background-color: rgb(255, 230, 153);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")        
            self.window.purchasingFood.setStyleSheet("QPushButton{\n"
            "background-color: rgb(217, 217, 217);\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(197, 197, 197);\n"
            "}")

    def idCheck(self):
        if self.userdb.idChecking(self.userPopup.idInput.text()):
            QtWidgets.QMessageBox.information(self.userPopup.idCheck, "알림", "ID 사용가능!!")
        else:
            QtWidgets.QMessageBox.information(self.userPopup.idCheck, "알림", "ID 사용불가!!")
                 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = petcal.Ui_mainwindow()
    mainwindow.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint)
    ui.setupUi(mainwindow)
    ###userDatapopup
    usermainFrame = QtWidgets.QWidget()
    userData = signup_popup.Ui_mainFrame()
    userData.setupUi(usermainFrame)
    usermainFrame.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ###foodedit
    foodmainFrame = QtWidgets.QWidget()
    userfood = foodedit.Ui_foodmainFrame()
    userfood.setupUi(foodmainFrame)
    foodmainFrame.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ###foodwarn
    foodWarnmainFrame = QtWidgets.QWidget()
    foodWarn = food_warn_popup.Ui_mainFrame()
    foodWarn.setupUi(foodWarnmainFrame)
    foodWarnmainFrame.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ###schedulepopup
    schedulemainFrame = QtWidgets.QWidget()
    schedule = schedule_popup.Ui_mainFrame()
    schedule.setupUi(schedulemainFrame)
    schedulemainFrame.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ###changeimg
    changeimgmainFrame = QtWidgets.QWidget()
    changeimg = changeimg.Ui_mainFrame()
    changeimg.setupUi(changeimgmainFrame)
    changeimgmainFrame.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    
    main = mainClass(ui)

    mainwindow.show()
    sys.exit(app.exec_())