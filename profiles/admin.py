from django.contrib import admin
from django_blog.profiles.models import User

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)