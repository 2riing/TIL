import json
from platform import release
import urllib.request
import requests
from django.shortcuts import render
from . import config
import random

my_api_key = config.API_KEY['api_key']
base_url = 'https://api.themoviedb.org/3/'

# id = 278

# Create your views here.
def home(request):
    return render(request, 'movies/index.html')

def recommendations(request):
    url = f'{base_url}movie/278/recommendations?api_key={my_api_key}&language=ko-kr&page=1'
    recommendation = requests.get(url)
    result = recommendation.json()
    num = random.choice(range(0,21))

    movie = {
        'title': result['results'][num]['title'],
        'poster_path': result['results'][num]['poster_path'],
        'overview': result['results'][num]['overview'],
        'vote_average' : round(result['results'][num]['vote_average'],1),
        'release_date': result['results'][num]['release_date'],
    }
    print(movie['release_date'])
    
   
    return render(request, 'movies/recommendations.html', context = movie)
