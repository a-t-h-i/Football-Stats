#!/usr/bin/python3
from ai import prediction
from calc import calculate
import os, glob, pandas as pd

os.system('clear')

class team(object):
    def __init__(self, data):
        self.data = data

    def getPosition(self):
        return self.data[1]

    def getName(self):
        return self.data[0]

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

    def getAwayGoals(self):
        return self.data[25]

    def getAwayConceded(self):
        return self.data[26]

    def getAwayMatches(self):
        return self.data[21]

    def getAwayLoses(self):
        return self.data[24]

    def getAwayDraws(self):
        return self.data[23]

    def getAwayWins(self):
        return self.data[22]

    def getHomeGoals(self):
        return self.data[16]

    def getHomeConceded(self):
        return self.data[17]
    
    def getHomeMatches(self):
        return self.data[12]
    
    def getHomeWins(self):
        return self.data[13]

    def getHomeDraws(self):
        return self.data[14]

    def getHomeLoses(self):
        return self.data[15]


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



def calcOverallPerformance(team):
    matchesPlayed = team.getGamesPlayed()
    goalsScored = team.getGoals()
    matchesWon = team.getGamesWon()
    loses = team.getLoses()
    draws = team.getDraws()

    winPerc = calculate.winPercentage(matchesPlayed, matchesWon)
    losePerc = calculate.losePercentage(matchesPlayed, loses)
    drawPerc = calculate.drawPercentage(matchesPlayed, draws)
    goalsPerGame = calculate.averageGoals(goalsScored, matchesPlayed)
    
    return (winPerc, losePerc, drawPerc, goalsPerGame)


def calcHomePerformance(team):
    matchesPlayed = team.getHomeMatches()
    goalsScored = team.getHomeGoals()
    matchesWon = team.getHomeWins()
    loses = team.getHomeLoses()
    draws = team.getHomeDraws()

    winPerc = calculate.winPercentage(matchesPlayed, matchesWon)
    losePerc = calculate.losePercentage(matchesPlayed, loses)
    drawPerc = calculate.drawPercentage(matchesPlayed, draws)
    goalsPerGame = calculate.averageGoals(goalsScored, matchesPlayed)

    return (winPerc, losePerc, drawPerc, goalsPerGame)
    

def calcAwayPerformance(team):
    matchesPlayed = team.getAwayMatches()
    goalsScored = team.getAwayGoals()
    matchesWon = team.getAwayWins()
    loses = team.getAwayLoses()
    draws = team.getAwayDraws()

    winPerc = calculate.winPercentage(matchesPlayed, matchesWon)
    losePerc = calculate.losePercentage(matchesPlayed, loses)
    drawPerc = calculate.drawPercentage(matchesPlayed, draws)
    goalsPerGame = calculate.averageGoals(goalsScored, matchesPlayed)

    return (winPerc, losePerc, drawPerc, goalsPerGame)

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
    performance = calcOverallPerformance(data)
    homePerf = calcHomePerformance(data)
    awayPerf = calcAwayPerformance(data)
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
    
    Average Goals Per Game: {performance[3]}
    Overall Win Percentage: {performance[0]}%
    
    Home wins: {homePerf[0]}%
    Home loses: {homePerf[1]}%
    Home draws: {homePerf[2]}%
    
    Away wins: {awayPerf[0]}%
    Away loses: {awayPerf[1]}%
    Away draws: {awayPerf[2]}%
    """

def aiPrompt(homeTeam, awayTeam):
    return f"""
Assume the role of a sports analyst and give me analytical information.

Given these stats for the home team:
{homeTeam}

Also given these stats for the away team:
{awayTeam}

Take into account which team is playing home and what is their home win %
Analyse the stats using poisson distribution, regression and elo rating.
Which team do you suggest will win?
Give me the likelihood of a draw in %?
Likelihood of both teams scoring in %?
What's the expected number of goals?
"""

def main():
    homeTeam, awayTeam = teams()
    run = stats(homeTeam, awayTeam) #Instantiate stats class
    run.mapTeams() #Save list of teams from CSV file
    teamsList= run.getTeams()
    teamObjects = []

    #Add teams to list of objects
    for i in range(len(teamsList)-1):
        teamObjects.append(team(teamsList[i]))

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
