from django.shortcuts import render
import app, json

stats = ""
home_stats = ""
away_stats = ""
names = ""
stats = ""


def initialise():
    return app.main()


def team_stats(search):
    global stats

    for team in stats:
        if team["Name"] == search:
            return team
    return {"Error", f"Could not find {search}"}


def index_view(request):
    global stats, names, home_stats, away_stats
    home_stats, away_stats = "", ""  # Reset stats
    context = {}
    names, stats = initialise()
    prediction = ""
    context["names"] = names
    return render(request, "stats/home.html", context)


def compare_view(request):
    global copy, home_stats, away_stats
    context = {}

    home = request.POST.get("home_team")
    away = request.POST.get("away_team")

    if (home == "") or (away == ""):
        context["error"] = "Please make sure you have made both selections!"
        context["names"] = names
        return render(request, "stats/home.html", context)

    if not isinstance(home_stats, dict) or (not isinstance(away_stats, dict)):
        home_stats = team_stats(home)
        away_stats = team_stats(away)

    elif (home_stats["Name"] != home) or (away_stats["Name"] != away):
        home_stats = team_stats(home)
        away_stats = team_stats(away)

    context["selected_home"] = home
    context["selected_away"] = away
    context["names"] = names
    context["home"] = json.dumps(home_stats)
    context["away"] = json.dumps(away_stats)
    return render(request, "stats/home.html", context)


def predict_view(request):
    context = {}
    context["names"] = names
    context["home"] = json.dumps(home_stats)
    context["away"] = json.dumps(away_stats)
    context["prediction"] = app.get_prediction(home_stats, away_stats)
    return render(request, "stats/home.html", context)
