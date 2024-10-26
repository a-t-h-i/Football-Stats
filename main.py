#!/usr/bin/python3
from ai import prediction
from calc import calculate
from rotowire import api


class app(object):
    def __init__(self):
        self.names, self.teams = api.stats()
        self.team_stats = self._create_stats()

    def get_names(self):
        return self.names

    def _to_json(self, data):
        return {
            "Name": data["team"],
            "Position": int(data["totalrank"]),
            "Points": int(data["totalp"]),
            "Played": int(data["totalm"]),
            "Won": int(data["totalw"]),
            "Lost": int(data["totall"]),
            "Draws": int(data["totald"]),
            "Goals": int(data["totalg"]),
            "Conceded": int(data["totalga"]),
            "AwayPlayed": int(data["awaym"]),
            "AwayGoals": int(data["awayg"]),
            "AwayConceded": int(data["awayga"]),
            "AwayWins": int(data["awayw"]),
            "AwayLost": int(data["awayl"]),
            "AwayDraws": int(data["awayd"]),
            "HomePlayed": int(data["homem"]),
            "HomeGoals": int(data["homeg"]),
            "HomeConceded": int(data["homega"]),
            "HomeWins": int(data["homew"]),
            "HomeLoses": int(data["homel"]),
            "HomeDraws": int(data["homed"]),
            "AverageGoals": calculate.average_goals(data["totalg"], data["totalm"]),
            "WinPercentage": calculate.win_percentage(data["totalm"], data["totalw"]),
            "LosePercentage": calculate.lose_percentage(data["totalg"], data["totall"]),
            "DrawPercentage": calculate.draw_percentage(data["totalm"], data["totald"]),
            "AverageHomeGoals": calculate.average_goals(data["homeg"], data["homem"]),
            "HomeWinPercentage": calculate.win_percentage(data["homem"], data["homew"]),
            "HomeDrawsPercentage": calculate.draw_percentage(
                data["homem"], data["homed"]
            ),
            "HomeLosePercentage": calculate.lose_percentage(
                data["homem"], data["homel"]
            ),
            "AverageAwayGoals": calculate.average_goals(data["awayg"], data["awaym"]),
            "AwayWinPercentage": calculate.win_percentage(data["awaym"], data["awayw"]),
            "AwayLosePercentage": calculate.lose_percentage(
                data["awaym"], data["awayl"]
            ),
            "AwayDrawPercentage": calculate.draw_percentage(
                data["awaym"], data["awayd"]
            ),
        }

    def _create_stats(self):
        stats_list = []
        [stats_list.append(self._to_json(team)) for team in self.teams]
        return stats_list

    def get_stats(self):
        return self.team_stats

    def _ai_prompt(self, home_team, away_team):
        return f"""
    Assuming the role of a sports analyst, you are provided with data on the performance of two soccer teams,
    in the current season. The data includes the following variables:

    Home Team:
    {home_team}

    Away Team:
    {away_team}
    
    Using only the data provided, do the following:
    You must use info from these websites to support your analysis:
    - https://forebet.com
    - https://www.fctables.com/
    - https://www.sofascore.com/
    - https://footystats.org/
    - https://www.flashscore.co.za/

    If the above external sites were referenced, then credit them in your analysis.
    
    Give me a concise analysis of both team's performances in the current season. Compare their position 
    in the league, number of games played, wins, losses, draws, goals scored, goals conceded, and their form at home and away.
    What is the win percentage in the current season for both the teams? Please provide a clear and concise answer.
    What is the average goals per game in the current season for both teams? Please provide a clear and concise answer.
    What is the home team's win percentage in the current season? Please provide a clear and concise answer.
    Based on your analysis, what is the likelihood of both teams scoring and the likelihood of a draw? Please provide a clear and concise answer.
    Based on your analysis, what is the expected number of goals? Please provide a clear and concise answer.
    Based on your analysis, which team has a better chance of winning?
    
    Finally, please include the following statement at the end of your response exactly as it is: 'The above predictions are that of a language 
    model and should be used for entertainment purposes only. Be advised not to make financial decisions based on them.'
    """

    def get_prediction(self, home, away):

        line_width = 60
        title = "AI PREDICTION"

        # Calculate the padding on each side
        padding = (line_width - len(title)) // 2

        # Format the line
        output = f"Home Team Stats:\n{home}\n\n\nAway Team Stats:\n{away}\n\n\n\n\n\n{'_' * padding}{title}{'_' * padding}\n{prediction.ask(self._ai_prompt(home, away))}"

        return output

