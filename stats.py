from scraper import scraper
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

        if run.teamFound(homeTeam) and run.teamFound(awayTeam):
            os.system('clear')
            for i in range(len(teamObjects) -1):
                if homeTeam.upper() == teamObjects[i].getName().upper():
                    print("--------------Home Team--------------")
                    print(f"Team: {teamObjects[i].getName()}")
                    print(f"Position: {teamObjects[i].getPosition()}")
                    print(f"Games played: {teamObjects[i].getGamesPlayed()}")
                    print(f"Games won: {teamObjects[i].getGamesWon()}")
                    print(f"Games lost: {teamObjects[i].getLoses()}")
                    print(f"Draws: {teamObjects[i].getDraws()}")
                    print("\n")
                elif awayTeam.upper() == teamObjects[i].getName().upper():
                    print("--------------Away Team----------")
                    print(f"Team: {teamObjects[i].getName()}")
                    print(f"Position: {teamObjects[i].getPosition()}")
                    print(f"Games played: {teamObjects[i].getGamesPlayed()}")
                    print(f"Games won: {teamObjects[i].getGamesWon()}")
                    print(f"Games lost: {teamObjects[i].getLoses()}")
                    print(f"Draws: {teamObjects[i].getDraws()}")

            found = True
        else:
            os.system('clear')
            print("Please enter correct team names...")
            homeTeam, awayTeam = teams()


main()
# scraper.getHTML("https://www.rotowire.com/soccer/league-table.php")

