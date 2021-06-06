from django.db import models
from django.contrib.auth.models import User
import os

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=120)
	message = models.TextField()
	deadline = models.DateField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class OrderFile(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	file = models.FileField(upload_to='files/')

	def __str__(self):
		return f"{self.order.id}"

	def filename(self):
		return os.path.basename(self.file.name)