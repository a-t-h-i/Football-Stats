def average_goals(goals_scored, games_played):
    return float(round((int(goals_scored) / int(games_played)), 2))


def win_percentage(games_played, games_won):
    return float(round(((int(games_won) / int(games_played)) * 100), 2))


def lose_percentage(games_played, games_lost):
    return float(round(((int(games_lost) / int(games_played)) * 100), 2))


def draw_percentage(games_played, draws):
    return float(round(((int(draws) / int(games_played)) * 100), 2))
