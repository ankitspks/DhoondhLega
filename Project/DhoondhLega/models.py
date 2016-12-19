from __future__ import unicode_literals

from django.db import models

# Create your models here.
class House(models.Model):
 	house_type = models.CharField (max_length=25)
 	price = models.IntegerField(default = 0)
 	customer = models.CharField (max_length =100)
 	description = models.CharField(max_length = 1000)
 	address = models.CharField(max_length = 200)
<<<<<<< HEAD
 	photos = models.FileField (upload_to=None, null=True, blank=True)
=======
 	photos = models.FileField (upload_to=None, max_length=100)
>>>>>>> 09c2f93630f49c369de2be6fb66892298b3b587e
 	contact = models.IntegerField(default=0)
 
  	def __str__(self):
  		return self.customer