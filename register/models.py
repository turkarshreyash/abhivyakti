from django.db import models

# Create your models here.
class participants(models.Model):
    event = models.CharField(max_length=30)
    email = models.CharField(max_length=50)