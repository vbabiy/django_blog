from django.contrib import admin
from django_blog.profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
