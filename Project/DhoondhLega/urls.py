from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie/$', views.theater_movie, name='theater_movie'),
]
