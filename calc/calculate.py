def average_goals(goals_scored, games_played):
    return float(round((goals_scored / games_played), 2))


def win_percentage(games_played, games_won):
    return float(round(((games_won / games_played) * 100), 2))


def lose_percentage(games_played, games_lost):
    return float(round(((games_lost / games_played) * 100), 2))


def draw_percentage(games_played, draws):
    return float(round(((draws / games_played) * 100), 2))
