from django.contrib.syndication.feeds import Feed
from django_blog.blog.models import Post


class LatestPosts(Feed):
    title = "Latest Posts"
    link = ""
    description = ""
    
    def items(self):
        return Post.live.order_by('-date_published') [:10]
