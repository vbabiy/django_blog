from django.conf.urls.defaults import *

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
    (r'^blog/', include('blog.urls.posts')),

    # Profiles
    (r'^profiles/', include('django_blog.profiles.urls')),

    # Flat Pages
    (r'^flat/', include('django.contrib.flatpages.urls')),

    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)
