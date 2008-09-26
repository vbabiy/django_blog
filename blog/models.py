from django.db import models
from django_blog.profiles.models import User

class Post(models.Model):
        title=models.CharField(max_length=255)
        body=models.TextField()
        date_crated=models.DateTimeField(auto_now=True)
        date_modifed=models.DateTimeField(auto_now_add=True)
        date_published=models.DateTimeField()
        created_by=models.ForeignKey(User)