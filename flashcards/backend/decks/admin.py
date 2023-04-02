from django.contrib import admin

from .models import Category


class CategoryAdminConfig(admin.ModelAdmin):
    """Class **CategoryAdminConfig**
    displays categories list in admin panel based on :class:`decks.models.Category` model."""

    list_display = ("name", "description")
    search_fields = ("name",)
    list_editable = ("description",)
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 50


admin.site.register(Category, CategoryAdminConfig)
