from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.home, name="main"),
    path('recommendations/', views.recommendations, name="recommendations"),
]
