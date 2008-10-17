from django_blog.profiles.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def view_user(request, user_id):
    user=User.objects.get(id=user_id)
    context = RequestContext(request, {
        "user_view": user
    })
    
    return render_to_response("profiles/user.html", context)