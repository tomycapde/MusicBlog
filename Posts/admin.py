from django.contrib import admin

# Register your models here.

from Posts.models import *

admin.site.register(Topic)
admin.site.register(Post)