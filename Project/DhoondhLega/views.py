from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from .forms import HouseForm
from .models import House


def index(request):
    return render(request, "index.html")


def house_post(request):
	if request.method == "GET":
		pass
	# if request.method == "POST":
	obj = House.objects.all()
	data = serializers.serialize('json', obj)
	return HttpResponse(data , content_type='json')