from django.shortcuts import render
from django.http import JsonResponse
import main, json


object = main.app("one_user")
names = object.get_names()
stats = object.get_stats()
home_stats = ""
away_stats = ""

def initialise():
    return main.app()


def team_stats(search):
    global stats
    for team in stats:
        if team["Name"] == search:
            return team
    response = f"{'Error, Could not find stats for {search}'}"
    
    return json.dumps(response)


def index_view(request):
    global stats, names, home_stats, away_stats
    home_stats, away_stats = "", ""  # Reset stats
    context = {}
    context["names"] = names
    return render(request, "stats/home.html", context)


def compare_view(request):
    global home_stats, away_stats
    
    body = json.loads(request.body)
     
    home_stats = team_stats(body.get("Home"))
    away_stats = team_stats(body.get("Away"))  
     
    result = {"Home": home_stats, "Away": away_stats}
    
    print(result)
    return JsonResponse(json.dumps(result), safe=False)


def predict_view(request):
    context = {}
    context["names"] = names
    context["home"] = home_stats
    context["away"] = away_stats
    context["prediction"] = object.get_prediction(home_stats, away_stats)
    return render(request, "stats/home.html", context)
