from django.contrib import admin

from .models import Category, DifficultyLevel


class CategoryAdminConfig(admin.ModelAdmin):
    """Class **CategoryAdminConfig**
    displays categories list in admin panel based on :class:`decks.models.Category` model."""

    list_display = ("name", "description")
    search_fields = ("name",)
    list_editable = ("description",)
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 50


class DifficultyLevelAdminConfig(admin.ModelAdmin):
    """Class **DifficultyAdminConfig**
    displays difficulty levels list in admin panel based on :class:`decks.models.DifficultyLevel` model."""

    ordering = ("name",)
    list_display = ("name", "value")
    search_fields = ("name",)
    list_display_links = ("name",)
    list_per_page = 50


admin.site.register(Category, CategoryAdminConfig)
admin.site.register(DifficultyLevel, DifficultyLevelAdminConfig)
