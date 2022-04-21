from django.db import models


class User(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    title = models.CharField(max_length=10)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    picture = models.URLField(max_length=300)
