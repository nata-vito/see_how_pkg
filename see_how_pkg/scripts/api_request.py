import firebase_admin
from firebase import firebase
from firebase_admin import credentials
from firebase_admin import firestore

class FireRise:
    def __init__(self, url, data, service = None):
        self.url        = url
        self.data       = data
        self.service    = service
        self.firebase   = firebase.FirebaseApplication(url)

# firebase = firebase.FirebaseApplication("https://myhand-ff333-default-rtdb.firebaseio.com/")
    def putData(self, frame, isField, field = None, data = None):

        if isField:
            polegar   = self.firebase.put(f"/{frame}", 'polegar', data[0])
            indicador     = self.firebase.put(f"/{frame}", 'indicador', data[1])
            meio        = self.firebase.put(f"/{frame}", 'meio', data[2])
            anelar      = self.firebase.put(f"/{frame}", 'anelar', data[3])
            mindinho    = self.firebase.put(f"/{frame}", 'mindinho', data[4])
        else:
            put_api = self.firebase.put(f"/{frame}", f"{field}", data)

    def getData(self, frame, isField = False, field = None):
        if isField:
            path  = f"{frame}/{field}"
            result = firebase.get(self.url, path)
        else: 
            path = f"{frame}"
            result = firebase.get(self.url, path)        

        return result

""" 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection('hand').add({'thumb finger':1,
                            'index finger':1,
                            'middle finger':1,
                            'ringe finger':1,
                            'little finger':1}) """