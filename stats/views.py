from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def compare_view(request):
    body = json.loads(request.body)
    
    if (body.get("Home") == "Select Team" or body.get("Away") == "Select Team"):
        return JsonResponse(json.dumps({"Error":" Please make both selections dumbo!"}), safe=False)

    result = {"Home": team_stats(body.get("Home")), "Away": team_stats(body.get("Away"))}
    
    return JsonResponse(json.dumps(result), safe=False)


@csrf_exempt
def predict_view(request):
    body = json.loads(request.body)
    
    prediction = {"Prediction":object.get_prediction(team_stats(body.get("Home")), 
                                                     team_stats(body.get("Away")))}
    return JsonResponse(json.dumps(prediction), safe=False)