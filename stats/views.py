from django.shortcuts import render
import app

stats = []

def initialise():
    return app.main()
    

def teamStats(search):
    global stats
    
    for team in stats:
        
        if team["Name"].upper() == search.upper():
            return team
    return {"Error":"Team not found"}


def index_view(request):
    global stats
    context = {}
    names, stats = initialise()
    prediction = ""
    context['names'] = names
    
    #Render takes in 3 parameters: request, html file and the context in {} which helps pass values from things like variables
    return render(request, "stats/home.html", context)


def stats_view(request):
    homeTeam  = ""
    awayTeam = ""
    context = {}
    context['home'] = teamStats(homeTeam)
    context['away'] = teamStats(awayTeam)
    return render(request, "stats/home.html", context)


def prediction_view(request):
    homeTeam = ""
    awayTeam = ""
    context = {}
    context['ai'] = app.getPrediction([teamStats(homeTeam), teamStats(awayTeam)])
    return render(request, "stats/home.html", context)
