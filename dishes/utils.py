from dishes.models import Categories


class DataMixin:
    title_page = None
    extra_context = {}
    categories = Categories.objects.all()
    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page.title

        if 'categories' not in self.extra_context:
            self.extra_context['categories'] = self.categories