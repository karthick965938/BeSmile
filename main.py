from flask import Flask, render_template, Response, request, json, redirect, url_for
from threading import Timer
from camera import VideoCamera
from datetime import datetime
import webbrowser
import os
import csv

app = Flask(__name__)
user_detail_file = os.path.dirname(os.path.realpath(__file__))

@app.route('/')
def index():
  user = os.environ['USER'].title()
  if os.path.exists(user_detail_file+"/user_details.txt"):
    return render_template('home.html', **locals())
  else:
    return render_template('index.html', **locals())

@app.route('/userDetailStore', methods=['POST'])
def userDetailStore():
  email =  request.form['email'];
  if os.path.exists(user_detail_file+"/user_details.txt"):
    f = open("user_details.txt", "a")
    f.write(email)
    f.close()
  else:
    f = open("user_details.txt", "wt")
    f.write(email)
    f.close()
  return redirect("/")

@app.route('/emotion_count', methods=['GET'])
def getEmotionCount():
  # file  = open('emotion_details.csv', "r")
  # a = {'Angry' : 0, 'Disgust' : 0, 'Fear' : 0, 'Happy' : 0, 'Sad' : 0, 'Surprise' : 0, 'Neutral' : 0, 'NoFace' : 0, 'Discussion' : 0 }
  # read = csv.reader(file)
  # for i, row in enumerate(read):
  #   if row[0] in a:
  #     a[row[0]] += 1
  # return str(a)

  # get it from the db
# get the reports
@app.route('/reports')
def report():
  return render_template('report.html', **locals())

# Init webcam feed
def gen(camera):
  while True:
    frame = camera.get_frame()
    yield (b'--frame\r\n'
      b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Show webcam feed
@app.route('/video_feed')
def video_feed():
  return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

# Init the browser open after the app start
def open_browser():
  webbrowser.open_new('http://127.0.0.1:2000/')

# start the FLASK app, and open ther browser
if __name__ == "__main__":
  Timer(1, open_browser).start();
  app.run(port=2000)