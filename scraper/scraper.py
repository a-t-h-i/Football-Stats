#This package will contain the code for scraping web content
from urllib.request import urlopen as scrape
import os
htmlCopy = ""

def getHTML(url):
  page = scrape(url)
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  createHTML(html)

def createHTML(html):
  #This function will create an html file and save it in the html folder
  if html == None:
    print("Failed!")
  else:
    #Code to write to html file
    with open(os.path.join("scraper/html", "page.html"), "w") as file:
      file.write(html)
      file.close()
    
def createCSV():
  if htmlCopy == "":
    print("Do some scraping first!")
  # else:
    #Code to create csv file from html code
  