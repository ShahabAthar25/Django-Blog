from django.contrib import admin
from .models import Post, FAQ, aboutmodel

# Register your models here.

admin.site.register(Post)
admin.site.register(FAQ)
admin.site.register(aboutmodel)