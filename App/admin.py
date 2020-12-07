from django.contrib import admin
from .models import Post, FAQ, About, Category

# Register your models here.

admin.site.register(Post)
admin.site.register(FAQ)
admin.site.register(About)
admin.site.register(Category)