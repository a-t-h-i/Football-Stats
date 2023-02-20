def averageGoals(goalsScored, gamesPlayed):
    result = (goalsScored/gamesPlayed)
    return round(result,2)

def winPercentage(gamesPlayed, gamesWon):
    result = (gamesWon/gamesPlayed)*100
    return round(result,2)

def losePercentage(gamesPlayed, gamesLost):
    result = (gamesLost/gamesPlayed)*100
    return round(result, 2)

def drawPercentage(gamesPlayed, draws):
    result = (draws/gamesPlayed)
    return round(result,2)
