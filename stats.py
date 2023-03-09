#!/usr/bin/python3
from ai import prediction
from calc import calculate
import os, glob, json, pandas as pd

os.system('clear')

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
              "Win Percentage":calculate.winPercentage(data[7], data[4]),
              "Lose Percentage":calculate.losePercentage(data[7], data[6]),
              "Draw Percentage":calculate.drawPercentage(data[7], data[5]),
              "Average Home Goals":calculate.averageGoals(data[16],data[12]),
              "Home Win Percentage":calculate.winPercentage(data[12],data[13]),
              "Home Draws Percentage":calculate.drawPercentage(data[12],data[14]),
              "Home Lose Percentage":calculate.losePercentage(data[12], data[15]),
              "Average Away Goals":calculate.averageGoals(data[25], data[21]),
              "Away Win Percentage":calculate.winPercentage(data[21], data[22]),
              "Away Lose Percentage":calculate.losePercentage(data[21], data[24]),
              "Away Draw Percentage":calculate.drawPercentage(data[21], data[23])}
    return result


class stats(object):
    def __init__(self, home, away):
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
        

    def teamFound(self,searchValue):
        for team in self.teams:

            if team[0].upper() == searchValue.upper():
                return True

        return False
    
    def getTeams(self):
        return self.teams


def teams():
    home = input("Home team: ")
    away = input("Away team: ")
    return (home, away)

def generateStats(data):

    return f"""
    Team name: {data["Team Name"]}
    Position: {data["Position"]}
    Games Played: {data["Games Played"]}
    Games Won: {data["Games Won"]}
    Games Lost: {data["Games Lost"]}
    Draws: {data["Draws"]}
    Goals Scored: {data["Goals Scored"]}
    Goals Conceded: {data["Goals Conceded"]}
    
    Average Goals Per Game: {data["Average Goals"]}
    Overall Win Percentage: {data["Win Percentage"]}%
    
    Home wins: {data["Home Wins"]}%
    Home loses: {data["Home Loses"]}%
    Home draws: {data["Home Draws"]}%
    
    Away wins: {data["Away Wins"]}%
    Away loses: {data["Away Loses"]}%
    Away draws: {data["Away Draws"]}%
    """

def aiPrompt(homeTeam, awayTeam):
    return f"""
You are a sports analyst. Take into account the stats of two soccer teams below.

These are the stats in JSON format for the team that will be playing on home ground:
{homeTeam}

These are the stats in JSON format for the away team:
{awayTeam}

Analyse them and give me an accurate, useful and in depth information that I can use for betting.
Use logistic regression, poisson distribution and alto rating to give me answers to the following:
Give me the likelihood of a draw in %?
Likelihood of both teams scoring in %?
What's the expected number of goals?
Which team do you think will win and why?
"""

def main():
    homeTeam, awayTeam = teams()
    run = stats(homeTeam, awayTeam) #Instantiate stats class
    run.mapTeams() #Save list of teams from CSV file
    teamsList= run.getTeams() #Get list of teams
    jsonList = [] #List of json objects

    #Create json object and save to list of json objects
    for team in teamsList:
        jsonList.append(toJson(team))

    found = False

    while not found:
        homeStats = ""
        awayStats = ""
        
        if run.teamFound(homeTeam) and run.teamFound(awayTeam):
            os.system('clear')

            for object in jsonList:

                if str(object.get("Team Name")).upper() == homeTeam.upper():
                    homeStats = str(object)
                
                elif str(object.get("Team Name")).upper() == awayTeam.upper():
                    awayStats = str(object)
                                
            print("Home team Stats\n" + homeStats)
            print("-----------------------------")
            print("Away team stats\n" + awayStats)
            print("-----------------------------")
            print(prediction.ask(aiPrompt(homeStats, awayStats)))
            found = True

        else:
            os.system('clear')
            print("Please enter correct team names...")
            homeTeam, awayTeam = teams()


# scraper.getHTML("https://www.rotowire.com/soccer/league-table.php")

if __name__ == "__main__":
    main()
