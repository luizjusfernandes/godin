#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tool to manually create turtles facial graphs.
"""

import cv2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
import os
from os import path
import sys
import json
from faceMatch import get_graph

start = True
app = QApplication(sys.argv)
while start:
    # Ask for image location
    imgLocation = QFileDialog.getOpenFileName()[0]

    # Read image and json file
    img = cv2.imread(imgLocation)

    with open(path.splitext(imgLocation)[0] + r'.json') as file:
        jsonData = file.read()

    # Ensure image and info were read
    if (img is None) or (jsonData is None):
        raise FileNotFoundError("Could not read image or json file.")

    # Convert json data to dictionary
    info = json.loads(jsonData)

    # Anottates image with user's help
    G, img_out = get_graph(img)
    
    #Copy original image to image database with name ID_Date_Side
    #with open('Database/'+turtleID+'.pickle', 'wb') as handle:
    #    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

    cont = input('Another One? (y/n) ')
    if cont != 'y':
        start = False

app.quit()
