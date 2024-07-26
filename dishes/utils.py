from dishes.models import Categories


# Вечная весна
class DataMixin:
    title_page = None
    extra_context = {}
    categories = Categories.objects.all()
    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page.title

        if 'categories' not in self.extra_context:
            self.extra_context['categories'] = self.categories

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.title_page:
            context['title'] = self.title_page

        if 'categories' not in context:
            context['categories'] = self.categories

        context.update(self.extra_context)
        return context