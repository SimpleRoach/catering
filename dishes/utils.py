from dishes.models import Categories


# Вечная весна
class DataMixin:
    title_page = None
    extra_context = {}
    categories = Categories.objects.all()

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'categories' not in self.extra_context:
            self.extra_context['categories'] = self.categories

    def get_mixin_context(self, context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context