#Input: numpy depth array, camera frames
#Output: display disparity map and camera frames

#Run in IDLE environment to display images

import numpy as np
#import matplotlib
#matplotlib.use('Agg')
from matplotlib import pyplot as plt
from PIL import Image

#print('POINT 0')
fig, (ax1,ax2) = plt.subplots(2,1)

#print('POINT 1')

for i in range(3000,4001):
    #print('ITERATION: ',i)

    # DISPLAY ORIGINAL IMAGE FRAMES
    # For kitti_2015 data
    #frame = Image.open(r'C:\Users\Benjamin Chang\Documents\KITTI Scene_Flow_Dataset_2015\testing\image_2\%06i_10.png' %i)
    
    # For cam_1_1_trim data
    frame = Image.open(r'C:\Users\Benjamin Chang\Documents\Video Processing Research\Camera Calibration\left_data_rect\cam_left_rgb_frame_%05i.png' %i)
    #print('FRAME: ', frame)
    
    # DISPLAY DEPTH OUTPUT IMAGES
    # For kitti_2015 data
    #depth_output = Image.open(r'C:\Users\Benjamin Chang\Documents\Video Processing Research\monodepth-master\outputs\kitti_2015_dataset\testing\image_2\%06i_10_disp.png' %i)
    
    # For cam_1_1_trim data
    depth_output = Image.open(r'C:\Users\Benjamin Chang\Documents\Video Processing Research\monodepth-master\outputs\left_data_rect\cam_left_rgb_frame_%05i_disp.png' %i)
    #print('DEPTH_OUTPUT_1: ', depth_output)

    # DISPLAY NUMPY FILES
    # For kitti_2015 data
    #depth_output_npy = np.load(r'C:\Users\Benjamin Chang\Documents\Video Processing Research\monodepth-master\outputs\kitti_2015_dataset\testing\image_2\%06i_10_disp.npy' %i)
    
    #For cam_1_1_trim data
    #depth_output_npy = np.load(r'C:\Users\Benjamin Chang\Documents\Video Processing Research\monodepth-master\outputs\cam_1_1_trim_zoom_1\cam_1_1_trim %04i_disp.npy' %i)
    #print('DEPTH_OUTPUT_2: ', depth_output_npy)
    #print('shape_2 : ', depth_output_npy.shape)

    #disp_output = 1./depth_output_npy
    #print('DISP_OUTPUT: ', disp_output)
    
    ax1 = plt.subplot("211").imshow(frame)                      #128x1248x3
    ax2 = plt.subplot("212").imshow(depth_output,cmap='gray')
	
    plt.pause(0.01)
    plt.clf()
    
