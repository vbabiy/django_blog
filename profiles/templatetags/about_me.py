from django import template
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

register = template.Library()

class AboutMeNode(template.Node):
    def render(self, context):
        context['about_me_user'] = User.objects.get(id=settings.ABOUT_ME_USER_ID)
        return ''
    
def do_about_me(parser, token):
    return AboutMeNode()
    
    
register.tag('about_me', do_about_me)
