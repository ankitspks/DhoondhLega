from django.shortcuts import render
from django.http import HttpResponse
import urllib, json
from datetime import datetime, timedelta


def index(request):
    return render(request, "index.html")


def theater_movie(request):
	current_dt = datetime.today().strftime("%Y-%m-%d")
	previous_dt = (datetime.now() - timedelta(days=20)).strftime("%Y-%m-%d")
	url = "https://api.themoviedb.org/3/discover/movie?api_key=8419dce727cd16afcc50b6e085faf444&primary_release_date.gte=2016-11-15&primary_release_date.lte="+str(current_dt)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return render(request, "theater_movie.html" , {"data":data})