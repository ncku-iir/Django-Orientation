from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import User, UserInfo
from django.http import JsonResponse
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

def createUser(request):
    u = User.objects.create(name=“lisa”)
    u.save()
    ui = UserInfo.objects.create(user_id=u, age=23)
    ui.save()
    return JsonResponse({“state”:”success”})