from django.shortcuts import render

# Create your views here.

def index_view(request):
    #Render takes in 3 parameters: request, html file and the context in {} which helps pass values from things like variables
    return render(request,"index.html",{})
