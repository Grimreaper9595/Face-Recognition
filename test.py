import pyrebase
import storage as storage
from numpy import var

#Test to connect with Firebase
firebaseConfig = {
    "apiKey": "Your API key",
    "authDomain": "auth url",
    "databaseURL": "firebase URL",
    "projectId": "Your Project id",
    "storageBucket": "StorageBucket link",
    "messagingSenderId": "id",
    "appId": "Your app id"
}
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

#Test: Save file to database/firebase
filename = input("enter the name of file")
cloudfilename = input("asda")

storage.child(cloudfilename).put(filename)