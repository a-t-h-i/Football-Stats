#!/usr/bin/python3
from ai import prediction
from calc import calculate
import os, glob, json, time, pandas as pd

os.system('clear')

teamStats = []

def getNames():
    #Gets names of teams and returns the list of names
    names = []
    
    for team in teamStats:
        names.append(team["Name"])
    return names


def getStats():
    global teamStats

    return teamStats 


def updateData():
    #This function will update the data sored on the json file
    return 0


def saveToJson(data):
    #This function will help optimise the program by storing all the data
    #for all the teams in a json file for quicker access instead of having
    #to do all the computations everytime the program is run
    return 0

def saveStats(stats):
    global teamStats
    teamStats = stats


def toJson(data):
    #Another way I can approach this is if I loop throught the data list and then
    #add the items I'm iterating to the json object
    result = {"Name":data[0], 
              "Position":data[1],
              "Played":data[3],
              "Won":data[4],
              "Lost":data[6],
              "Draws":data[5],
              "Goals":data[7],
              "Conceded":data[8],
              "Away Played":data[21],
              "Away Goals":data[25],
              "Away Conceded":data[26],
              "Away Wins":data[22],
              "Away Lost":data[24],
              "Away Draws":data[23],
              "Home Played":data[12],
              "Home Goals":data[16],
              "Home Conceded":data[17],
              "Home Wins":data[13],
              "Home Loses":data[15],
              "Home Draws":data[14],
              "Average Goals":calculate.averageGoals(data[7], data[3]),
              "Win Percentage":calculate.winPercentage(data[3], data[4]),
              "Lose Percentage":calculate.losePercentage(data[3], data[6]),
              "Draw Percentage":calculate.drawPercentage(data[3], data[5]),
              "Average Home Goals":calculate.averageGoals(data[16],data[12]),
              "Home Win Percentage":calculate.winPercentage(data[12],data[13]),
              "Home Draws Percentage":calculate.drawPercentage(data[12],data[14]),
              "Home Lose Percentage":calculate.losePercentage(data[12], data[15]),
              "Average Away Goals":calculate.averageGoals(data[25], data[21]),
              "Away Win Percentage":calculate.winPercentage(data[21], data[22]),
              "Away Lose Percentage":calculate.losePercentage(data[21], data[24]),
              "Away Draw Percentage":calculate.drawPercentage(data[21], data[23])}    
    return result


class app(object):
    def __init__(self):
        #self.df = pd.read_csv('csv/soccer-standings.csv', header=1)
        self.csvPath = "csv/"
        self.csvFiles = glob.glob(self.csvPath + "/*.csv")
        self.dfList = []
        
        [self.dfList.append(self.readFile(file)) for file in self.csvFiles]

        self.df = pd.concat(self.dfList, ignore_index=True)
        self.rows, self.columns = self.df.shape #Get number of rows and columns 
        self.teams = []
    
    def readFile(self, file):
        return pd.read_csv(file, header = 1)
   
    def mapTeams(self):
        for i in range(self.rows):
            self.teams.append(self.df.loc[i, :].values.flatten().tolist()) #Append to list of teams
    
    def getTeams(self):
        return self.teams


def aiPrompt(homeTeam, awayTeam):
    return f"""
You are a sports analyst. Take into account the stats of two soccer teams below.

Look at this JSON data and show it in a presentable way:
{homeTeam}

Look at this JSON data and show it in a presentable way also:
{awayTeam}


First give me a summary of the stats and compare both teams.

Now analyse all the data and give me an accurate, useful and in depth information that I can use for betting.
Use logistic regression, poisson distribution and alto rating to give me answers to the following:
Give me the likelihood of a draw in %?
Likelihood of both teams scoring in %?
What's the expected number of goals?
Which team do you think will win and why?
"""

def getPrediction(stats):
    #Takes in a list that of stats at index 0 is the home team stasts at iindex 1 is the away team statss
    prompt = aiPrompt(stats[0],stats[1])
    return prediction.ask(prompt)

def main():

    run = app()
    run.mapTeams() #Save list of teams from CSV file
    teamsList = run.getTeams() #Get list of teams
    jsonList = [] #List of json objects
    #Create json object and save to list of json objects
    names = []
    stats = {}
    for team in teamsList:
        jsonList.append(toJson(team))
    saveStats(jsonList)
    names = getNames()
    stats = getStats()
    return (names,stats)
