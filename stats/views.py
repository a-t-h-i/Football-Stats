from django.shortcuts import render
import app

stats = []
copy = []
def initialise():
    return app.main()
    

def teamStats(search):
    global stats
    
    for team in stats:
        
        if team["Name"].upper() == search.upper():
            return team
    return {"Error":f"{search} not found"}


def index_view(request):
    global stats
    context = {}
    names, stats = initialise()
    prediction = ""
    context['names'] = names
    
    #Render takes in 3 parameters: request, html file and the context in {} which helps pass values from things like variables
    return render(request, "stats/home.html", context)


def compare_view(request):
    global copy
    index_view(request)
    homeTeam  = request.POST.get("home_team")
    awayTeam = request.POST.get("away_team")
    context = {}
    copy = []
    copy.append(homeTeam)
    copy.append(awayTeam)
    context['home'] = teamStats(homeTeam)
    context['away'] = teamStats(awayTeam)
    return render(request, "stats/home.html", context)


def predict_view(request):
    global copy
    context = {}
    context['prediction'] = app.getPrediction(copy)
    return render(request, "stats/home.html", context)
