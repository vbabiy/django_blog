from django.conf.urls.defaults import *
from django_blog.blog.models import Tag

display_dict = {
    'queryset' : Tag.objects.all(),
    'template_name' : 'blog/category_detail.html',
}

urlpatterns = patterns('django.views.generic.list_detail',
    
    # Display Post in Category
    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', display_dict, name="tag_detail"),
    
)