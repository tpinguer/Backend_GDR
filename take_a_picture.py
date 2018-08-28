import pyrebase

config = {
    'apiKey': "AIzaSyDQUUngWHg4wRG7RN1keEJNd77QNYVA6lI",
    'authDomain': "kleider-40b8e.firebaseapp.com",
    'databaseURL': "https://kleider-40b8e.firebaseio.com",
    'projectId': "kleider-40b8e",
    'storageBucket': "kleider-40b8e.appspot.com",
    'messagingSenderId': "793580625707"
}

firebase = pyrebase.initialize_app(config)
user = firebase.auth().sign_in_with_email_and_password('guimili@live.com', 'leo123')
storage = firebase.storage()
database = firebase.database()


def stream_handler(message):
    if len(message['path']) > 1:
        if message['data'] == True or message['data']['takePhoto'] == True:
            column = message['path'].split('/')[1]
            key = database.child('photo').child(column).push({'url': ''}, user['idToken'])['name']
            token = storage.child('images/{}/{}.jpg'.format(column, key)).put('bard.jpg', user['idToken'])['downloadTokens']
            url_save = storage.child('images/{}/{}.jpg'.format(column, key)).get_url(token)
            database.child('photo').child(column).child(key).update({'url': url_save}, user['idToken'])
            database.child('instruction').child(column).update({'takePhoto': False}, user['idToken'])


my_stream = database.child("instruction").stream(stream_handler, stream_id='instruction')

# {'name': 'images/2sMO82ugagWNwDibbslEQwRGsUr1.jpg', 'bucket': 'kleider-40b8e.appspot.com', 'generation': '1535155400016363', 'metageneration': '1', 'contentType': 'image/jpeg', 'timeCreated': '2018-08-25T00:03:20.016Z', 'updated': '2018-08-25T00:03:20.016Z', 'storageClass': 'STANDARD', 'size': '86241', 'md5Hash': 'kAlpjC16JQ2aFQxY5jOxig==', 'contentEncoding': 'identity', 'contentDisposition': "inline; filename*=utf-8''2sMO82ugagWNwDibbslEQwRGsUr1.jpg", 'crc32c': 'RKE6uQ==', 'etag': 'COuDrMLzht0CEAE=', 'downloadTokens': '281ad3f5-9662-4b4e-8fd7-f3b8b49667f2'}
