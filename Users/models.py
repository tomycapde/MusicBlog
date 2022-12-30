from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    # user vinculate
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # folder in media
    image = models.ImageField(upload_to='avatars', blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.image}"
    
