from django.db import models

class Profile(models.Model):
    # nickname = models.CharField(max_length=30)
    photo=models.ImageField(upload_to='profile_image',blank=True)
     
