import numpy as np
import opencv as cv2
import os
 
width = 1280
hieght = 720
channel = 3
 
fps = 30
sec = 5
 
# Syntax: VideoWriter_fourcc(c1, c2, c3, c4) # Concatenates 4 chars to a fourcc code
#  cv2.VideoWriter_fourcc('M','J','P','G') or cv2.VideoWriter_fourcc(*'MJPG)
 
fourcc = cv2.VideoWriter_fourcc(*'MP42') # FourCC is a 4-byte code used to specify the video codec.
# A video codec is software or hardware that compresses and decompresses digital video. 
# In the context of video compression, codec is a portmanteau of encoder and decoder, 
# while a device that only compresses is typically called an encoder, and one that only 
# decompresses is a decoder. Source - Wikipedia
 
#Syntax: cv2.VideoWriter( filename, fourcc, fps, frameSize )
video = cv2.VideoWriter('test.mp4', fourcc, float(fps), (width, hieght))
 
for frame_count in range(fps*sec):
    img = np.random.randint(0,255, (hieght, width, channel), dtype = np.uint8)
    video.write(img)
 
video.release()