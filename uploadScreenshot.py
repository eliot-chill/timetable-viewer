#!/usr/bin/python3
import ftpAPI
import ftplib
import login

login.getFrameSourceAnywhere("","")

apiKey = ftpAPI.getKey('/home/eliot/timetable-viewer/client_secret.txt')
packageID = ftpAPI.getPackageID(apiKey, "eliotchill.com")
ftpAPI.toggleFTP(apiKey, "eliotchill.com", packageID, True)
ftpSession = ftplib.FTP('', '', '')
for i in range(4):
    screenshot = open(f'timetable{i}.png','rb')                  # file to send
    ftpSession.storbinary(f'STOR timetable{i}.png', screenshot)     # send the file
    screenshot.close()
ftpAPI.toggleFTP(apiKey, "eliotchill.com", packageID, False)
