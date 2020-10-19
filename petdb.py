import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import calendar
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import time
import urllib

class userData:
    def __init__(self):
        self.conn = sqlite3.connect("pet_user.db")
        self.cur = self.conn.cursor()
        self.inputid = True

    # cur.execute("CREATE TABLE useridpw (id TEXT, pw TEXT)")
    # cur.execute("CREATE TABLE userinfo (id TEXT, img BLOB, address TEXT, email TEXT, food TEXT)")
    ### edittingPhoto
    def convertToBinaryData(self, fileName):
        with open(fileName, 'rb') as file:
            blobData = file.read()
        return blobData

    def insertPhoto(self, userid, fileName):
        conPhoto = self.convertToBinaryData(fileName)
        self.cur.execute("UPDATE userinfo SET img = (?) WHERE id == (?)", (conPhoto, userid))
        
        self.conn.commit()
        # return conPhoto

    # def showPhoto(self, id, photo, openPath):
    #     self.cur.execute("SELECT img FROM userinfo WHERE id == (?)", (id, ))
    #     with open(openPath, 'wb') as file:
    #         file.write(photo)

    #     self.conn.commit()

    def showImg(self, page, id):
        self.cur.execute("SELECT img FROM userinfo WHERE id == (?)", (id, ))
        img = QtGui.QPixmap()
        img.loadFromData(self.cur.fetchall()[0][0])
        page.userIMG.setPixmap(img)
        page.userIMG.setScaledContents(True)

    # def inputComm(self):
    #     fileName = input("파일경로")
    #     newfileName = input("뉴파일경로")
    #     userid = input("id 입력")
    #     photo = self.insertPhoto(userid, fileName)
        # self.showPhoto(userid, photo, newfileName)
        # self.cur.close()

    def getImgPath(self, path, page, id):
        self.insertPhoto(id, path)
        self.showImg(page, id)

    def signup(self, page):
        userId = str(page.idInput.text())
        if userId != self.inputid or self.inputid == True:
            QtWidgets.QMessageBox.information(page.confirm, "알림", "ID 중복확인이 필요합니다!!")
            return 0
        userPw = str(page.passwordInput.text())
        userLocation = str(page.locationInput.text())
        userEmail = str(page.emailInput.text())
        if len(userLocation) == 0 | len(userEmail) == 0:
            QtWidgets.QMessageBox.information(page.confirm, "알림", "거주지와 이메일을 입력해주세요!!")
            return 0
        if self.checkSpace(userId, userPw):
            QtWidgets.QMessageBox.information(page.confirm, "알림", "회원가입완료!!")
        else:
            QtWidgets.QMessageBox.information(page.confirm, "알림", "id나 pw에 공백포함 불가!!")
            return 0

        self.cur.execute("INSERT INTO userinfo (id, location, email) VALUES (?, ?, ?)", (userId, userLocation, userEmail))
        self.cur.execute("INSERT INTO useridpw (id, pw) VALUES (?, ?)", (userId, userPw))
        self.cur.execute("INSERT INTO userfood (id) VALUES (?)", (userId, ))
        self.cur.execute("INSERT INTO schedule (id) VALUES (?)", (userId, ))
        self.conn.commit()

    def checkSpace(self, id, pw):
        if id.strip() == '':
            return False
        if pw.strip() == '':
            return False
        userid = id.split(' ')
        pw = pw.split(' ')
        if len(userid) == 1:
            if len(pw) == 1:
                return True
        
        return False

    def idChecking(self, userid):
        self.cur.execute("SELECT id FROM useridpw WHERE id == (?)", (userid,))
        if self.cur.fetchall() ==[]:
            if self.checkSpace(userid, 'pass'):
                self.inputid = userid
                return True
        
        return False

    def loginCheck(self, id, pw):
        self.cur.execute("SELECT * FROM useridpw WHERE id == (?)", (id, ))
        if self.cur.fetchall() == []:
            return False
        self.cur.execute("SELECT * FROM useridpw WHERE id == (?)", (id, ))
        if pw == self.cur.fetchall()[0][1]:
            return True
        
        return False

    def showId(self, page, id):
        self.cur.execute("SELECT id FROM useridpw WHERE id == (?)", (id, ))
        page.showid.setText(self.cur.fetchall()[0][0])

    def __str__(self):
        self.cur.close()

    def checkUser(self, page):
        if page.currentIndex() == 1:
            return True
        return False

    def isFoodOk(self, id):
        self.cur.execute("SELECT foodname FROM userfood WHERE id == (?)", (id, ))
        if self.cur.fetchall() != [(None, )]:
            self.cur.execute("SELECT * FROM userfood WHERE id == (?)", (id, ))
            food = self.cur.fetchall()[0]
            left = food[2] - food[3]
            if left*10 < food[2]:
                return False

        return True

    def userFood(self, id, page, wholefood, foodeating, dayeating, foodname):
        self.cur.execute("SELECT id FROM userfood WHERE id == (?)", (id, ))
        if self.cur.fetchall() == []:
            self.cur.execute("INSERT INTO userfood VALUES (?, ?, ?, ?, ?)",\
            (id, foodname, wholefood, foodeating, dayeating))
            self.conn.commit()
        else:
            self.cur.execute("UPDATE userfood SET foodname = (?), wholefood = (?), eatfood = (?), dayfood = (?) WHERE id == (?)",\
                (foodname, wholefood, foodeating, dayeating, id))
            self.conn.commit()
        left = str(round(wholefood - foodeating, 2))
        page.leftFoodData.setText(left)
    
    def setData(self, page, id):
        self.cur.execute("SELECT foodname FROM userfood WHERE id == (?)", (id, ))
        # print(self.cur.fetchall()[0])
        if self.cur.fetchall()[0][0] != None:
            self.setFood(page, id)
        self.cur.execute("SELECT img FROM userinfo WHERE id == (?)", (id, ))
        if self.cur.fetchall() != [(None,)]:
            self.showImg(page, id)
        self.cur.execute("SELECT location FROM userinfo WHERE id == (?)", (id, ))
        location = self.cur.fetchall()[0][0]
        page.title.setText(location + " 친구 찾기")
        page.hospitalTitle.setText(location + " 병원 찾기")
    
    def setSchedule(self, page,  table, id):
        self.cur.execute("SELECT date, note FROM schedule WHERE id == (?)", (id, ))
        scheduleList = self.cur.fetchall()
        table.setRowCount(len(scheduleList))
        for i in range (len(scheduleList)):
            for row in range (2):
                table.setItem(i, row, QtWidgets.QTableWidgetItem(scheduleList[i][row]))
        scheduleString = ''
        for i in range (len(scheduleList)):
            for row in range (2):
                scheduleString = scheduleString + str(scheduleList[i][row]) + "\n" 
        page.schedule.setText(scheduleString)

    def setFoodPopup(self, popup, id):
        self.cur.execute("SELECT foodname FROM userfood WHERE id == (?)", (id, ))
        if self.cur.fetchall() != [(None, )]:
            self.cur.execute("SELECT * FROM userfood WHERE id == (?)", (id, ))
            food = self.cur.fetchall()[0]
            popup.wholeFoodInput.setText(str(food[2]))
            popup.FoodEatingInput.setText(str(food[3]))
            popup.leftFoodData.setText(str(food[2] - food[3]))
            popup.dayEatingInput.setText(str(food[4]))
            popup.foodNameInput.setText(food[1])

    def setFood(self, page, id):
        self.cur.execute("SELECT * FROM userfood WHERE id == (?)", (id, ))
        data = self.cur.fetchall()[0]
        left = round(data[2] - data[3], 2)
        page.wholeFoodData.setText(str(data[2]))
        page.eatFoodData.setText(str(data[3]))
        page.leftFoodData.setText(str(left))

        day = int(left//data[4])
        estimatePurchase = 0
        today = str(datetime.date.today())
        today = today.split('-')
        year = int(today[0])
        month = int(today[1])
        todayDay = int(today[2])
        while True:
            thisMonth = calendar.monthrange(year, month)
            if month == int(today[1]):
                leftDay = thisMonth[1] - todayDay
            else:
                leftDay = thisMonth[1]

            if day <= leftDay:
                if month != int(today[1]):
                    estimatePurchase = day
                    break
                estimatePurchase = int(today[2]) + day
                break
            else:
                day -= leftDay
                if month != 12:
                    month += 1
                else:
                    year += 1
                    month = 1

        purchaseData = str(year) + "년 " + str(month) + "월 " + \
            str(estimatePurchase) + "일"
        page.purchaseDayData.setText(purchaseData)

    def resetData(self, page):
        page.wholeFoodData.setText('')
        page.eatFoodData.setText('')
        page.leftFoodData.setText('')
        page.purchaseDayData.setText('')
        page.schedule.setText('')
        img = QtGui.QPixmap()
        img.loadFromData(None)
        page.userIMG.setPixmap(img)
        page.userIMG.setScaledContents(True)

    def setFriend(self, page, id, Count):
        self.cur.execute("SELECT location FROM userinfo WHERE id == (?)", (id, ))
        location = self.cur.fetchall()[0][0]
        self.cur.execute("SELECT * FROM userinfo WHERE id != (?) AND location == (?)", (id, location))
        friendList = self.cur.fetchall()
        friendCount = len(friendList)
        pageCount = friendCount//4
        if Count > pageCount:
            return pageCount
        elif Count == pageCount and friendCount%4 == 0:
            return pageCount
        lastPage = friendCount - pageCount*4
        if pageCount - Count > 0:
            i = Count
            i = i*4
            page.memberId1.setText(friendList[i][0])
            page.memberEmail1.setText(friendList[i][2])
            page.memberLocation1.setText(friendList[i][1])
            page.memberId2.setText(friendList[i + 1][0])
            page.memberEmail2.setText(friendList[i + 1][2])
            page.memberLocation2.setText(friendList[i + 1][1])
            page.memberId3.setText(friendList[i + 2][0])
            page.memberEmail3.setText(friendList[i + 2][2])
            page.memberLocation3.setText(friendList[i + 2][1])
            page.memberId4.setText(friendList[i + 3][0])
            page.memberEmail4.setText(friendList[i + 3][2])
            page.memberLocation4.setText(friendList[i + 3][1])
            self.setFriendImg(i, page, friendList)
 
        if pageCount - Count == 0:
            i = pageCount*4
            img = QtGui.QPixmap()
            if lastPage >= 1:
                page.memberId1.setText(friendList[i][0])
                page.memberEmail1.setText(friendList[i][2])
                page.memberLocation1.setText(friendList[i][1])
                img.loadFromData(friendList[i][3])
                page.memberIMG1.setPixmap(img)
                page.memberIMG1.setScaledContents(True)
                img = QtGui.QPixmap()
                img.loadFromData(None)
                page.memberIMG2.setPixmap(img)
                page.memberIMG2.setScaledContents(True)
                page.memberId2.setText("")
                page.memberEmail2.setText("")
                page.memberLocation2.setText("")
                page.memberId3.setText("")
                page.memberEmail3.setText("")
                page.memberLocation3.setText("")
                page.memberIMG3.setPixmap(img)
                page.memberIMG3.setScaledContents(True)
                page.memberId4.setText("")
                page.memberEmail4.setText("")
                page.memberLocation4.setText("")
                page.memberIMG4.setPixmap(img)
                page.memberIMG4.setScaledContents(True)                             
            if lastPage >= 2:
                page.memberId2.setText(friendList[i + 1][0])
                page.memberEmail2.setText(friendList[i + 1][2])
                page.memberLocation2.setText(friendList[i + 1][1])
                img.loadFromData(friendList[i + 1][3])
                page.memberIMG2.setPixmap(img)
                page.memberIMG2.setScaledContents(True)
                img = QtGui.QPixmap()
                img.loadFromData(None)
                page.memberId3.setText("")
                page.memberEmail3.setText("")
                page.memberLocation3.setText("")
                page.memberIMG3.setPixmap(img)
                page.memberIMG3.setScaledContents(True)
                page.memberId4.setText("")
                page.memberEmail4.setText("")
                page.memberLocation4.setText("")
                page.memberIMG4.setPixmap(img)
                page.memberIMG4.setScaledContents(True)    
            if lastPage >= 3:
                page.memberId3.setText(friendList[i + 2][0])
                page.memberEmail3.setText(friendList[i + 2][2])
                page.memberLocation3.setText(friendList[i + 2][1])
                img.loadFromData(friendList[i + 2][3])
                page.memberIMG3.setPixmap(img)
                page.memberIMG3.setScaledContents(True)
                img = QtGui.QPixmap()
                img.loadFromData(None)
                page.memberId4.setText("")
                page.memberEmail4.setText("")
                page.memberLocation4.setText("")
                page.memberIMG4.setPixmap(img)
                page.memberIMG4.setScaledContents(True) 
    
    def setFriendImg(self, i, page, friendList):
        img = QtGui.QPixmap()
        img.loadFromData(friendList[i][3])
        page.memberIMG1.setPixmap(img)
        page.memberIMG1.setScaledContents(True)
        img.loadFromData(friendList[i + 1][3])
        page.memberIMG2.setPixmap(img)
        page.memberIMG2.setScaledContents(True)
        img.loadFromData(friendList[i + 2][3])
        page.memberIMG3.setPixmap(img)
        page.memberIMG3.setScaledContents(True)
        img.loadFromData(friendList[i + 3][3])
        page.memberIMG4.setPixmap(img)
        page.memberIMG4.setScaledContents(True)

    def saveSchedule(self, id, table, row):
        self.cur.execute("DELETE FROM schedule WHERE id == (?)", (id, ))
        scheduleList = []
        for i in range (row):
            if table.item(i, 0) == None:
                row = i + 1
                break
            scheduleList.append([])
            for column in range (2):
                scheduleList[i].append(table.item(i, column).text())
        for i in range (row):
            self.cur.execute("INSERT INTO schedule VALUES (?, ?, ?)", \
                (id, scheduleList[i][0], scheduleList[i][1]))
        
        self.conn.commit()

    def getLocation(self, id):
        self.cur.execute("SELECT location FROM userinfo WHERE id == (?)", (id, ))
        location = str(self.cur.fetchall()[0][0])
        return location

    def getFoodName(self, id):
        self.cur.execute("SELECT foodname FROM userfood WHERE id == (?)", (id,))
        foodname = self.cur.fetchall()[0][0]
        if foodname == None:
            return False
        return str(foodname)

    def showSchedule(self, id):
        self.cur.execute("SELECT date FROM schedule WHERE id == (?)", (id, ))
        scheduleList = self.cur.fetchall()
        return scheduleList