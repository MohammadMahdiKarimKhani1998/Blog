from django.shortcuts import render
from django.views.generic import ListView
from home.models import FirstSlide


class Home(ListView):
    model = FirstSlide
    ordering = ['slug']
    template_name = 'home/index.html'
