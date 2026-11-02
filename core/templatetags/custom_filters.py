from django import template

register = template.Library()

@register.filter(name='length_is')
def length_is(value, arg):
    """
    Compatibility filter for Django 5.1+ where length_is was removed.
    Returns True if len(value) == int(arg), otherwise False.
    """
    try:
        return len(value) == int(arg)
    except (ValueError, TypeError):
        return ''
