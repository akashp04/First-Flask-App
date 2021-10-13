from flask import Flask, app, config, render_template,request, jsonify
from flask.helpers import send_from_directory, url_for
from werkzeug.utils import redirect, secure_filename
import os
import pyrebase 
import cv2

config = {
    "apiKey": "AIzaSyCNrp3TU-Ue2SFssJH489qmpMrjXhu7sYw",
    "authDomain": "flask-test-firebase.firebaseapp.com",
    "projectId": "flask-test-firebase",
    "storageBucket": "flask-test-firebase.appspot.com",
    "messagingSenderId": "890677906619",
    "appId": "1:890677906619:web:5a55c2532fff5f9efb6d9e",
    "measurementId": "G-JMTEHX9D2D",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


def firebaseUpload(video):
    storage.child("Videos/Video Test.mp4").put(video)
# def firebaseDownload(filepath):
    
    
app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upme():
    video = request.files.get('video')
    if video: 
        print(video)    
        firebaseUpload(video)
        # video.save(os.path.join(os.getcwd(), "vid/video.mp4"))
        # process the file object here! 
        return redirect(url_for('test'))
        
        return jsonify(success=True)
    return jsonify(success=False)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    if True:
        links = storage.child("Videos/Video Test.mp4").get_url(None)
        print(links)
        return render_template('test.html', linkToVideo = links)
    return render_template('test.html')




if __name__ == '__main__':
    app.run(debug=True)
