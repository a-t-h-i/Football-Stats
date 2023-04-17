from django.shortcuts import render
from django.http import JsonResponse
import main, json


object = main.app("one_user")
names = object.get_names()
stats = object.get_stats()

def initialise():
    return main.app()


def team_stats(search):
    
    for team in stats:
        if team["Name"] == search:
            return team
    response = f"{'Error, Could not find stats for {search}'}"
    
    return json.dumps(response)


def index_view(request):
    global stats, names
    context = {}
    context["names"] = names
    return render(request, "stats/home.html", context)


def compare_view(request):
    body = json.loads(request.body)
    
    if (body.get("Home") == "Select Team" or body.get("Away") == "Select Team"):
        return JsonResponse(json.dumps({"Error":"Not found!"}), safe=False)
        
    object.set_home_stats(team_stats(body.get("Home")))
    object.set_away_stats(team_stats(body.get("Away"))) 
    
    result = {"Home": object.home_stats, "Away": object.away_stats}

    return JsonResponse(json.dumps(result), safe=False)


def predict_view():
    prediction = {"Prediction":object.get_prediction(object.home_stats, object.away_stats)}
    return JsonResponse(json.dumps(prediction, safe=False))