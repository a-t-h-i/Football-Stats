#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, datetime, dropbox

token = os.environ.get("D_BOX")

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
    dbx = dropbox.Dropbox(token)

    # Set up local folder to save CSV files
    local_folder = 'csv'
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)

    # Get list of files in Dropbox folder
    dropbox_folder = '/csv'
    files = dbx.files_list_folder(dropbox_folder).entries

    # Download each CSV file and save it to local folder
    for file in files:
        if isinstance(file, dropbox.files.FileMetadata) and file.name.endswith('.csv'):
            dropbox_path = f'{dropbox_folder}/{file.name}'
            local_path = f'{local_folder}/{file.name}'
            with open(local_path, 'wb') as f:
                metadata, res = dbx.files_download(dropbox_path)
                f.write(res.content)


def check():
    if not has_latest_data():
        update()

check()
