from django_blog.blog.models import Post, Category, Tag
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

#def recent_post(request):    
#    context = RequestContext(request, {
#        "post_list": Post.objects.filter(status__exact=Post.LIVE_STATUS).all(),
#    })
#    return render_to_response("index.html", context)
#
#def view_post(request, post_id):
#    post=get_object_or_404(Post, id=post_id)
#    
#    context = RequestContext(request, {
#        "post" : post
#    })
#    
#    return render_to_response("blog/view.html", context)