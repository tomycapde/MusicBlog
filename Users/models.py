from django.db import models
from django.contrib.auth.models import User

# Model Profile contains all data for users   
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.user)
    
    def get_avatar(self):
        return self.avatar