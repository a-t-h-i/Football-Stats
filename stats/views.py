from django.shortcuts import render
import app

# Create your views here.

def index_view(request):
    context = {}
    context['ai'] = app.main("Liverpool","Arsenal")[0]

    #Render takes in 3 parameters: request, html file and the context in {} which helps pass values from things like variables
    return render(request, "stats/home.html", context)
