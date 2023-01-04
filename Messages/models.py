from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    content = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(null = True)
    
    def __str__(self):
        return f"From: {self.sender} to: {self.receiver} {self.date}" 
    
    def is_seen(self):
        if self.seen == True:
            return "Leido"
        else:
            return "No leido"