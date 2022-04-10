# Ajnur Bogucanin | Graficari | for HackAtHome2022

# util.py is going to be used for summing up all the tools that I need to make
# in one place, so i can call them all from here which makes code much more readable.

#IMPORTS
from firebase_admin import credentials  #Credentials for Firebase
from firebase_admin import db           #RT_Database from Firebase
import firebase_admin                   #Firebase admin
import arduino as ard                   #Importing so we can use functions from arduino.py

#VARS
#Firebase Credentials and Database access
cred = credentials.Certificate("creds/cred.json")
firebase_admin = firebase_admin.initialize_app(cred, {'databaseURL': 'https://ticketsa-26792-default-rtdb.europe-west1.firebasedatabase.app/'})

#MAIN

#Function that pulls ticket status of the event from DB
def getTicketData(eventName, userID):
    path = 'users/'+userID+'/ticket_data/'+eventName
    ref = db.reference(path)
    return ref.get()

#Function that pulls Username of the user from DB
def pullUserName(userID):
    path = str('users/{}/info/name'.format(str(userID)))
    ref = db.reference(path)
    return ref.get()


