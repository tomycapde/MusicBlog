from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=150, null = True)
    description = RichTextUploadingField(null = True, config_name='description')
    body = RichTextUploadingField(null = True, config_name='default')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    date = models.DateTimeField(auto_now_add=True)
    images = RichTextUploadingField(null = True, config_name='image')
    category = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    
    def __str__(self):
        return self.title
