from django.shortcuts import render
import app

# Create your views here.

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
    context['home'] = teamStats("Barcelona")
    context['away'] = teamStats("Liverpool")
    context['prediction'] = app.getPrediction([teamStats("Barcelona"),teamStats("Liverpool")])

    #Render takes in 3 parameters: request, html file and the context in {} which helps pass values from things like variables
    return render(request, "stats/home.html", context)
