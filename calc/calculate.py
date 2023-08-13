def average_goals(goals_scored, games_played):
    if (int(goals_scored) == 0) or (int(games_played) == 0):
        return 0.0;
        
    return float(round((int(goals_scored) / int(games_played)), 2))


def win_percentage(games_played, games_won):
    if (int(games_played) == 0) or (int(games_won) == 0):
        return 0.0;
        
    return float(round(((int(games_won) / int(games_played)) * 100), 2))


def lose_percentage(games_played, games_lost):
    if (int(games_played) == 0) or (int(games_lost) == 0):
        return 0.0;
        
    return float(round(((int(games_lost) / int(games_played)) * 100), 2))
    


def draw_percentage(games_played, draws):
    if (int(games_played) == 0) or (int(draws) == 0):
        return 0.0;
    
    return float(round(((int(draws) / int(games_played)) * 100), 2))
