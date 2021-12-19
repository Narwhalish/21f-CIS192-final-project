from django.shortcuts import render, redirect


def home(request):
    return render(request, "core/home.html")


def class_selection(request):
    context = {}

    if request.method == "POST":
        context["user_email"] = request.POST.get("user_email")
        context["user_password"] = request.POST.get("user_password")

    return render(request, "core/class_selection.html", context)
