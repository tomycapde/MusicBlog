from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=150, null = True)
    description = models.CharField(max_length=255, null = True)
    body = models.CharField(max_length=2000, null = True)
    author = models.CharField(max_length=50, null = True)
    date = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='img_post/', blank=True)
    content = RichTextUploadingField(null = True)
    
    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    
    def __str__(self):
        return self.title
