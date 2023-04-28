from django.contrib import admin

from .models import AccountType, Player


class AccountTypeAdminConfig(admin.ModelAdmin):
    """Class **AccountTypeAdminConfig** displays account types list in admin panel
    based on :class:`players.models.AccountType` model."""

    list_display = ("name", "duration", "cost")
    search_fields = ("name",)
    list_display_links = ("name",)
    save_on_top = True
    list_per_page = 10


class PlayerAdminConfig(admin.ModelAdmin):
    """Class **PlayerAdminConfig** displays players list in admin panel
    based on :class:`players.models.Player` model."""

    list_display = ("nick", "user", "account_type", "created_at", "is_active")
    search_fields = ("nick", "user__email")
    list_editable = (
        "account_type",
        "is_active",
    )
    list_display_links = ("nick",)
    save_on_top = True
    list_filter = ("account_type",)
    list_per_page = 50


admin.site.register(Player, PlayerAdminConfig)
admin.site.register(AccountType, AccountTypeAdminConfig)
