#!/usr/bin/python3
from ai import prediction
from calc import calculate
import glob, pandas as pd

from dbox import drop


class app(object):
    
    def __init__(self, id):
        drop.check()
        self.object_id = id
        self.csv_path = 'csv'
        self.csv_files = glob.glob(self.csv_path + '/*.csv')
        self.df_list = []
        [self.df_list.append(self._read_file(file)) for file in self.csv_files]
        self.df = pd.concat(self.df_list, ignore_index=True)
        self.rows, self.columns = self.df.shape
        self.teams = self._create_teams_list()
        self.team_stats = self._create_stats()
        self.home_stats = ""
        self.away_stats = ""
    
    def _read_file(self, file):
        return pd.read_csv(file, header=1)


    def _create_teams_list(self):
        result = []
        for i in range(self.rows):
            result.append(self.df.loc[i, :].values.flatten().tolist())
        return result


    def get_names(self):
        names = []
        [names.append(team['Name']) for team in self.team_stats]
        names.sort()
        return names


    def _to_json(self, data):
        statistics = {
            'Name': data[0],
            'Position': int(data[1]),
            'Played': int(data[3]),
            'Won': int(data[4]),
            'Lost': int(data[6]),
            'Draws': int(data[5]),
            'Goals': int(data[7]),
            'Conceded': int(data[8]),
            'AwayPlayed': int(data[21]),
            'AwayGoals': int(data[25]),
            'AwayConceded': int(data[26]),
            'AwayWins': int(data[22]),
            'AwayLost': int(data[24]),
            'AwayDraws': int(data[23]),
            'HomePlayed': int(data[12]),
            'HomeGoals': int(data[16]),
            'HomeConceded': int(data[17]),
            'HomeWins': int(data[13]),
            'HomeLoses': int(data[15]),
            'HomeDraws': int(data[14]),
            'AverageGoals': calculate.average_goals(data[7], data[3]),
            'WinPercentage': calculate.win_percentage(data[3], data[4]),
            'LosePercentage': calculate.lose_percentage(data[3], data[6]),
            'DrawPercentage': calculate.draw_percentage(data[3], data[5]),
            'AverageHomeGoals': calculate.average_goals(data[16], data[12]),
            'HomeWinPercentage': calculate.win_percentage(data[12], data[13]),
            'HomeDrawsPercentage': calculate.draw_percentage(data[12], data[14]),
            'HomeLosePercentage': calculate.lose_percentage(data[12], data[15]),
            'AverageAwayGoals': calculate.average_goals(data[25], data[21]),
            'AwayWinPercentage': calculate.win_percentage(data[21], data[22]),
            'AwayLosePercentage': calculate.lose_percentage(data[21], data[24]),
            'AwayDrawPercentage': calculate.draw_percentage(data[21], data[23]),
        }
        return statistics


    def _create_stats(self):
        stats_list = []
        [stats_list.append(self._to_json(team)) for team in self.teams]
        return stats_list
    
    
    def get_stats(self):
        return self.team_stats
    
    
    def set_home_stats(self, stats):
        self.home_stats = stats
        

    def set_away_stats(self, stats):
        self.away_stats = stats    
    

    def _ai_prompt(self, home_team, away_team):
        return f"""
    Assuming the role of a sports analyst, you are provided with data on the performance of two soccer teams,
    in the current season. The data includes the following variables:

    Home Team:
    {home_team}

    Away Team:
    {away_team}
    
    Using only the data provided, please do the following:

    Write a paragraph that provides an in-depth analysis of both team's performance in the current season. Please compare their position 
    in the league, number of games played, wins, losses, draws, goals scored, goals conceded, and their form at home and away. Use your knowledge 
    of soccer to provide insights and predictions for their future performance.
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
        return prediction.ask(self._ai_prompt(home, away))