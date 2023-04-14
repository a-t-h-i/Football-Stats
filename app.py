#!/usr/bin/python3
from ai import prediction
from calc import calculate
import glob, pandas as pd


class app(object):
    
    def __init__(self, id):
        self.object_id = id
        self.csv_path = "csv"
        self.csv_files = glob.glob(self.csv_path + "/*.csv")
        self.df_list = []
        [self.df_list.append(self._read_file(file)) for file in self.csv_files]
        self.df = pd.concat(self.df_list, ignore_index=True)
        self.rows, self.columns = self.df.shape
        self.teams = self._create_teams_list()
        self.team_stats = self._create_stats()
    
    
    def _read_file(self, file):
        return pd.read_csv(file, header=1)


    def _create_teams_list(self):
        result = []
        for i in range(self.rows):
            result.append(self.df.loc[i, :].values.flatten().tolist())
        return result


    def get_names(self):
        names = []
        [names.append(team["Name"]) for team in self.team_stats]
        names.sort()
        return names


    def _to_json(self, data):
        statistics = {
            "Name": data[0],
            "Position": int(data[1]),
            "Played": int(data[3]),
            "Won": int(data[4]),
            "Lost": int(data[6]),
            "Draws": int(data[5]),
            "Goals": int(data[7]),
            "Conceded": int(data[8]),
            "Away Played": int(data[21]),
            "Away Goals": int(data[25]),
            "Away Conceded": int(data[26]),
            "Away Wins": int(data[22]),
            "Away Lost": int(data[24]),
            "Away Draws": int(data[23]),
            "Home Played": int(data[12]),
            "Home Goals": int(data[16]),
            "Home Conceded": int(data[17]),
            "Home Wins": int(data[13]),
            "Home Loses": int(data[15]),
            "Home Draws": int(data[14]),
            "Average Goals": calculate.average_goals(data[7], data[3]),
            "Win Percentage": calculate.win_percentage(data[3], data[4]),
            "Lose Percentage": calculate.lose_percentage(data[3], data[6]),
            "Draw Percentage": calculate.draw_percentage(data[3], data[5]),
            "Average Home Goals": calculate.average_goals(data[16], data[12]),
            "Home Win Percentage": calculate.win_percentage(data[12], data[13]),
            "Home Draws Percentage": calculate.draw_percentage(data[12], data[14]),
            "Home Lose Percentage": calculate.lose_percentage(data[12], data[15]),
            "Average Away Goals": calculate.average_goals(data[25], data[21]),
            "Away Win Percentage": calculate.win_percentage(data[21], data[22]),
            "Away Lose Percentage": calculate.lose_percentage(data[21], data[24]),
            "Away Draw Percentage": calculate.draw_percentage(data[21], data[23]),
        }
        return statistics


    def _create_stats(self):
        stats_list = []
        [stats_list.append(self._to_json(team)) for team in self.teams]
        return stats_list
    
    
    def get_stats(self):
        return self.team_stats


    def _ai_prompt(self, home_team, away_team):
        return f"""
    Assume the role of a sports analyst. Look at the following JSON data of two soccer teams going head to head:

    {home_team}

    {away_team}

    After looking at the data do the following (Use only the data I provided you for the below actions):
    1) Provide a paragraph of an in depth, creative and informative comparison of the provided data.
    2) Is it likely that both teams will score?
    3) What are the chances of a draw happening?
    4) What are the chances of a draw?
    5) Who do you suggest will win the match? (Do factor in home ground advantage)

    At the end of your response say the following exactly as it is: "The above predictions are that of a language
    model and should be used for entertainment purposes only. Be advised not to make financial decisions based on
    them."
    """


    def get_prediction(self, home, away):
        return prediction.ask(self._ai_prompt(home, away))