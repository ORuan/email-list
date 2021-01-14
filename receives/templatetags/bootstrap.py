from django import template


register = template.Library()

@register.filter(name='class')
def addClass(value, arg):
    return value.as_widget(attrs={'class': arg})