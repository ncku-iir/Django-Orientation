from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")

def index(request):
    name = "Pika~"
    current_time = str(datetime.now())
    return render(request, 'myapp/index.html', locals())

def tag_page(request):
    animals = ['cat', 'dog', 'pikachu'] 
    return render(request, 'myapp/tag.html', locals())