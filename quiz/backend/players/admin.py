from django.contrib import admin

from .models import Player


class PlayerAdminConfig(admin.ModelAdmin):
    """Class **PlayerAdminConfig** displays players list in admin panel based on **Player** model."""

    list_display = ("nick", "rank", "is_bot", "created_at", "is_active")
    search_fields = ("nick",)
    list_editable = (
        "rank",
        "is_active",
    )
    list_display_links = ("nick",)
    save_on_top = True
    list_filter = (
        "is_bot",
        "created_at",
    )
    list_per_page = 50


admin.site.register(Player, PlayerAdminConfig)
