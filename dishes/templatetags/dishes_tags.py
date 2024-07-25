from django import template
import dishes.views as views

register = template.Library()

@register.inclusion_tag(filename='dishes/list_categories.html')
def show_categories():
    return {}