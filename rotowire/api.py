# -*- coding: utf-8 -*-
import requests, json


def stats():
    names = []
    stats = []
    api_endpoints = [
        "https://rotowire.com/soccer/tables/standings.php?league=EPL&length=total&season=2022",
        "https://www.rotowire.com/soccer/tables/standings.php?league=ENG_CH&length=total&season=2022",
        "https://www.rotowire.com/soccer/tables/standings.php?league=LIGA&length=total&season=2022",
        "https://www.rotowire.com/soccer/tables/standings.php?league=SERI&length=total&season=2022",
        "https://www.rotowire.com/soccer/tables/standings.php?league=FRAN&length=total&season=2022",
        "https://www.rotowire.com/soccer/tables/standings.php?league=BUND&length=total&season=2022",
    ]
    result = []

    for endpoint in api_endpoints:
        result.append(requests.get(endpoint).text)

    for league in result:
        for team in json.loads(league):
            names.append(team["team"])
            stats.append(team)

    names.sort()
    return names, stats
