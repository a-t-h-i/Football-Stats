#Script to auto-update the csv files
from zdrive import Downloader

#def checkDate():
    #Check the date of the present files

def update():
    output_directory = "./csv"
    d = Downloader()
    folder_id = 'csv'
    d.downloadFolder(folder_id, destinationFolder=output_directory)


