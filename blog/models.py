from django.db import models
from django_blog.profiles.models import User

class Tag(models.Model):
        name=models.CharField(max_length=255)
        
        def __unicode__(self):
                return self.name
        
class Category(models.Model):
        name=models.CharField(max_length=255)
        
        def __unicode__(self):
                return self.name

class Post(models.Model):
        
        # Statuses
        LIVE_STATUS = 1
        DRAFT_STATUS = 2
        HIDDEN_STATUS = 3
        
        statuses = (
                (LIVE_STATUS, 'Live'),
                (DRAFT_STATUS, 'Draft'),
                (HIDDEN_STATUS,'Hidden'),
        )
        
        title = models.CharField(max_length=255)
        slug = models.SlugField(unique_for_date="date_published")
        body = models.TextField()
        status = models.IntegerField(choices=statuses)        
        created_by = models.ForeignKey(User)

        categories = models.ManyToManyField(Category)
        tags = models.ManyToManyField(Tag)
        
        date_crated = models.DateTimeField(auto_now=True)
        date_modifed = models.DateTimeField(auto_now_add=True)
        date_published = models.DateTimeField()
        
        
        def __unicode__(self):
                return self.title

