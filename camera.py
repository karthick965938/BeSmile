import cv2
from PyEmotion import *
import sqlite3 as sql
from datetime import datetime

# PyEmotion init
er = DetectFace(device='cpu', gpu_id=0)

class VideoCamera(object):
  def __init__(self):
    self.video = cv2.VideoCapture(0)
  
  def __del__(self):
    self.video.release()
  
  def get_frame(self):
    success, frame = self.video.read()
    image, emotion = er.predict_emotion(frame)
    if emotion:
    	self.save_emotion(emotion) 
    ret, jpeg = cv2.imencode('.jpg', image)
    return jpeg.tobytes()

  def save_emotion(self, emotion):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    date = datetime.now().strftime("%d-%m-%Y")
    if emotion:
      try: 
        with sql.connect("DB/database.db") as con:
          cur = con.cursor()
          cur.execute("INSERT INTO emotions (name,create_date,created_at) VALUES (?,?,?)",(emotion, date, time))  
          con.commit()
      except:
        con.rollback()

      finally:
        con.close()