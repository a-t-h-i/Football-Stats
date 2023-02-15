from scraper import scraper
import csv
import os
import pandas as pd
os.system('clear')

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


def teams():
    home = input("Home team: ")
    away = input("Away team: ")
    return (home, away)

homeTeam, awayTeam = teams()
run = stats(homeTeam, awayTeam) #Instantiate stats class
run.mapTeams() #Save list of teams from CSV file
found = False

while not found:

    if run.teamFound(homeTeam) and run.teamFound(awayTeam):
        found = True
    else:
        os.system('clear')
        print("Please enter correct team names...")
        homeTeam, awayTeam = teams()


# scraper.getHTML("https://www.rotowire.com/soccer/league-table.php")

