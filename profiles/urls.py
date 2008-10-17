from django.conf.urls.defaults import *


urlpatterns = patterns('django_blog.profiles.views',
    # profiles
    (r'^(\d)/$', 'view_user'),
)
