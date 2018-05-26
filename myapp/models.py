from django.db import models

class Passenger(models.Model):
	name = models.CharField(max_length=255)
	sex = models.CharField(max_length=255)
	survived = models.BooleanField()
	age = models.FloatField()
	ticket_class = models.PositiveSmallIntegerField()
	embarked = models.CharField(max_length=255)

	def __str__(self):
		return self.name
