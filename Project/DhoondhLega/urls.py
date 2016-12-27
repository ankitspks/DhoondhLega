from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^house/$', views.house, name='house'),
    url(r'^house/post/$', views.house_post, name='house_post'),
    url(r'^house/post.html/$', views.house_post_html, name='house_post_html'),
    url(r'^templates/hm.html/$', views.hm, name='hm'),
    url(r'^house/find.html/$', views.find, name='find'),
    url(r'^templates/login.html/$', views.signIn, name='signIn'),
    url(r'^templates/sign.html/$', views.Register, name='register'),
    url(r'^SignUp.html/$', views.signUp, name='signUp'),
    url(r'^house/post/$', views.house_post, name='house_post'),

]
