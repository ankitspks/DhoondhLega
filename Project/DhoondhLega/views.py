from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse, JsonResponse
=======
from django.http import HttpResponse
>>>>>>> 09c2f93630f49c369de2be6fb66892298b3b587e
import json
from django.core import serializers
from .forms import HouseForm
from .models import House


def index(request):
    return render(request, "index.html")

<<<<<<< HEAD
def house(request):
    return render(request, "House.html")

def find(request):
    return render(request, "find.html")

def hm(request):
    return render(request, "hm.html")

def signIn(request):
    return render(request, "login.html")

def Register(request):
    return render(request, "sign.html")

def signUp(request):
    return render(request, "SignUp.html")

def house_post(request):
	if request.method == "GET":
		print "skjfklsj"
		obj = House.objects.all()
		data = serializers.serialize('json', obj)
		return JsonResponse(dict(genres=list(House.objects.values())))

	# # if request.method == "POST":
	# obj = House.objects.all()
	# data = serializers.serialize('json', obj)
	# print "sample"
	# return JsonResponse(data)

def house_post_html(request):
    return render(request, "post.html")
=======

def house_post(request):
	if request.method == "GET":
		pass
	# if request.method == "POST":
	obj = House.objects.all()
	data = serializers.serialize('json', obj)
	return HttpResponse(data , content_type='json')
>>>>>>> 09c2f93630f49c369de2be6fb66892298b3b587e
