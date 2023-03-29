from django.contrib import admin

from .models import Tag


class TagAdminConfig(admin.ModelAdmin):
    """Class **TagAdminConfig** displays tags list in admin panel based on :class:`decks.models.Tag` model."""

    list_display = ("name", "description")
    search_fields = ("name",)
    list_editable = ("description",)
    list_display_links = ("name",)
    list_filter = ("name",)
    list_per_page = 50


admin.site.register(Tag, TagAdminConfig)
