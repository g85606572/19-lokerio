from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('firebase-adminsdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://lokerio-66f3f.firebaseio.com/'
})
