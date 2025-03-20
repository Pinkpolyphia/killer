from django.urls import path
from . import views

app_name = "killing"
urlpatterns = [
    path("", views.index, name="index"),
    # path("/<str:name>", views.greet, name="greet"),
    path("/tusk", views.tusk, name="tusk"),
    path("/confess", views.confessionary, name="confessionary")
] 