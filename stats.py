from scraper import scraper
import csv
import os
import pandas as pd
os.system('clear')

class team(object):
    def __init__(self, name, position, data):
        self.name = name
        self.position = position
        self.data = data

    def getPosition(self):
        return self.position

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
        self.df = pd.read_csv('csv/soccer-standings.csv', header=1)
        self.homeTeam = home
        self.awayTeam = away
        self.rows, self.columns = self.df.shape
        self.teams = []

   
    def mapTeams(self):
        for i in range(self.rows-1):
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

homeTeam, awayTeam = teams()
run = stats(homeTeam, awayTeam) #Instantiate stats class
run.mapTeams() #Save list of teams from CSV file
teams = run.getTeams()
teamObjects = []

#Add teams to list of objects
for i in range(len(teams)-1):
    teamObjects.append(team(teams[i][0], i+1, teams[i]))

found = False

while not found:

    if run.teamFound(homeTeam) and run.teamFound(awayTeam):
        print(f"Name: {teamObjects[0].getName()}")
        print(f"Posision: {teamObjects[0].getPosition()}")
        print(f"Matches won: {teamObjects[0].getGamesWon()}")
        print(f"Draws: {teamObjects[0].getDraws()}")
        print(f"Conceded: {teamObjects[0].getGoalsConceded()}")
        print(f"Loses: {teamObjects[0].getLoses()}")
        print(f"Played: {teamObjects[0].getGamesPlayed()}")
        found = True
    else:
        os.system('clear')
        print("Please enter correct team names...")
        homeTeam, awayTeam = teams()


# scraper.getHTML("https://www.rotowire.com/soccer/league-table.php")

