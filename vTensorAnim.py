from skimage import io
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import seaborn as sns 
import numpy as np
from tkinter import filedialog


vTensor= io.imread(r"C:\Users\richa\OneDrive\Neuroscience\Data\DBS_preprocessed_ROI_and_3D_data\normalized\TIFF_registered\dft_avgTensor.tiff")
mult= 1
add= 0
sizer= .8
begindex= 100
endex= 200
frameCount= endex-begindex
pseInterval= 0.001
xLabel= np.arange(0, 91, 10)
yLabel= np.arange(0, 121, 10)
plt.figure(figsize = (12.8*sizer,9.1*sizer), facecolor= "black", edgecolor="black")
#sns.heatmap(vTensor[:, :, 0], cbar=False)

im= plt.imshow((vTensor[:, :, 0]+add)*mult)
plt.xlabel('X', color = 'white', fontweight ='bold')
plt.ylabel('Y', color = 'white', fontweight ='bold')
plt.colorbar()
plt.xticks(color= 'white', labels= xLabel, ticks= xLabel)
plt.yticks(color= 'white', labels= yLabel, ticks= yLabel)
plt.grid()
plt.tick_params(direction='out', grid_linewidth= 0.1, width= 3, length= 3)
plt.minorticks_on()
plt.box(on=True)

for i in range(begindex+1,endex+1):
    im.set_data((vTensor[:, :, i]+add)*mult)
    plt.pause(pseInterval)
    plt.title("M["+str(i//120)+':'+str(82)+']  |  ' + str(i), fontsize = 15, color = 'white', fontweight ='bold')
plt.show()


#[+]----------------------------------------------------

# plt.rcParams["figure.figsize"] = [9.1*sizer, 12.8*sizer]
# plt.rcParams["figure.autolayout"] = True
# fig = plt.figure()
# dimension = (5, 5)
# data = vTensor
# sns.heatmap(data[:, :, 0], vmax=.8)


# def init():
#     sns.set_theme()
#     plt.style.use("dark_background")
#     sns.heatmap(data[:, :, 0], cbar=False)

# def animate(i):
#     data = vTensor[:, :, i]
#     sns.heatmap(data, vmax=.8, cbar=False)
#     print()
    

# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frameCount, repeat=False)

# plt.show()


#------------------

# export_file_path = filedialog.asksaveasfilename(defaultextension = '.png')
# im1.save(export_file_path)


#------------------
# https://medium.com/@enriqueav/how-to-create-video-animations-using-python-and-opencv-881b18e41397

# import numpy as np
# from cv2 import VideoWriter, VideoWriter_fourcc

# width = 1280
# height = 720
# FPS = 24
# seconds = 10

# fourcc = VideoWriter_fourcc(*'MP42')
# video = VideoWriter('./noise.avi', fourcc, float(FPS), (width, height))

# for _ in range(FPS*seconds):
#     frame = np.random.randint(0, 256, 
#                               (height, width, 3), 
#                               dtype=np.uint8)
#     video.write(frame)
# video.release()

