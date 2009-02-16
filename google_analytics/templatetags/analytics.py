from django import template
from django.conf import settings

from django.template import Context, loader

register = template.Library()

@register.simple_tag
def analytics():
    'You must define ANALYTICS_ID = "UA-XXXXXXX-X" in your settings.py'

    analytics_id = getattr(settings, 'ANALYTICS_ID', None)
    if analytics_id.strip() != '':
        t = loader.get_template ('analytics/analytics_template.html')
        c = Context({
            'analytics_code': analytics_id,
        })
        return t.render(c)

    else:
        return ""

