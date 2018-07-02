# -*- coding: utf-8 -*-
""" code snippet to speed up a video
Created on Fri Jun 29 14:41:17 2018

@author: tbeleyur
"""

from moviepy.editor import *

import easygui as eg

video_file =  str(eg.fileopenbox('please choose video file'))
vid_clip = VideoFileClip(video_file)
vid_clip.speedx(2).write_videofile('spedup_version_outsideOC.mp4')