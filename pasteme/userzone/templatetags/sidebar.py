from django import template
from django.template import Template

register = template.Library()

@register.inclusion_tag('userzone/sidebar_partial.html')
def sidebar_content():
    return {
        'link': 'aaa',
    }
