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
            verbose_name_plural = "categories"
        
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
        author = models.ForeignKey(User)

        categories = models.ManyToManyField(Category)
        tags = models.ManyToManyField(Tag)
        
        date_created = models.DateTimeField(auto_now=True, editable=False)
        date_modified = models.DateTimeField(auto_now_add=True, editable=False)
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
        
        
import akismet
from django.conf import settings
from django.contrib.sites.models import Site 


# Signals
def pre_save_comment(sender, **kargs):
    """
    Run comment through a markdown filter
    """
    if 'comment' in kargs:
        comment = kargs['comment']
        
        # If in debug mode skip this check with Akismet
        if not settings.DEBUG:
            try:
                real_key = akismet.verify_key(settings.AKISMET_KEY ,Site.objects.get_current().domain)
                if real_key:
                    is_spam = akismet.comment_check(settings.AKISMET_KEY ,Site.objects.get_current().domain, comment.ip_address, None, comment_content=comment.comment)
                    if is_spam:
                        comment.is_public = False
                        print "That was spam"
            except akismet.AkismetError, e:
                print e.response, e.statuscode
        
        # Apply markdown
        comment.comment = markdown(comment.comment)

comment_will_be_posted.connect(pre_save_comment, Comment)
