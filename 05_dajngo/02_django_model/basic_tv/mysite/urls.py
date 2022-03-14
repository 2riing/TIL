
from django.urls import path
from . import views


urlpatterns = [
    # /mysite/
    path('', views.home),
    # /mysite/lunch/
    path('lunch/', views.lunch, name = 'lunch'),
    # /mysite/lotto/
    path('lotto/', views.lotto, name = 'lotto'),
    path('greeting/<str:name>/', views.greeting),
]
