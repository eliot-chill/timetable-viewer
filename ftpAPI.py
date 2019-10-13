#!/usr/bin/python3
from base64 import b64encode
import requests
import json

def getKey(filename):
    with open(filename) as reader: client_secret = reader.read().splitlines()[0] #Get API key from file, splitlines()[0] to avoid `\n` char
    return b64encode(client_secret.encode()).decode() #Encode then decode to return string, not byte object

def getPackageID(encKey, domain):
    authHeaders = {'Authorization':f'Bearer {encKey}'}
    generalPackageRe = requests.get('https://api.20i.com/package', headers=authHeaders)
    if generalPackageRe.ok:
        for packageObj in generalPackageRe.json():
            if(packageObj['name'] == domain):
                return packageObj['id']


def getCurrentIP():
    return requests.get('http://ifconfig.me').text

def toggleFTP(encKey, domain, packageID, unlock=True):
    authHeaders = {'Authorization':f'Bearer {encKey}'}
    ftpIDre = requests.get(f'https://api.20i.com/package/{packageID}/web/ftpusers', headers=authHeaders)
    if ftpIDre.ok:
        #print(ftpIDre.json())
        for ftpObj in ftpIDre.json():
            if(ftpObj['Username'] == "timetable@"+domain):
                ftpID = ftpObj['Id']
    if(unlock): 
        payload = {
                "update":{
                    "ftp": [
                        {
                            "id":ftpID,
                            "user":{
                                "Password":"",
                                "JailFrom":"/public_html/timetable",
                                "UnlockedUntil":None,
                                "Enabled":True
                                },
                            "acl":[
                                {
                                    "Ip4Address":getCurrentIP(),
                                    "Ip6Address":None
                                    }
                                ]}
                        ]}
                }
    else:
        payload = {
                "update":{
                    "ftp": [
                        {
                            "id":ftpID,
                            "user":{
                                "Password":"",
                                "JailFrom":"/public_html/timetable",
                                "UnlockedUntil":None,
                                "Enabled":True
                                },
                            "acl":"clear"
                            }]
                        }
                }
 
    openFTPre = requests.post(f'https://api.20i.com/package/{packageID}/web/ftpusers', headers=authHeaders, json=payload)
