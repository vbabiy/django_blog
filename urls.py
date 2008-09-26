from django.conf.urls.defaults import *
<<<<<<< HEAD:urls.py
from django_blog.blog.views import recent_post

import os.path

from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',
	# Images, Csss, etc...
    (r'site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media }),
    
    # Blog
    (r'^blog/', include('django_blog.blog.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)
