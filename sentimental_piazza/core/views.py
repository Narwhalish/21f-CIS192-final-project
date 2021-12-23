from django.shortcuts import render, redirect
from util import api_caller, grapher


def home(request):
    request.session.flush()

    return render(request, "core/home.html")


def class_selection(request):
    if request.method == "POST":
        request.session["email"] = request.POST.get("user_email")
        request.session["password"] = request.POST.get("user_password")

    return render(request, "core/class_selection.html")


def wc(request):
    context = {}

    if request.method == "POST":
        if request.session.get("email") is None:
            return redirect("home")

        request.session["class_id"] = request.POST.get("class_id")

        data = api_caller.get_information(
            request.session.get("email"),
            request.session.get("password"),
            request.session.get("class_id"),
        )

        grapher.customPlotFreq(
            data, [9, 12], "sentimental_piazza/core/static/core/plotfreq.png"
        )

        grapher.createWordCloud(
            grapher.retrieveMonths(grapher.dataDictionary(data), [12, 11, 10, 9]),
            100,
            "sentimental_piazza/core/static/core/wordcloud.png",
        )

        return render(request, "core/wc.html", context)

    return redirect("home")
