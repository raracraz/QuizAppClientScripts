# StudentID:	p2104089
# Name:	AAI XUN EN
# Class:		DISM/FT/1B/05   
# Assessment:	CA1 / CA2
# 
# Script name:	user.py
# 
# Purpose:	script to handle user login, register and forget password. Also to allow user to take quiz and view past results.
#
# Usage syntax:	Run with play button, press f5 to run
# 
# Input file:	jsonPython/db/...
# 
# Output file:	jsonPython/db/...
# 
# Python ver:	Python 3
#
#################################################################################
#                               Import Libraries                                #
#################################################################################
import os
import re
import base64
import datetime
import time
import uuid
import getpass
import base64
import socket as s
import json
#############################################################################
#                               functions                                   #
#############################################################################
#

def receiveParser(data):
    try:
        jsonData = json.loads(data)
        return jsonData
    except:
        print("Error: Server data is not in JSON format")
        return False

def formatParser(menuid, theMessage, minLength=1,maxLength=512,minVal=1,maxVal=99):
    jsonStr = {'menuid': menuid, 'message': theMessage, 'minLength': minLength, 'maxLength': maxLength, 'minVal': minVal, 'maxVal': maxVal,}
    return json.dumps(jsonStr)
#############################################################################
#                                 menu                                      #
#############################################################################
# open connection to server using socket
try:
    s = s.socket(s.AF_INET, s.SOCK_STREAM)
    s.connect(('localhost', 3000))
    #Purpose of this lambda function is to clear terminal after each input
    clearConsole = lambda: os.system('cls')

    #this is the main menu of the quiz app
    #purpose of this menu is to provide the user with a menu to choose from

    #open connection to server using socket

    while True:
        receive_data = s.recv(1024).decode()
        try:
            jsonData = receiveParser(receive_data)
            displayMessage = jsonData['message']
            displayPrompt = jsonData['prompt']
            menuid = jsonData['menuid']
            MessageType = jsonData['type']
            
            theMessage = input(displayMessage+"\n"+displayPrompt)
        
            if theMessage == '':
                menuid = 0
                theMessage = '0'

            if theMessage == 'exit':
                break
            if MessageType == 'text':
                menuid = theMessage

            if MessageType == 'email':
                # use re to check if email is valid
                if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', theMessage):
                    print("Error: Email is not valid")
                    menuid = 0
                    theMessage = '0'
                    continue
                else:
                    pass
            
            


                
            s.send(formatParser(menuid, theMessage).encode())
        except:
            print("Error: Serverrr data is not in JSON format")
except:
    print("Error: cannot connect to server")
    s.close()