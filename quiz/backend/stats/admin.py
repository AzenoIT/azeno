from django.contrib import admin

from .models import Badge, PlayerBadge


class BadgeAdminConfig(admin.ModelAdmin):
    """Class **BadgeAdminConfig** displays list of badges
    in Django admin panel and is based on :class:`stats.models.Badge` model.

    .. admonition:: Note

        This is a basic configuration that can be expanded.

    """

    list_display = (
        "name",
        "points",
        "created_at",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_editable = ("points",)
    save_on_top = True
    list_filter = ("points",)
    ordering = ("points",)


class PlayerBadgeAdminConfig(admin.ModelAdmin):
    list_display = (
        "badge",
        "player",
        "obtained_on",
    )
    search_fields = (
        "badge",
        "player",
    )
    list_filter = ("obtained_on",)
    ordering = ("-obtained_on",)


admin.site.register(PlayerBadge, PlayerBadgeAdminConfig)
admin.site.register(Badge, BadgeAdminConfig)
