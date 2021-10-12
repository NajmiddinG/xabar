from django.db import models

class Message(models.Model):
    who = models.EmailField(max_length=100)
    towhom = models.EmailField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=5000)
    time = models.DateTimeField(auto_now_add=True)