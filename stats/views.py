from django.shortcuts import render
import app

home_stats = ''
away_stats = ''
names = ''

def initialise():
    return app.main()
    

def teamStats(search):
    global stats
    
    for team in stats:
        
        if team["Name"].upper() == search.upper():
            return team
    return {"Error":f"{search} not found"}


def index_view(request):
    global stats, names
    context = {}
    names, stats = initialise()
    prediction = ""
    context['names'] = names
    
    #Render takes in 3 parameters: request, html file and the context in {} which helps pass values from things like variables
    return render(request, "stats/home.html", context)


def compare_view(request):
    global copy, home_stats, away_stats

    home_stats = teamStats(request.POST.get("home_team"))
    away_stats = teamStats(request.POST.get("away_team"))
    context={}
    context['names'] = names
    context['home'] = home_stats
    context['away'] = away_stats
    return render(request, "stats/home.html", context)


def predict_view(request):
    context = {}
    context['names'] = names
    context['home'] = home_stats
    context['away'] = away_stats
    context['prediction'] = app.getPrediction((home_stats, away_stats))
    return render(request, "stats/home.html", context)
