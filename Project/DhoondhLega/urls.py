from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^house/post/$', views.house_post, name='house_post'),

]
