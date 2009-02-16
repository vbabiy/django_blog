from django.contrib.syndication.feeds import Feed
from django_blog.blog.models import Post, Category


class LatestPosts(Feed):
    title = "Latest Posts"
    link = ""
    description = "The Latest posts from the blog."
    
    def items(self):
        return Post.live.order_by('-date_published') [:10]
    
class Categories(Feed):
    description = ""
    
    def get_object(self, bits):
        if len(bits) != 1:
            raise Category.DoesNotExist
        return Category.objects.get(slug=bits[0])
    
    def title(self, obj):
        return obj.name
        
    def link(self, obj):
        return obj.get_absolute_url()

    def items(self, obj):
        return obj.post_set.all()
