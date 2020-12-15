from flask import Flask, render_template, Response, request, json, redirect, url_for
from camera import VideoCamera
from joke import jokes
from datetime import datetime
from flask_apscheduler import APScheduler
import os
import sqlite3 as sql
import notify2
import random
import jaydebeapi
import sys

argv = sys.argv

multicast_address = argv[1] # default : 239.0.0.1
port_no = argv[2] # default : 41999
cluster_name = argv[3]
username = argv[4]
password = argv[5]

url = "jdbc:gs://" + multicast_address + ":" + port_no + "/" + cluster_name
conn = jaydebeapi.connect("com.toshiba.mwcloud.gs.sql.Driver", url, [username, password], "./gridstore-jdbc.jar")

app = Flask(__name__)

def get_user_data():
  cur = conn.cursor()
  cur.execute("SELECT * from User")
  user = cur.fetchall();
  if len(user) > 0 :
    return True
  return False

#function executed by scheduled job
def show_joke(text):
  if get_user_data():
    notify2.init('BeSmile')
    n = notify2.Notification('Joke From BeSmile', random.choice(jokes))
    n.timeout=20000
    n.show()

@app.route('/')
def index():
  username = os.environ['USER'].title()
  if get_user_data():
    title = 'BeSmile-Home'
    return render_template('home.html', **locals())
  else:
    title = 'BeSmile'
    return render_template('index.html', **locals())

@app.route('/userDetailStore', methods=['POST'])
def userDetailStore():
  email =  request.form['email'];
  time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
  try:
    cur = conn.cursor()
    cur.execute("INSERT INTO User (email_address,created_at) VALUES (?,?)",(email, time))
    con.commit()
  except:
    con.rollback()
  finally:
    con.close()
  return redirect("/")

@app.route('/emotion_count', methods=['POST'])
def getEmotionCount():
  user = os.environ['USER'].title()
  date = datetime.now().strftime("%d-%m-%Y")
  neutral = conn.cursor()
  neutral.execute("SELECT name FROM emotions WHERE name=? AND create_date=?", ('Neutral', (request.form['data'], date)[request.form['data'] == 'today']))
  neutral_count = neutral.fetchall()
  happy = conn.cursor()
  happy.execute("SELECT name FROM emotions WHERE name=? AND create_date=?", ('Happy', (request.form['data'], date)[request.form['data'] == 'today']))
  happy_count = happy.fetchall()
  sad = conn.cursor()
  sad.execute("SELECT name FROM emotions WHERE name=? AND create_date=?", ('Sad', (request.form['data'], date)[request.form['data'] == 'today']))
  sad_count = sad.fetchall()
  angry = conn.cursor()
  angry.execute("SELECT name FROM emotions WHERE name=? AND create_date=?", ('Angry', (request.form['data'], date)[request.form['data'] == 'today']))
  angry_count = angry.fetchall()
  fear = conn.cursor()
  fear.execute("SELECT name FROM emotions WHERE name=? AND create_date=?", ('Fear', (request.form['data'], date)[request.form['data'] == 'today']))
  fear_count = fear.fetchall()
  surprise = conn.cursor()
  surprise.execute("SELECT name FROM emotions WHERE name=? AND create_date=?", ('Surprise', (request.form['data'], date)[request.form['data'] == 'today']))
  surprise_count = surprise.fetchall()
  return json.dumps({'Neutral':len(neutral_count), 'Happy':len(happy_count), 'Sad':len(sad_count), 'Angry':len(angry_count), 'Fear':len(fear_count), 'Surprise':len(surprise_count)});

def gen(camera):
  while True:
    frame = camera.get_frame()
    yield (b'--frame\r\n'
      b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
  return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
  scheduler = APScheduler()
  scheduler.add_job(func=show_joke, args=['Joke Start'], trigger='interval', id='job', seconds=600)
  scheduler.start()
  app.run('0.0.0.0', 8085)