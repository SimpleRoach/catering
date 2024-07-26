from django import template
import dishes.views as views

register = template.Library()

@register.inclusion_tag(filename='dishes/list_drop_categories.html')
def show_drop_categories():
    view_instance = views.CatalogListView()
    view_instance.object_list = view_instance.get_queryset()
    context = view_instance.get_context_data()
    categories  = context.get('categories', [])
    return {'categories ':categories }
