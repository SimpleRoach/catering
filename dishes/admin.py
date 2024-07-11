from django.contrib import admin

from dishes.models import Categories, Products

admin.site.register(Categories)
admin.site.register(Products)