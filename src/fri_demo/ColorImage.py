# This is the ColorImage class

import pyrealsense2 as rs
import numpy as np
import cv2

# Matplotlib testing code dependencies 
from PIL import Image
import matplotlib
import tkinter as tk
matplotlib.use('TkAgg')  # or 'Qt5Agg' or any other GUI backend
import matplotlib.pyplot as plt


class RealSenseCamera:
  def __init__(self):
    self.pipeline = rs.pipeline()
    self.config = rs.config()

    # Configure the pipeline
    self._configure_pipeline()

  def _configure_pipeline(self):
    self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    self.profile = self.pipeline.start(self.config)

  def get_frame(self):
    frames = self.pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    color_image = np.asanyarray(color_frame.get_data())
    color_image_rgb = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)
    return color_image_rgb
  
if __name__ == "__main__":
  camera = RealSenseCamera()
  imgplot = plt.imshow(camera.get_frame())
  plt.show()
