from django import template
from django.db import models

class ObjectCountNode(template.Node):
    def __init__(self, model, context_var):
        self.model = model;
        self.context_var = context_var
        
    def render(self, context):
        context[self.context_var] = self.model.objects.all()
        return '';
        

def get_model_name(token, tag_name):
    bits = token.split('.')
    if len(bits) != 2:
        raise template.TemplateSyntaxError, "%r tag model is not vaild" % tag_name

    return bits

def do_object_cout(parser, token):
    bits = token.split_contents()
    tag_name = bits[0]
    
    if len(bits) < 4:
        raise template.TemplateSyntaxError, "%r tag requires 3 argumetns" % tag_name
    
    model_name = get_model_name(bits[2], tag_name)
    model = models.get_model(*model_name)
    
    if not model:
        raise template.TemplateSyntaxError, "%r tag model is invalid %r" % (tag_name, model_name)
    
    return ObjectCountNode(model, bits[4])

register = template.Library()
register.tag('object_counts', do_object_cout)
