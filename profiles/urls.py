from django.conf.urls.defaults import *


urlpatterns = patterns('django_blog.profiles.views',
	url(r'^create', 'create_user', name='create_user'),
	url(r'^(?P<username>[-\w]+)/$', 'display_profile', name='display_profile'),
)
