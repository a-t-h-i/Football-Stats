#!/usr/bin/python3
from ai import prediction
from calc import calculate
from dbox import drop
import os, glob, json, time, pandas as pd

teamStats = []


def getNames():
    # Gets names of teams and returns the list of names
    names = []

    for team in teamStats:
        names.append(team["Name"])
    names.sort()
    return names


def getStats():
    global teamStats

    return teamStats


def updateData():
    # This function will update the data sored on the json file
    return 0


def saveToJson(data):
    # This function will help optimise the program by storing all the data
    # for all the teams in a json file for quicker access instead of having
    # to do all the computations everytime the program is run
    return 0


def saveStats(stats):
    global teamStats
    teamStats = stats


def toJson(data):

    result = {
        "Name": data[0],
        "Position": int(data[1]),
        "Played": int(data[3]),
        "Won": int(data[4]),
        "Lost": int(data[6]),
        "Draws": int(data[5]),
        "Goals": int(data[7]),
        "Conceded": int(data[8]),
        "Away Played": int(data[21]),
        "Away Goals": int(data[25]),
        "Away Conceded": int(data[26]),
        "Away Wins": int(data[22]),
        "Away Lost": int(data[24]),
        "Away Draws": int(data[23]),
        "Home Played": int(data[12]),
        "Home Goals": int(data[16]),
        "Home Conceded": int(data[17]),
        "Home Wins": int(data[13]),
        "Home Loses": int(data[15]),
        "Home Draws": int(data[14]),
        "Average Goals": float(calculate.averageGoals(data[7], data[3])),
        "Win Percentage": float(calculate.winPercentage(data[3], data[4])),
        "Lose Percentage": float(calculate.losePercentage(data[3], data[6])),
        "Draw Percentage": float(calculate.drawPercentage(data[3], data[5])),
        "Average Home Goals": float(calculate.averageGoals(data[16], data[12])),
        "Home Win Percentage": float(calculate.winPercentage(data[12], data[13])),
        "Home Draws Percentage": float(calculate.drawPercentage(data[12], data[14])),
        "Home Lose Percentage": float(calculate.losePercentage(data[12], data[15])),
        "Average Away Goals": float(calculate.averageGoals(data[25], data[21])),
        "Away Win Percentage": float(calculate.winPercentage(data[21], data[22])),
        "Away Lose Percentage": float(calculate.losePercentage(data[21], data[24])),
        "Away Draw Percentage": float(calculate.drawPercentage(data[21], data[23])),
    }
    
    return result


class app(object):
    def __init__(self):
        # self.df = pd.read_csv('csv/soccer-standings.csv', header=1)
        self.csvPath = "csv"
        self.csvFiles = glob.glob(self.csvPath + "/*.csv")
        self.dfList = []

        [self.dfList.append(self.readFile(file)) for file in self.csvFiles]

        self.df = pd.concat(self.dfList, ignore_index=True)
        self.rows, self.columns = self.df.shape  # Get number of rows and columns
        self.teams = []

    def readFile(self, file):
        return pd.read_csv(file, header=1)

    def mapTeams(self):
        for i in range(self.rows):
            self.teams.append(
                self.df.loc[i, :].values.flatten().tolist()
            )  # Append to list of teams

    def getTeams(self):
        return self.teams


def aiPrompt(homeTeam, awayTeam):
    return f"""
Assume the role of a sports analyst. Look at the following JSON data of two soccer teams going head to head:

{homeTeam}

{awayTeam}

After looking at the data do the following (Use only the data I provided you for the below actions):
1) Provide a paragraph of an in depth, creative and informative comparison of the provided data.
2) Is it likely that both teams will score?
3) What are the chances of a draw happening?
4) What are the chances of a draw?
5) Who do you suggest will win the match? (Do factor in home ground advantage)

At the end of your response say the following exactly as it is: "The above predictions are that of a language model and should be used for entertainment purposes only. Be advised not to make financial decisions based on them."
"""


def getPrediction(home, away):
    # Takes in a list that of stats at index 0 is the home team stasts at iindex 1 is the away team statss
    prompt = aiPrompt(home, away)
    return prediction.ask(prompt)


def main():
    # First check data
    drop.check()

    run = app()
    run.mapTeams()  # Save list of teams from CSV file
    teamsList = run.getTeams()  # Get list of teams
    jsonList = []  # List of json objects
    # Create json object and save to list of json objects
    names = []
    stats = {}
    for team in teamsList:
        jsonList.append(toJson(team))
    saveStats(jsonList)
    names = getNames()
    stats = getStats()
    return (names, stats)
