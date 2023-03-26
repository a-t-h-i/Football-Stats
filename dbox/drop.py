#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, datetime, dropbox

token = os.environ.get("D_BOX")

def has_latest_data():
    
    folder_path = "csv"

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
    local_folder = "csv"
    dbx = dropbox.Dropbox(token)

    if not os.path.exists(local_folder):
        os.makedirs(local_folder)

    # List files in dropbox folder
    dropbox_folder = '/csv'
    files = dbx.files_list_folder(dropbox_folder).entries

    #Download csv files to local folder
    for file in files:
        if isinstance(file, dropbox.files.FileMetadata) and file.name.endswith('.csv'):
            dropbox_path = f'{dropbox_folder}/{file.name}'
            file_it = f'{local_folder}/{file.name}'
            with open(file_it, 'wb') as f:
                metadata, res = dbx.files_download(dropbox_path)
                f.write(res.content)


def check():
    if not has_latest_data():
        update()