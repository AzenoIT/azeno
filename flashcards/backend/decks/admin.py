from django.contrib import admin

from .models import Category, Tag, Deck, DifficultyLevel


class CategoryAdminConfig(admin.ModelAdmin):
    """Class **CategoryAdminConfig**
    displays categories list in admin panel based on :class:`decks.models.Category` model."""

    list_display = ("name", "description")
    search_fields = ("name",)
    list_editable = ("description",)
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 50


class TagAdminConfig(admin.ModelAdmin):
    """Class **TagAdminConfig** displays tags list in admin panel based on :class:`decks.models.Tag` model."""

    list_display = ("name",)
    search_fields = ("name",)
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 50


class DeckAdminConfig(admin.ModelAdmin):
    """**DeckAdminConfig** is a configuration class for :class:`decks.models.Deck` model in the admin panel."""

    list_display = ("name", "is_public", "price", "author", "rating", "is_active", "created_at")
    search_fields = ("name",)
    list_editable = ("price", "is_public", "is_active")
    list_display_links = ("name",)
    save_on_top = True
    list_filter = ("is_public", "is_active", "author", "category")
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
admin.site.register(Tag, TagAdminConfig)
admin.site.register(Deck, DeckAdminConfig)
admin.site.register(DifficultyLevel, DifficultyLevelAdminConfig)
