# -*- coding: utf-8 -*-
""" Script to automate the merge and export of thermal camera files

Created on Wed May 02 16:22:14 2018

@author: tbeleyur
"""
import re
import subprocess
import os
import easygui as eg

# change the current working directory
print('please choose a folder')
overall_folder = eg.diropenbox()
os.chdir(overall_folder)

folder_name = 'P0000002'
#choose set of files (common for all cameras)
print('please choose the file names that will be used across the previously input folder')
chosen_filepaths_unicode = eg.fileopenbox(multiple=True)
chosen_filepaths_ascii = map(lambda X: X.encode('ascii', 'ignore'), chosen_filepaths_unicode)
def get_filename(X):
    '''
    '''
    result = re.search('[0-9]*.TMC', X)
    filename = result.string[result.start():result.end()]
    return(filename)

chosen_filenames = map(get_filename, chosen_filepaths_ascii)
output_filename = '_wand_merge.TMC'

# give in name of end result file 

# 


for each_camfolder in ['K1', 'K2', 'K3']:
    os.chdir(overall_folder+'\\'+each_camfolder+'\\'+folder_name)
    output_file = each_camfolder+ output_filename
    thermoviewer_command = 'Thermoviewer -exfn ' + output_file+' -merge '+ ' '.join(chosen_filenames)
    process = subprocess.Popen(['Powershell', thermoviewer_command])
    print ( 'processing taking place - please wait for some time '+each_camfolder)
    print "Happens while running"
    process.communicate() #now wait plus that you can send commands to process