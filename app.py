from flask import Flask, app, render_template,request, jsonify
from flask.helpers import send_from_directory, url_for
from werkzeug.utils import redirect, secure_filename
import os
app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'
@app.route('/test', methods=['GET','POST'])
def test():
    if request.method =='POST':
        task_content = request.form['inpFile']
        print(task_content)
        return f"<html><body>{ task_content }</body></html>"
    else:
        return render_template('test.html')

@app.route("/upload", methods=['POST'])
def upme():
    video = request.files.get('video')
    if video: 
        print(video)
        video.save(os.path.join(os.getcwd(), "vid/video.mp4"))
       # process the file object here! 

        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method =='POST':
        uploaded_file = request.form

        print(request)
        print(uploaded_file)

    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == '__main__':
    app.run(debug=True)