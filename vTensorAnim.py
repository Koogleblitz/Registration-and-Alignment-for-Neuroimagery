from skimage import io
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import seaborn as sns 

vTensor= io.imread(r"C:\Users\richa\OneDrive\Neuroscience\Data\DBS_preprocessed_ROI_and_3D_data\normalized\TIFF_registered\reg_avg180_300.tiff")
mult= 2
add= .2
sizer= .8
begindex= 0
endex= 240
frameCount= endex-begindex
pseInterval= 0.1
plt.figure(figsize = (12.8*sizer,9.1*sizer), facecolor= "black", edgecolor="black")
#sns.heatmap(vTensor[:, :, 0], cbar=False)

im= plt.imshow((vTensor[:, :, 0]+add)*mult)
plt.xlabel('X', color = 'white', fontweight ='bold')
plt.ylabel('Y', color = 'white', fontweight ='bold')
plt.colorbar()
plt.xticks(color= 'white', labels=[0,10,30,50,70, 90], ticks=[0,10,30,50,70, 90])
plt.yticks(color= 'white', labels= [120, 100,70,40,10,0], ticks=[120, 100,70,40,10,0])
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

