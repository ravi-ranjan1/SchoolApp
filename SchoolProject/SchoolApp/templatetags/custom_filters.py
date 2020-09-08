from django import template
register=template.Library()

@register.filter(name='name_filter')
def name_filter(value):
    if value.istitle():
        result=value
        return result