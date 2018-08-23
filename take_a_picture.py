import pyrebase
from uuid import uuid1

# import picamera
#
#
# def take_a_picture(photo):
#     with picamera.PiCamera() as photo:
#         photo.start_preview()
#         photo.capture('picture.jpg')
#         photo.stop_preview()
#         photo.close()


config = {
    'apiKey': "AIzaSyDQUUngWHg4wRG7RN1keEJNd77QNYVA6lI",
    'authDomain': "kleider-40b8e.firebaseapp.com",
    'databaseURL': "https://kleider-40b8e.firebaseio.com",
    'projectId': "kleider-40b8e",
    'storageBucket': "kleider-40b8e.appspot.com",
    'messagingSenderId': "793580625707"
}

db = pyrebase.initialize_app(config)
database = db.database()
auth = db.auth()
user = auth.sign_in_with_email_and_password('tintoogmp@gmail.com', 'thiago55')
storage = db.storage()


def call_db_user():
    retorno = storage.child('image/{}/{}.jpg'.format(user['localId'], uuid1())).put('bard.jpg')
    # instructions = database.child("instruction/forJHq8WWbfqa4VbHrUlBTotQkr1").get(user['idToken']).val()['takePhoto']
    print(retorno)


def stream_handler(message):
    print(message["path"])
    # print(message["data"])  # {'title': 'Pyrebase', "body": "etc..."}
    call_db_user()


my_stream = database.child("instruction/".format(user['localId'])).stream(stream_handler)
