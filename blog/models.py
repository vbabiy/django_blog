from django.db import models
from django.contrib.comments.signals import comment_will_be_posted
from django.contrib.comments.models import Comment
from markdown import markdown
from django.contrib.auth.models import User


class Tag(models.Model):
        name=models.CharField(max_length=255)
        slug=models.SlugField(unique=True)
        
        def __unicode__(self):
                return self.name
            
        class Meta:
            ordering = ['name']
        
        @models.permalink
        def get_absolute_url(self):
            return('tag_detail', (), {'slug': self.slug })
        
class Category(models.Model):
        name=models.CharField(max_length=255)
        slug=models.SlugField(unique=True)
        
        def __unicode__(self):
                return self.name
            
        class Meta:
            ordering = ['name']
        
        @models.permalink
        def get_absolute_url(self):
                return('category_detail', (), {'slug': self.slug })
     
class Live(models.Manager):
    """
    Customer Manager that is aware of Post statues
    """

    def get_query_set(self):
        return super(Live, self).get_query_set().filter(status__exact=Post.LIVE_STATUS)
    
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
        
        date_created = models.DateTimeField(auto_now=True, editable=False)
        date_modifed = models.DateTimeField(auto_now_add=True, editable=False)
        date_published = models.DateTimeField(editable=False)
        
        # manager
        live = Live()
        objects = models.Manager()
        
        class Meta:
                ordering = ['-date_published']
                
        def save(self):
            import datetime
            self.date_published = datetime.datetime.now()
            super(Post, self).save()

        @models.permalink
        def get_absolute_url(self):
                return('post_detail', (), {
                    'year': self.date_published.strftime("%Y"),
                    'month': self.date_published.strftime("%b").lower(),
                    'day': self.date_published.strftime("%d"),
                    'slug': self.slug })
        
        def __unicode__(self):
                return self.title
        
        
# Signals
def pre_save_comment(sender, **kargs):
    """
    Run comment through a markdown filter
    """
    if 'comment' in kargs:
        comment = kargs['comment']
        comment.comment = markdown(comment.comment)
    
    
comment_will_be_posted.connect(pre_save_comment, Comment)
