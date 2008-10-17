from django.db import models
from django_blog.profiles.models import User

class Tag(models.Model):
        name=models.CharField(max_length=255)
        
        def __str__(self):
                return self.name
        
class Category(models.Model):
        name=models.CharField(max_length=255)
        
        def __str__(self):
                return self.name

class Post(models.Model):
        title=models.CharField(max_length=255)
        body=models.TextField()
        date_crated=models.DateTimeField(auto_now=True)
        date_modifed=models.DateTimeField(auto_now_add=True)
        date_published=models.DateTimeField()
        created_by=models.ForeignKey(User)
        categories = models.ManyToManyField(Category)
        tags = models.ManyToManyField(Tag)
        
        def __str__(self):
                return self.title

