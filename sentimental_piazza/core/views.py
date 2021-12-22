from django.shortcuts import render, redirect
from util import api_caller, wordcloud


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
        context["data"] = data

        wordcloud.customPlotFreq(data)
        wordcloud.customWordCloud(data)

        return render(request, "core/wc.html", context)

    return redirect("home")
