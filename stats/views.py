from django.shortcuts import render
import app

# Create your views here.

def initialise():
    return 

def index_view(request):
    context = {}
    app.main()
    context['names'] = app.getNames()
    context['home'] = app.getStats("Barcelona")
    context['away'] = app.getStats("Liverpool")
    #Render takes in 3 parameters: request, html file and the context in {} which helps pass values from things like variables
    return render(request, "stats/home.html", context)
