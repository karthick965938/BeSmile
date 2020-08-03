import cv2
from PyEmotion import *
import cv2 as cv
import os
import csv
from pathlib import Path

# PyEmotion init
er = DetectFace(device='cpu', gpu_id=0)
er.store_emotion_details(os.path.dirname(os.path.realpath(__file__)))

class VideoCamera(object):
  def __init__(self):
    self.video = cv2.VideoCapture(0)
  
  def __del__(self):
    self.video.release()
  
  def get_frame(self):
    success, frame = self.video.read()
    image = er.predict_emotion(frame)
    ret, jpeg = cv2.imencode('.jpg', image)
    return jpeg.tobytes()
  	