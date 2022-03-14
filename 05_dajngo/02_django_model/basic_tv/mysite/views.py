from msvcrt import LK_UNLCK
from multiprocessing import context
import re
from django.http import HttpResponse # 그냥 데이터를 응답으로 주는 함수(클래스)
from django.shortcuts import render # html을 응답으로 함수
import random


# Create your views here.
def home(request):
    return render(request, 'a.html')

def lunch(request):
    return render(request, 'lunch.html')


def lotto(request):
    lucky_numbers = random.sample(range(1,46), 6)
    return HttpResponse(f'{lucky_numbers} ')

def greeting(request, name):
    context = {
        'name' : name.upper()
    }
    return render(request, 'greeting.html', context)
