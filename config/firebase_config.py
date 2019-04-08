import pyrebase
import firebase_admin
from firebase_admin import credentials

def firebase_connection():
    """
    Initiate instance of Firebase Access class

    :return: object of initiated Firebase object
    """

    # configure firedb
    config = {
    "apiKey": "AIzaSyAo1KBmwzdCvz-gXl88AsTtfwEEZ7OjQi4",
    "authDomain": "pit-street-sweeper.firebaseapp.com",
    "databaseURL": "https://pit-street-sweeper.firebaseio.com",
    "projectId": "pit-street-sweeper",
    "storageBucket": "pit-street-sweeper.appspot.com",
    "messagingSenderId": "1056333683675",
    "serviceAccount": "./credentials/serviceAccountCredentials.json"
    }

    # initialize firebase
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    return db