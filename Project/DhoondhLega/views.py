from django.shortcuts import render
from django.http import HttpResponse
import urllib, json
from datetime import datetime, timedelta
from .forms import HouseForm


def index(request):
    return render(request, "index.html")

def house_post(request):
	form = HouseForm(request.POST or None , request.FILES or None )
	# if Request.method == "POST":
	# 	print Request.POST.get("Content")
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		
		return render(request, "post_house.html")
		
	else:
		return render(request, "post_house.html",{"form":form})
# def theater_movies(request):
# 	current_dt = datetime.today().strftime("%Y-%m-%d")
# 	previous_dt = (datetime.now() - timedelta(days=40)).strftime("%Y-%m-%d")
# 	url = "https://api.themoviedb.org/3/discover/movie?api_key=8419dce727cd16afcc50b6e085faf444&include_video=true&primary_release_date.gte="+str(previous_dt)+"&primary_release_date.lte="+str(current_dt)
# 	response = urllib.urlopen(url)
# 	data = json.loads(response.read())
# 	return render(request, "theater_movie.html" , {"data":data['results']})


# def popular_movies(request):
# 	url = "https://api.themoviedb.org/3/discover/movie?api_key=8419dce727cd16afcc50b6e085faf444&sort_by=popularity.desc"
# 	response = urllib.urlopen(url)
# 	data = json.loads(response.read())
# 	return render(request, "theater_movie.html" , {"data":data['results']})


# def top_rated_movies(request):
# 	url = "https://api.themoviedb.org/3/discover/movie?api_key=8419dce727cd16afcc50b6e085faf444&sort_by=vote_average.desc"
# 	response = urllib.urlopen(url)
# 	data = json.loads(response.read())
# 	return render(request, "theater_movie.html" , {"data":data['results']})

# def upcoming_movies(request):
# 	current_dt = datetime.today().strftime("%Y-%m-%d")
# 	next_dt = (datetime.now() + timedelta(days=40)).strftime("%Y-%m-%d")
# 	url = "https://api.themoviedb.org/3/discover/movie?api_key=8419dce727cd16afcc50b6e085faf444&include_video=true&primary_release_date.gte="+str(current_dt)+"&primary_release_date.lte="+str(next_dt)
# 	response = urllib.urlopen(url)
# 	data = json.loads(response.read())
# 	return render(request, "theater_movie.html" , {"data":data['results']})

# For trailers
#  https://api.themoviedb.org/3/movie/id/videos?api_key=8419dce727cd16afcc50b6e085faf444&language=en-US