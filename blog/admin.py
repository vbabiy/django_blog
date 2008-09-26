from django.contrib import admin
from django_blog.blog.models import Post

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)