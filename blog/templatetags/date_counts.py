from django import template
from django.db import models

register = template.Library()

class DateCount(object):
    def __init__(self, date, count):
        self.date = date;
        self.count = count
    

class DateCountNode(template.Node):
    def __init__(self, model, date_field, on, context_var):
        self.model = model
        self.date_field = date_field
        self.on = on
        self.context_var = context_var
        
    def render(self, context):
        dates = []
        for date in self.model._default_manager.dates(self.date_field, self.on):                    
            count = self.model._default_manager.filter(date_published__year=date.year).filter(date_published__month=date.month).count()
            dates.append(DateCount(date.date, count))
            
        context[self.context_var] = dates
        return ''
    
def do_date_count(parser, token):
    bits = token.split_contents()
    tag_name = bits[0]
    
    if len(bits) != 7:
        raise template.TemplateSyntaxError, "%r tag requires 7 argumetns" % tag_name
    
    model_bits = bits[2].split('.')
    model = models.get_model(model_bits[0], model_bits[1])
    
    return DateCountNode(model, model_bits[2], bits[4], bits[6])
    
    
register.tag('date_counts', do_date_count)