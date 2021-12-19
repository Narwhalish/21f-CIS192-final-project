from django.urls import path
from core.views import *

urlpatterns = [
    path("", home, name="home"),
    path("class_selection/", class_selection, name="class_selection"),
]
