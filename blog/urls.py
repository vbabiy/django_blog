from django.conf.urls.defaults import *


urlpatterns = patterns('django_blog.blog.views',
    # Blog
    (r'^$', 'recent_post'),
    (r'^(\d)/$', 'view_post'),
)
