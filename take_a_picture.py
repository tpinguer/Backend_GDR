import pyrebase

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


auth = db.auth()
user = auth.sign_in_with_email_and_password('tintoogmp@gmail.com', 'thiago55')
storage = db.storage()
storage.child('image/cloth.jpg').put('bard.jpg', user['idToken'])
print(user['localId'])
