from django.db import models

class FoodStore(models.Model):
	title      = models.CharField(max_length=250)
	quantity   = models.IntegerField()
	distance   = models.IntegerField()
	meter      = models.CharField(max_length=20)
	active 	   = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.title


	class Meta:
		verbose_name_plural = "FoodStore"
