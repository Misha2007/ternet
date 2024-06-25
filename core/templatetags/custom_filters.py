# site_project_django/core/templatetags/custom_tags.py

from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def set_break(context, value=True):
    context['break_loop'] = value
    return ''

@register.filter
def check_break(value, context):
    return context.get('break_loop', False)
