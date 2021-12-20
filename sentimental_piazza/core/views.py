from django.shortcuts import render, redirect
from util import api_caller, wc

user_data = {}


def home(request):
    user_data.clear()

    return render(request, "core/home.html")


def class_selection(request):
    if request.method == "POST":
        user_data["email"] = request.POST.get("user_email")
        user_data["password"] = request.POST.get("user_password")

    return render(request, "core/class_selection.html")


def wc(request):
    if request.method == "POST":
        user_data["class_id"] = request.POST.get("class_id")

    return render(request, "core/wc.html")
