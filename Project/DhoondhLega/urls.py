from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie/$', views.theater_movies, name='theater_movies'),
    url(r'^movie/popular/$', views.popular_movies, name='popular_movies'),
    url(r'^movie/top/$', views.top_rated_movies, name='top_rated_movies'),
    url(r'^movie/upcoming/$', views.upcoming_movies, name='upcoming_movies'),
]
