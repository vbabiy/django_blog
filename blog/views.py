from django_blog.blog.models import Post, Category, Tag
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def recent_post(request):
    current_posts=Post.objects.order_by("-date_published").all()
    categories = Category.objects.order_by("name")
    tags = Tag.objects.order_by("name")
    
    context = RequestContext(request, {
        "posts": current_posts,
        "categories": categories,
        "tags": tags
    })
    
    return render_to_response("index.html", context)

def view_post(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    
    context = RequestContext(request, {
        "post" : post
    })
    
    return render_to_response("blog/view.html", context)