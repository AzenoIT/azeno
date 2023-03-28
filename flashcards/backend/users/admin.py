from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class UserAdminConfig(UserAdmin):
    """Customized configuration for admin panel prepared for :class:`users.models.CustomUser` model.
    If order of fields in admin panel is not to your liking
    it can be changed in list_display class field.
    """

    model = User
    search_fields = ("email", "username")
    list_filter = ("email", "username", "is_active", "is_staff")
    ordering = ("-last_login",)
    list_display = ("email", "username", "is_active", "is_staff")


admin.site.register(User, UserAdminConfig)
