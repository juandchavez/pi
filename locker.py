import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
import time
from datetime import date
import logging


class locker_system:
    # config = {
    #     "apiKey": "AIzaSyCMxHjpqF1nSyPqXMrtvtCtkhE_41yy4uQ",
    #     "authDomain": "senior-project-c7714.firebaseapp.com",
    #     "databaseURL": "https://senior-project-c7714-default-rtdb.firebaseio.com/",
    #     "storageBucket": "senior-project-c7714.appspot.com"
    # }
    # TODO: Abstract this outside of the class
    config = "./fb_key/senior-project-c7714-firebase-adminsdk-jdiyj-73f126782d.json"
    firebase = None
    cred = None
    db = None
    logging.basicConfig(level=logging.INFO)

    def __init__(self) -> None:

        self.cred = credentials.Certificate(self.config)
        self.firebase = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        pass

    def useLocker(self, locker, user):
        # doc_ref = self.db.collection(u'users').document(
        #     u'alovelace')
        # doc_ref.set({
        #     u'first': u'Ada',
        #     u'last': u'Lovelace',
        #     u'born': 1815
        # })
        logging.info("Using Locker...")
        if (self.isLockerInUse(locker, user)):
            if (self.isLockerLockedByUser(locker, user)):
                logging.info("Unlocking Locker")
                self.unlockLocker(locker, user)
                return "Locker unlocked"
            else:
                logging.info("Locker does not belong to user")
                return "Locker does not belong to you"
        else:
            logging.info("Locking locker")
            if (self.isLockerClosed(locker)):
                self.lockLocker(locker, user)
                return "Locker locked"
            else:
                return "Locker is not able to lock at the moment. Make sure to close the locker."

    def lockLocker(self, locker, user):
        logging.info("Locking locker")
        doc_ref = self.db.collection('Lockers').document(
            f'{locker}')
        doc_ref.update({
            u'currentUser': f'{user}',
            u'status': u'in_use',
            u'last_modified': datetime.datetime.now()
        })

    def unlockLocker(self, locker, user):
        logging.info("Unlocking locker")
        doc_ref = self.db.collection('Lockers').document(
            f'{locker}')
        doc_ref.update({
            u'currentUser': f'{user}',
            u'status': u'open',
            u'last_modified': datetime.datetime.now()
        })

    def closeLocker(self, locker):
        logging.info("Locker closed")
        doc_ref = self.db.collection('Lockers').document(
            f'{locker}')
        doc_ref.update({
            u'state_of_locker_door': u'close',
        })

    def openLocker(self, locker):
        logging.info("Locker open")
        doc_ref = self.db.collection('Lockers').document(
            f'{locker}')
        doc_ref.update({
            u'state_of_locker_door': u'open',
            u'currentUser': None,
        })

    def isLockerClosed(self, locker):
        logging.info("Check if locker door is closed.")
        doc_ref = self.db.collection(u'Lockers').document(f'{locker}')
        doc = doc_ref.get()
        if doc.exists:
            locker_attributes = doc.to_dict()
            if (locker_attributes.get('state_of_locker_door') == "open"):
                logging.info("Locker is not closed")
                return False
            else:
                logging.info("Locker is closed")
                return True
        else:
            logging.warn("Locker is not registered")
            return False

    def isLockerLockedByUser(self, locker, user):
        doc_ref = self.db.collection(u'Lockers').document(f'{locker}')
        doc = doc_ref.get()
        if doc.exists:
            locker_attributes = doc.to_dict()
            if (locker_attributes.get('status') == "in_use"):
                if (locker_attributes.get('currentUser') == user):
                    return True
                else:
                    logging.info("This is not the user's locker")
                    return False
            else:
                logging.info("Locker is no longer in use by any user")
                return False
        else:
            logging.warn("Locker is not registered")
            return False

    def isLockerInUse(self, locker, user):
        doc_ref = self.db.collection(u'Lockers').document(f'{locker}')
        doc = doc_ref.get()
        if doc.exists:
            locker_attributes = doc.to_dict()
            if (locker_attributes.get('status') != "open"):
                return True
            else:
                return False
        else:
            logging.warn("Locker is not registered")
            return False

    def defaultBreached(self, locker):
        doc_ref = self.db.collection(u'Lockers').document(f'{locker}')
        doc = doc_ref.get()
        if doc.exists:
            return True
        else:
            logging.warn("Locker is not registered")
            return False
