from django.contrib import admin

from .models import Player, Profile


class PlayerAdminConfig(admin.ModelAdmin):
    """Class **PlayerAdminConfig** displays players list in admin panel
    based on :class:`players.models.Player` model.

    """

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


class ProfileAdminConfig(admin.ModelAdmin):
    """Class **ProfileAdminConfig** displays list of players profiles in admin panel.
    Based on :class:`players.models.Profile` model.

    """

    list_display = (
        "player",
        "score",
        "status",
        "is_push_notification",
        "is_findable",
        "is_invitable",
    )
    list_filter = (
        "status",
        "is_push_notification",
        "is_findable",
        "is_invitable",
    )
    search_fields = ("player__nick",)
    list_per_page = 50


admin.site.register(Profile, ProfileAdminConfig)
admin.site.register(Player, PlayerAdminConfig)
