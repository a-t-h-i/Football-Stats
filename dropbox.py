#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime

folder_path = "csv"

def has_latest_data():
    # Get the current date
    today = datetime.date.today()
    latest = True
    
    #Check if folder empty
    if (os.listdir(folder_path)) == []:
        return False

    # Loop through each CSV file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):

            # Get the date the file was last modified
            file_path = os.path.join(folder_path, filename)
            modification_time = os.path.getmtime(file_path)
            modification_date = datetime.date.fromtimestamp(modification_time)
            
            # Delete the file if the modification date is not today
            if modification_date != today:
                os.remove(file_path)
                latest = False
    
    return latest

def update():
    return 0
    #Gets latest files from dropbox

def check():
    print(has_latest_data())
    if not has_latest_data():
        update()

check()
