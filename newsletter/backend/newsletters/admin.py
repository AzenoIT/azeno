from django.contrib import admin

from .models import Agreements


class AgreementsAdminConfig(admin.ModelAdmin):
    """Class **AgreementsAdminConfig**
    displays categories list in admin panel based on :class:`newsletters.models.Agreements` model."""

    list_display = ("email", "checkbox_1", "checkbox_2", "checkbox_3")
    search_fields = ("email",)
    list_editable = ("checkbox_1", "checkbox_2", "checkbox_3")
    list_display_links = ("email",)
    list_filter = ("email",)
    list_per_page = 50


admin.site.register(Agreements, AgreementsAdminConfig)
