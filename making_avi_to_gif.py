# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 15:11:19 2018

@author: tbeleyur
"""

from moviepy.editor import *
import easygui as eg

file_location = str(eg.fileopenbox('Please choose the AVI file you want to load'))

vid_clip = VideoFileClip(file_location)

print('Please choose the destination folder from the GUI window that has opened')
output_location = str(eg.filesavebox('Please give the file name to be saved'))

vid_clip.resize(0.5).write_gif(output_location, fps=60)

