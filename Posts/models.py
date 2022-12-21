from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=350)
    body = models.CharField(max_length=2000)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img_post/', blank=True)
