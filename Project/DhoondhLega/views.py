from django.shortcuts import render
from django.http import JsonResponse
from .models import House
import urllib, json
from datetime import datetime, timedelta


def index(req):
    return render(req, "index.html")


def house_main(req):
	# x=House.objects.all()
	# return render(req, "house.html",{'y':x})
	
	if request.method == "GET":
	 	obj = House.objects.all()
	 	data = serializers.serialize('json', obj)
	 	return HttpResponse(data , content_type='json')

	#data = json.loads(response.read()) 
	#return JsonResponse(data); 