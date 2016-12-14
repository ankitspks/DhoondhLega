from __future__ import unicode_literals

from django.db import models

# Create your models here.
class House(models.Model):
	house_type = models.CharField (max_length=25)
	price = models.IntegerField(default = 0)
	customer = models.CharField (max_length =100)
	description = models.CharField(max_length = 1000)
	address = models.CharField(max_length = 200)
	photos = models.FileField (upload_to=None, max_length=100)
	contact = models.IntegerField(default=0)

 	def __str__(self):
 		return self.customer 



class Movies(models.Model):
	name = models.CharField(max_length=25)
	MOVIE_TYPE = (
		('action', 'ACTION'),
		('animation', 'ANIMATION'),
		('comedy', 'COMEDY'),
		('documentary', 'DOCUMENTARY'),
		('horror', 'HORROR'),
		('musical', 'MUSICAL'),
		('romance', 'ROMANCE'),
		('Sci-Fi'),
		('thriller', 'THRILLER'),
	)
	genre = models.CharField(max_length=30, choices=MOVIE_TYPE,
			 default='action')
	LANGUAGE_CHOICE = (
		('hollywood', 'HOLLYWOOD'),
		('bollywood', 'BOLLYWOOD'),
	)