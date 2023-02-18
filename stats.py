from ai import prediction
import csv
import os
import glob
import pandas as pd
os.system('clear')

class team(object):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def getPosition(self):
        return self.data[1]

    def getName(self):
        return self.name

    def getGamesPlayed(self):
        return self.data[3]
    
    def getGamesWon(self):
        return self.data[4]
    
    def getLoses(self):
        return self.data[6]

    def getDraws(self):
        return self.data[5]

    def getGoals(self):
        return self.data[7]

    def getGoalsConceded(self):
        return self.data[8]


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
    name = data.getName()
    position = data.getPosition()
    played = data.getGamesPlayed()
    won = data.getGamesWon()
    loses = data.getLoses()
    draws = data.getDraws()
    goals = data.getGoals()
    conceded = data.getGoalsConceded()

    return f"""
    Team name: {name}
    Position: {position}
    Games Played: {played}
    Games Won: {won}
    Games Lost: {loses}
    Draws: {draws}
    Goals Scored: {goals}
    Goals Conceded: {conceded}
    """

def aiPrompt(homeTeam, awayTeam):
    return f"""
Asume the rolse of a sports analyst and give me analytical information.
Given these stats for the home team:
{homeTeam}

Also given these stats for the away team:
{awayTeam}

Give me an in depth analysis, which team do you think will win, will both teams score and number of goals
"""

def main():
    homeTeam, awayTeam = teams()
    run = stats(homeTeam, awayTeam) #Instantiate stats class
    run.mapTeams() #Save list of teams from CSV file
    teamsList= run.getTeams()
    teamObjects = []

    #Add teams to list of objects
    for i in range(len(teamsList)-1):
        teamObjects.append(team(teamsList[i][0], teamsList[i]))

    found = False

    while not found:
        homeStats = ""
        awayStats = ""
        
        if run.teamFound(homeTeam) and run.teamFound(awayTeam):
            os.system('clear')

            for i in range(len(teamObjects)):
                if teamObjects[i].getName().upper() == homeTeam.upper():
                    homeStats = generateStats(teamObjects[i])
                
                elif teamObjects[i].getName().upper() == awayTeam.upper():
                    awayStats = generateStats(teamObjects[i])
                                
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
