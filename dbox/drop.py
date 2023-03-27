#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, datetime, dropbox, requests

def check_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def has_latest_data():
    folder_path = "csv"
    today = datetime.date.today()
    latest = True

    check_folder(folder_path)

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
    dbx = dropbox.Dropbox(get_token())

    check_folder(local_folder)

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


def get_token():
    #Automatically get a short lived access token
    url = "https://api.dropbox.com/oauth2/token"
    refresh_token = os.eviron.get("REFRESH_TOKEN")
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    grant_type = "refresh_token"

    data = {
        "refresh_token": refresh_token,
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, data=data)

    return str(response.json()['access_token'])
    
def check():
  if not has_latest_data:
    update()
