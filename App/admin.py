from django.contrib import admin
from .models import Post, FAQ

# Register your models here.

admin.site.register(Post)
admin.site.register(FAQ)