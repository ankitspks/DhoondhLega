from __future__ import unicode_literals
from django.db import models

class Movie(models.Model):
	name = models.CharField(max_length=20)
	genre = models.CharField(max_length=25)
	language = models.CharField(max_length=50)
	cast = models.CharField(max_length=50)
	image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
	reviews = models.CharField(max_length=1000)
	rating = models.IntegerField(default=1)
	
	def __str__(self):
		return self.name