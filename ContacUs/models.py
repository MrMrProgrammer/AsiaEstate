from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
