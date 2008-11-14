from django.conf.urls.defaults import *
from django_blog.blog.models import Post

index_dict = {
    'queryset': Post.live.all(),
    'date_field': 'date_published',
    'template_object_name': 'post_list',
}

display_dict = {
    'queryset': Post.live.all(),
    'date_field': 'date_published',
    'template_name': 'blog/post_detail.html',
    'extra_context': { 'post_display' : True },
}

month_dict = {
    'queryset': Post.live.all(),
    'date_field': 'date_published',
    'template_name': 'blog/post_archive.html',
    'template_object_name':'post'
}

year_dict = {
    'queryset': Post.live.all(),
    'date_field': 'date_published',
    'template_name': 'blog/post_archive.html',
    'template_object_name':'post',
    'make_object_list': True
}

urlpatterns = patterns('django.views.generic.date_based',
    # Post List
    url(r'^$', 'archive_index', index_dict, 'blog_post_archive_list'),
    
    # Display Post
    url(r'^(?P<year>(\d){4})/(?P<month>(\w){3})/(?P<day>(\d){2})/(?P<slug>[-\w]+)/$', 'object_detail', display_dict, name="post_detail"),
        
    # Monthly Archive
    url(r'^(?P<year>(\d){4})/(?P<month>(\w){3})/$', 'archive_month', month_dict, name="post_month" ),
    
    # Yearly Archive
    (r'^(?P<year>(\d){4})/$', 'archive_year', year_dict, "post_year" ),

)